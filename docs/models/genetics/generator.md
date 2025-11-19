---
title: GENERator — Model Card (light)
status: draft
updated: 2025-11-16
---

# GENERator

Purpose
- Long-context generative DNA LM.

Hygiene
- Tokenizer sensitivity (k-mer/BPE) and RC handling; apply RC at nucleotide level pre-tokenization.

Implications
- Be explicit about tokenization scheme; test RC averaging stability.

Primary notes (KB summary)
- PDF: [docs/generated/kb_curated/papers-pdf/generator_2024.pdf](../../generated/kb_curated/papers-pdf/generator_2024.pdf)
- Original inputs: `pdf<->md;ai-summaries/input/generator_2024/`.
- Original paper:[arXiv:2502.07272](https://arxiv.org/abs/2502.07272)

Source repo
- **Local**: `external_repos/generator/`
- **GitHub**: [GenerTeam/GENERator](https://github.com/GenerTeam/GENERator)