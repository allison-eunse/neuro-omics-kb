# Caduceus Code Walkthrough

## Overview

Caduceus is a bi-directional, reverse-complement equivariant DNA foundation model based on Mamba + Hyena architecture, achieving state-of-the-art performance on genomic tasks.

**Key Features:**
- Architecture: RC-equivariant Hyena + Mamba
- Context: 131,072 bp
- Parameters: ~150M
- Special: Reverse-complement parameter sharing (RCPS)

## Quick Start

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

model = AutoModelForMaskedLM.from_pretrained(
    "kuleshov-group/caduceus-ps_seqlen-131k_d_model-256_n_layer-16"
)
tokenizer = AutoTokenizer.from_pretrained(
    "kuleshov-group/caduceus-ps_seqlen-131k_d_model-256_n_layer-16"
)

# Inference
sequence = "ACGTACGT" * 1000
inputs = tokenizer(sequence, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits
```

## Training

```bash
# Fine-tune on genomic benchmarks
python train.py experiment=hg38/genomic_benchmark \
    dataset.dataset_name=human_enhancers_ensembl \
    model.config.pretrained_model_name_or_path=kuleshov-group/caduceus-ps_... \
    optimizer.lr=5e-5
```

## Extract Embeddings

```python
model.config.output_hidden_states = True
outputs = model(**inputs, output_hidden_states=True)
embeddings = outputs.hidden_states[-1].mean(dim=1)
```

## Performance

- Human Enhancers: 89.2%
- Human vs Worm: 97.1%
- ClinVar AUROC: 0.82

## Links

- Repo: https://github.com/kuleshov-group/caduceus
- Models: https://huggingface.co/collections/kuleshov-group/caducues-65dcb89b4f54e416ef61c350
- Model Card: kb/model_cards/caduceus.yaml
