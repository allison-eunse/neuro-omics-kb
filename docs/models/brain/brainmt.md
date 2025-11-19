---
title: BrainMT — Model Card (light)
status: draft
updated: 2025-11-16
---

# BrainMT

Primary notes (KB summary)
- **Publication:** Conference paper on SpringerLink (Lecture Notes in Computer Science, pp. 150–160), first online 19 September 2025.
- **Official PDF (KB summary):** [docs/generated/kb_curated/papers-pdf/brainmt_2025.pdf](../../generated/kb_curated/papers-pdf/brainmt_2025.pdf) (synced from `pdf<->md;ai-summaries` pipeline; originals in `pdf<->md;ai-summaries/input/brainmt_2025/`).
- **Original publication:** [LNCS DOI 10.1007/978-3-032-05162-2_15](https://dl.acm.org/doi/10.1007/978-3-032-05162-2_15)
- **Summary card:** `kb/paper_cards/brainmt_2025.yaml` with authors/tasks/datasets.
- **Code reference:** `external_repos/brainmt/` (hybrid Mamba + Transformer architecture, 3D Conv patch embed → Mamba blocks → MHSA).

## Purpose
- Multitask brain transformer that fuses bidirectional Mamba blocks (temporal-first scanning) with transformer attention to model long-range fMRI.
- Targets fluid intelligence regression, sex classification, and auxiliary harmonization tasks across UKB/HCP cohorts.

## Usage for Us
- Defer until BrainLM/Brain-JEPA baselines are exhausted; BrainMT training/inference is heavier and requires fused kernels.
- When exporting embeddings, capture metadata about sequence length (≥200 frames) and masking ratio to maintain published accuracy.
- Preferred when we need multitask heads or more robustness to long temporal contexts; otherwise keep simpler ViT/JEPA encoders in rotation.

Source repo
- **Local**: `external_repos/brainmt/`
- **GitHub**: [arunkumar-kannan/brainmt-fmri](https://github.com/arunkumar-kannan/brainmt-fmri)
