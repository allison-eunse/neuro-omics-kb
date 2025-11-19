Dataset card schema (one YAML per dataset under `kb/datasets/`):

```
id: unique_slug
name: Human-readable title
description: Short paragraph
storage_location:
  bucket|huggingface|drive|source: URI or path
schema_ref: docs/data/schemas.md#anchor
dtypes: description of expected file types
required_columns:
  - column
modalities:
  - dna|fmri|clinical
modality_columns:
  dna:
    - gene_symbol
  fmri:
    - roi_mean
hf_sources:
  - repo: author/dataset
    subset: gener_tasks
subset_counts:
  train: 80000
  validation: 10000
  test: 10000
counts:
  subjects|records|base_pairs: numeric summary
base_pair_stats:
  total_bp: 1.2e8
  mean_seq_len: 1024
access: public|restricted|mixed
access_notes: Licensing / DUA notes + contact trail
license: SPDX or descriptive string
restrictions: Notes on compliance/PII
maintainers:
  - name: Contact or team
external_repos:
  - path: external_repos/caduceus
code_walkthrough_refs:
  - docs/code_walkthroughs/caduceus_walkthrough.md
verified: true|false
last_updated: YYYY-MM-DD
```

Always cross-link whichever `external_repos/*` workflow wrote the tensors and the walkthrough that documents preprocessing so downstream users can trace provenance.
