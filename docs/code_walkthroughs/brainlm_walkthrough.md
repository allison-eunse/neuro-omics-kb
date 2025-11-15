# BrainLM Code Walkthrough

## Overview

BrainLM is a masked autoencoder foundation model for fMRI, learning representations through self-supervised pretraining on UK Biobank.

**Key Features:**
- Architecture: ViT-MAE + Nystromformer
- Parameters: 111M / 650M
- Input: 424 voxels × 490 timepoints
- Masking: 75-90% random per-voxel

## Quick Start

```python
from brainlm_mae.modeling_brainlm import BrainLMForPreTraining

model = BrainLMForPreTraining.from_pretrained(
    "vandijklab/brainlm",
    trust_remote_code=True
)
model = model.cuda().eval()
```

## Extract [CLS] Token

```python
def extract_cls_embedding(model, fmri_data):
    """
    Args:
        fmri_data: [B, 424, 490] tensor
    Returns:
        cls_embedding: [B, hidden_size] tensor
    """
    with torch.no_grad():
        outputs = model(fmri_data, mask_ratio=0.0)
        cls_token = outputs.last_hidden_state[:, 0, :]
    return cls_token.cpu().numpy()
```

## Training

```bash
# Pretrain
python train.py \
    --data_path /mnt/ukb_fmri/arrow \
    --mask_ratio 0.75 \
    --learning_rate 1.5e-4 \
    --num_epochs 100

# Fine-tune
python train.py \
    --pretrained_checkpoint pretrained_models/brainlm_111m.pth \
    --task_type classification \
    --learning_rate 1e-5
```

## Downstream Tasks

### K-NN Regression

```python
from sklearn.neighbors import KNeighborsRegressor

knn = KNeighborsRegressor(n_neighbors=10)
knn.fit(embeddings_train, labels_train)
predictions = knn.predict(embeddings_test)
```

### MLP Probe

```python
probe = nn.Sequential(
    nn.Linear(768, 512),
    nn.ReLU(),
    nn.Dropout(0.3),
    nn.Linear(512, num_classes)
)
```

## Performance

- Age (K-NN): 0.72 correlation
- Age (fine-tuned): 0.85 correlation
- Sex: 94.2% accuracy

## Links

- Repo: https://github.com/vandijklab/BrainLM
- Model: https://huggingface.co/vandijklab/brainlm
- Model Card: kb/model_cards/brainlm.yaml
