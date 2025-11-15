# SwiFT Code Walkthrough

## Overview

SwiFT (Swin 4D fMRI Transformer) is a scalable foundation model using hierarchical 4D windows for fMRI analysis.

**Key Features:**
- Architecture: Swin Transformer 4D
- Parameters: ~80M
- Input: 96×96×96 voxels × 20 timepoints
- Training: PyTorch Lightning

## Quick Start

```python
from project.module.models.swin4d_transformer_ver7 import Swin4DTransformer

model = Swin4DTransformer(
    img_size=(96, 96, 96),
    patch_size=(4, 4, 4),
    in_chans=20,
    embed_dim=96
)
```

## Training

### Contrastive Pretraining

```bash
python project/main.py \
    --project_name swift_pretrain \
    --dataset_name UKB \
    --upstream contrastive \
    --batch_size 32 \
    --gpus 4
```

### Supervised Fine-Tuning

```bash
python project/main.py \
    --dataset_name UKB \
    --downstream_task sex \
    --pretrained_model_path pretrained_models/contrastive_pretrained.ckpt \
    --finetune \
    --lr 5e-5
```

## Extract Embeddings

```python
model = model.cuda().eval()

def extract_embeddings(fmri_data):
    with torch.no_grad():
        features = model(fmri_data.cuda())
        embeddings = features.mean(dim=[2, 3, 4])
    return embeddings.cpu()
```

## Performance

- Sex Classification: 94.2%
- Age Regression: 0.89 correlation
- Fluid Intelligence: 0.76 correlation

## Links

- Repo: https://github.com/Transconnectome/SwiFT
- Model Card: kb/model_cards/swift.yaml
