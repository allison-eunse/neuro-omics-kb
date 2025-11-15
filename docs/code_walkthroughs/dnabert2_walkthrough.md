# DNABERT-2 Code Walkthrough

## Overview

DNABERT-2 is an efficient foundation model using BPE tokenization and ALiBi positional embeddings, achieving state-of-the-art on the GUE benchmark.

**Key Features:**
- Architecture: BERT with ALiBi + BPE
- Parameters: 117M
- Context: 512 tokens
- Special: Multi-species training

## Quick Start

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained(
    "zhihan1996/DNABERT-2-117M",
    trust_remote_code=True
)
model = AutoModel.from_pretrained(
    "zhihan1996/DNABERT-2-117M",
    trust_remote_code=True
)

sequence = "ACGTACGT"
inputs = tokenizer(sequence, return_tensors='pt')
hidden_states = model(**inputs)[0]
cls_embedding = hidden_states[:, 0, :]
```

## Fine-Tuning

```bash
python finetune/train.py \
    --model_name_or_path zhihan1996/DNABERT-2-117M \
    --data_path /mnt/data \
    --learning_rate 3e-5 \
    --per_device_train_batch_size 8 \
    --num_train_epochs 10
```

## With LoRA

```bash
python finetune/train.py \
    --model_name_or_path zhihan1996/DNABERT-2-117M \
    --use_lora \
    --lora_r 8 \
    --learning_rate 1e-4
```

## Performance

- GUE Average: 92.1%
- Promoter Detection: 94.5%
- 3x faster than 6-mer models

## Links

- Repo: https://github.com/Zhihan1996/DNABERT2
- Model: https://huggingface.co/zhihan1996/DNABERT-2-117M
- Model Card: kb/model_cards/dnabert2.yaml
