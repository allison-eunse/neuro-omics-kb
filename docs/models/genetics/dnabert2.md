---
title: DNABERT-2 — Model Card (light)
status: draft
updated: 2025-11-16
---

# DNABERT-2

Tokenization
- BPE/k-mer hybrids; ensure RC is applied before tokenization; maintain frame.

Pooling
- Mean or CLS; verify linear-probe stability.

Notes
- Not strictly RC-equivariant; averaging forward/RC stabilizes.

Primary notes (KB summary)
- Summary pending (no curated `kb_curated` card yet); refer to the Hugging Face card `zhihan1996/DNABERT-2-117M` and the DNABERT-2 paper for full experimental details.

Source repo
- **Local**: `external_repos/dnabert2/`
- **GitHub**: [Zhihan1996/DNABERT2](https://github.com/Zhihan1996/DNABERT2)
