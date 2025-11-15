# Evo 2 Code Walkthrough

## Overview

Evo 2 is a StripedHyena 2-based DNA language model capable of modeling up to 1 million bp at single-nucleotide resolution.

**Key Features:**
- Architecture: StripedHyena 2 (mixer-based)
- Models: 1B, 7B, 40B parameters
- Context: 1,000,000 bp
- Special: FP8 precision, RC scoring

## Quick Start

```python
from evo2 import Evo2

model = Evo2('evo2_7b')

# Generate sequences
output = model.generate(
    prompt_seqs=["ACGT" * 100],
    n_tokens=256,
    temperature=0.8
)
print(output.sequences[0])

# Score sequences
scores = model.score_sequences(
    ['ACGTACGT', 'TGCATGCA'],
    reduce_method='mean'
)
```

## Variant Effect Prediction

```python
ref_seq = "ACGT...reference..."
alt_seq = "ACGT...alternative..."

ref_score = model.score_sequences([ref_seq])[0]
alt_score = model.score_sequences([alt_seq])[0]

effect = alt_score - ref_score  # Positive = deleterious
```

## RC Scoring

```python
# Score both strands
scores = model.score_sequences_rc(
    sequences,
    reduce_method='mean'
)
```

## Performance

- ClinVar AUROC: 0.89
- Handles 1M bp context
- State-of-the-art generation

## Links

- Repo: https://github.com/ArcInstitute/evo2
- Models: https://huggingface.co/arcinstitute
- Model Card: kb/model_cards/evo2.yaml
