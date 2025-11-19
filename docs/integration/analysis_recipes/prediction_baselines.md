---
title: Analysis Recipe — Prediction Baselines
status: ready
updated: 2025-11-18
---

# Prediction Baselines

Inputs
- Gene, Brain, and Fusion = [Gene | Brain], all 512-D after preprocessing (`embedding_strategies.genetics_gene_fm_pca512_v1`, `embedding_strategies.smri_free_surfer_pca512_v1`, `embedding_strategies.fusion_concat_gene_brain_1024_v1`).
- Tabular mode: raw ROI tables (`smri_free_surfer_raw_176`) and genetics PGS (`genetics_pgs_20traits`) for TabPFN / LR / GBDT baselines.

Context in integration plan

- This recipe is the **primary late-fusion baseline**: compare Gene-only, Brain-only, and simple Fusion ([Gene | Brain]) features using shallow models.
- Escalate beyond this (e.g., contrastive two-tower, EI stacking, hub tokens) **only if Fusion clearly and consistently outperforms both single-modality baselines**.
- Keep this runbook as the reference when deciding whether more complex integration architectures are justified.

Models
- Logistic Regression
  - penalty=L2, C∈{0.5,1,2}, solver=saga/liblinear, class_weight=balanced, max_iter=5,000.
- LightGBM
  - num_leaves=31, learning_rate=0.05, n_estimators=1,000 with early stopping, scale_pos_weight ≈ N_neg/N_pos.
- CatBoost
  - depth=6–8, learning_rate=0.05, iterations=2,000 with early stopping, loss_function=Logloss, auto class weights.
- TabPFN (`kb/model_cards/tabpfn.yaml`)
  - Max 10k samples and 500 features per forward pass; chunk folds if N is larger.
  - Use for tabular baselines (raw ROI, PGS, ROI+PGS fusion) to benchmark whether representation learning beats a tabular FM.

Evaluation
- Same CV folds across modalities.
- Metrics: AUROC, AUPRC; report mean ± SD across folds.
- Significance: DeLong or bootstrap for Fusion vs each single-modality on held-out predictions.

Outputs to save
- Per-fold predictions and labels for later DeLong/bootstrap and calibration checks.
- Embedding/harmonization IDs used to produce each feature set (copy from experiment config metadata).
