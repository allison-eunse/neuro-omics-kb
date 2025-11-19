---
title: Modality Features — Genomics
status: ready
updated: 2025-11-18
---

# Genomics Features

## Gene FM embedding (`genetics_gene_fm_pca512_v1`)

- Models: Caduceus, Evo 2, GENERaTOR, DNABERT-2 (see `kb/model_cards/`).
- RC hygiene:
  - Run the encoder on forward and reverse-complement sequences; average token embeddings before pooling.
  - Tokenization: maintain deterministic k-mer/BPE framing; avoid random masking for inference exports.
- Pooling hierarchy:
  1. Token → exon (mean or CLS).
  2. Exon → gene (mean, or attention if pathway-weighted).
  3. Gene set → subject vector (concatenate curated genes; align order with manifest).
- Covariates: residualize age, sex, ancestry PCs 1–10, sequencing batch.
- Dimensionality: PCA → 512 (fit on train fold).
- Retrieve the latest recipe with `python scripts/manage_kb.py ops strategy genetics_gene_fm_pca512_v1`.

## Tabular genetics features (`genetics_pgs_20traits`)

- 20 curated UKB PGS + ancestry PCs.
- Preprocessing: mean-impute missing PGS, z-score each feature inside the train fold.
- Intended for tabular prediction baselines (including TabPFN) and for fusion with sMRI ROI tables.

## Attribution

- Leave-one-gene-out (LOGO) ΔAUC with Wilcoxon across folds + FDR control remains the recommended approach once embeddings feed prediction models.
