# BrainMT Code Walkthrough

## Overview

BrainMT is a hybrid Mamba-Transformer for fMRI, combining bidirectional Mamba for temporal and MHSA for spatial modeling. MICCAI'25.

**Key Features:**
- Architecture: Hybrid Mamba + Transformer
- Parameters: ~120M
- Input: 91×109×91 voxels × 200 frames
- Special: Bidirectional Mamba blocks

## Quick Start

```python
from src.brainmt.models.brain_mt import BrainMT

model = BrainMT(
    hidden_dim=256,
    num_mamba_layers=6,
    num_attention_layers=2,
    bidirectional=True
)
```

## Training

```bash
# Single GPU
python src/brainmt/train.py \
    task=regression \
    dataset.fmri.img_path=/mnt/ukb_fmri/tensors \
    training.learning_rate=1e-4

# Multi-GPU
torchrun --nproc_per_node=2 \
    src/brainmt/train.py \
    task=regression
```

## Configuration

```yaml
model:
  hidden_dim: 256
  num_mamba_layers: 6
  num_attention_layers: 2
  bidirectional: true

training:
  learning_rate: 1e-4
  batch_size: 16
  num_epochs: 100
```

## Extract Features

```python
def extract_features(fmri_data, model):
    with torch.no_grad():
        outputs = model(fmri_data.cuda())
        features = model.get_features()
        pooled = features.mean(dim=1)
    return pooled.cpu().numpy()
```

## Performance

- Fluid Intelligence: 0.76 correlation
- Age: 0.84 correlation
- Sex: 92.1% accuracy

## Links

- Repo: https://github.com/arunkumar-kannan/brainmt-fmri
- Model Card: kb/model_cards/brainmt.yaml
