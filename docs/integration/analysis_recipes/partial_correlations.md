---
title: Analysis Recipe — Partial Correlations
status: ready
updated: 2025-11-16
---

# Partial Correlations

Goal
- Associate canonical scores or PCs with outcomes controlling covariates.

Context in integration plan

- Use this after you have **stable embeddings and late-fusion baselines**: it helps interpret axes (CCA components, PCs) rather than build new predictors.
- Treat it as an analysis layer sitting on top of the late-fusion-first stack, not as a standalone modeling approach.
- Prefer simple, regularized models here; if interpretation depends on heavy models, revisit whether the underlying embeddings/CCA steps are well-behaved.

Continuous outcome (e.g., PHQ-9)
- Residualize x and y on covariates within train folds → rx, ry.
- Correlate rx, ry (Pearson/Spearman); aggregate across folds.

Binary outcome (e.g., MDD)
- Preferred: logistic regression y ~ x + covariates; report OR, CI, p.
- Optional: approximate partial correlation via residuals y − p̂ from covariate-only logistic.

Report
- Per-axis coefficients/correlations with CIs; FDR across multiple tests if many axes.
