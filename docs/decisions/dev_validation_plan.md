---
title: Developmental cohort validation plan (CHA)
status: draft
updated: 2025-11-19
---

## Goal

Define a prospective validation strategy for the CHA developmental cohort so that future models
(brain-only, gene–brain–behaviour, BOM-aligned LLM/VLM) are evaluated on **truly held-out data**.

## High-level plan

- **Retrospective training window**: initial waves (e.g., years 1–N of data collection).
- **Prospective validation window**: later-enrolled participants and/or later waves (e.g., year N+1 onward).
- **Constraints**:
  - Preserve age and diagnosis distributions between train and validation where possible.
  - Avoid leakage across siblings or repeated visits when defining subject-level splits.

## Suggested splits (to refine once data are available)

1. **Temporal split**
   - Train:
     - All subjects enrolled up to a cutoff date (e.g., end of 2027).
   - Prospective test:
     - Subjects enrolled after the cutoff date (e.g., 2028+).
   - Rationale:
     - Mimics real-world deployment where models trained on early waves are applied to future patients.

2. **Wave-aware cross-validation**
   - Within the training period, use **wave-aware CV** (e.g., group by subject ID) so that:
     - Multiple visits for the same child never appear in both train and validation folds.
   - Target variables:
     - diagnostic status (ASD/ADHD/TD/etc.),
     - cognitive and adaptive trajectories.

3. **Documentation in configs**
   - Prospective split metadata should be referenced from:
     - `kb/datasets/cha_dev_longitudinal.yaml` (manifest fields once defined).
     - `configs/experiments/dev_*.yaml` (explicit `train_period` / `test_period` notes).

## What we can do now (without data)

- Fix the **conceptual split strategy** in this document.
- Ensure all CHA experiment templates:
  - use non-leaky CV (`group_by: subject_id` where applicable),
  - are written assuming a future prospective test set.
- Once the cohort is finalized:
  - add concrete sample sizes and calendar cutoffs to this file,
  - and register a canonical manifest strategy in `ukb_manifest_stub.yaml`-style metadata for CHA.


