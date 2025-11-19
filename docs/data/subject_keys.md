---
title: Subject key schemas
status: draft
updated: 2025-11-19
---

## Overview

This page documents how subject IDs are handled across cohorts (UKB, GARD, CHA, etc.), and clarifies that
**raw identifiers and mapping tables never live in this repository**. Only schemas and conventions are stored here.

### UK Biobank (UKB)

- **Primary ID**: `eid`
  - Used as the join key across:
    - genetics/WES tables (`ukb_wes.yaml`)
    - sMRI features (`ukb_smri_freesurfer.yaml`)
    - fMRI tensors (`ukb_fmri_tensor.yaml`)
    - manifest (`ukb_manifest_stub.yaml`)
- **Derived IDs**:
  - Analysis repos may define hashed IDs (e.g., `ukb_hash_id = SHA256(eid + salt)`), but the mapping from `eid` to
    hash must remain in secure infrastructure, not in this KB.

### CHA developmental cohort

- **Primary ID**: `subject_id` (local, non-PHI)
  - See `cha_dev_longitudinal.yaml` → `keys_and_linkage.subject_id_schema`.
  - Raw hospital IDs (`cha_ehr_id`) are stored only in secure mapping tables.
- **Time axis**:
  - Represented as `months_from_birth` (or equivalent) in analysis code; DOB remains PHI and is not stored here.

### Cross-cohort links (conceptual only)

- **GARD / CRIS / other cohorts**:
  - If future projects link UKB, GARD, CHA, etc., the actual link tables must remain in a governed environment.
  - This KB can store:
    - field names (e.g., `gard_id`, `cha_id`),
    - high-level descriptions of linkage methods (e.g., trusted third-party linkage),
    - but never the mapping content itself.

### Policy

- Subject identifiers in this repo must be:
  - **non-PHI** (no direct MRNs, names, or obvious re-identifiers),
  - **schema-level only** (field names and usage, not values),
  - and, where hashing is used, only the **hash schema** is documented, not salts or mapping tables.
- All actual mapping tables live in:
  - secure institutional storage (e.g., hospital servers, controlled lab disks),
  - under DRB/IRB-approved data governance,
  - and are referenced in this KB only by description.


