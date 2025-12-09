---
title: Team User Guide
updated: 2025-12-04
---

# 🧬🧠 Team User Guide

**For:** Lab members working on Brain–Genetics FM integration

!!! tip "Quick Start for New Team Members"
    1. Read this guide (you're here!)
    2. Browse the [Integration Strategy](integration/integration_strategy.md)
    3. Check [experiment configs](https://github.com/allison-eunse/neuro-omics-kb/tree/main/configs/experiments)

---

## 🎯 What This Repo Does

This is your **documentation-first knowledge base** — the map and spec for the Brain–Genetics program.

### Repository Structure

<div style="font-family: monospace; background: #f5f5f5; padding: 16px; border-radius: 8px; line-height: 1.8;">
<code>kb/</code><br>
├── <span class="genetics"><b>model_cards/</b></span> ← 20 FM specs (17 FMs + 3 reference)<br>
├── <span class="multimodal"><b>paper_cards/</b></span> ← 30 research papers with structured takeaways<br>
├── <span class="brain"><b>datasets/</b></span> ← 19 dataset schemas (UKB, HCP, Cha, benchmarks)<br>
└── <span class="fusion"><b>integration_cards/</b></span> ← 6 integration recipes
</div>

### What's Documented

| Category | What It Is | Examples |
|:---------|:-----------|:---------|
| <span class="genetics">**Genetics FMs**</span> | DNA sequence foundation models for gene-level embeddings | Caduceus, DNABERT-2, Evo 2, HyenaDNA, GENERator |
| <span class="brain">**Brain FMs**</span> | Neuroimaging models for fMRI/sMRI subject embeddings | BrainLM, Brain-JEPA, BrainMT, Brain Harmony, SwiFT |
| <span class="multimodal">**Multimodal FMs**</span> | Clinical & unified multimodal architecture references | BAGEL, MoT, M3FM, Me-LLaMA, TITAN, Flamingo, FMS-Medical |
| <span class="multimodal">**Research Papers**</span> | Curated paper summaries with implementation notes | RC-equivariance, Ensemble Integration, MURD, Yoon BioKDD'25 |
| <span class="brain">**Datasets**</span> | Data schema specs and preprocessing protocols | UKB (fMRI, sMRI, WES), HCP, Cha developmental, benchmarks |
| <span class="fusion">**Integration & Strategy**</span> | Embedding recipes, harmonization, fusion playbooks | `genetics_joo_mdd_cog_v1`, `murd_t1_t2`, CCA + permutation |

### The Playbook

**Strategy:** Late fusion → Two-tower contrastive → MoT/unified BOM

| Phase | When | What |
|:------|:-----|:-----|
| <span class="ready">**Stage 1**</span> | Now | Per-modality FMs + 512-D embeddings + late fusion |
| <span class="pending">**Stage 2**</span> | If fusion wins | Two-tower contrastive / EI stacking |
| <span class="future">**Stage 3**</span> | Long-term | MoT/BAGEL unified architectures |

---

## 📋 Canonical Embedding Recipes

!!! info "All recipes defined in `kb/integration_cards/embedding_strategies.yaml`"
    Query any recipe: `python scripts/manage_kb.py ops strategy <recipe_id>`

| Recipe ID | Type | Output | Pipeline |
|:----------|:-----|:------:|:---------|
| `genetics_gene_fm_pca512_v1` | <span class="genetics">genetics</span> | 512-D | Caduceus/DNABERT-2/Evo2 + RC-averaging |
| `genetics_joo_mdd_cog_v1` | <span class="genetics">genetics</span> | 512-D | <span class="strong">Prof. Joo's 38 MDD genes</span> ⭐ |
| `smri_free_surfer_pca512_v1` | <span class="brain">brain</span> | 512-D | FreeSurfer ROIs → residualize → PCA |
| `rsfmri_swift_segments_v1` | <span class="brain">brain</span> | 512-D | SwiFT segments → mean pool → PCA |
| `rsfmri_brainlm_segments_v1` | <span class="brain">brain</span> | 512-D | BrainLM CLS tokens → mean pool |
| `fusion_concat_gene_brain_1024_v1` | <span class="fusion">fusion</span> | 1024-D | Concat(Gene₅₁₂ + Brain₅₁₂) |

⭐ = Recommended starting point

**Query a recipe:**

<div style="font-family: monospace; background: #263238; color: #4fc3f7; padding: 12px 16px; border-radius: 6px; border-left: 4px solid #2e7d32;">
python scripts/manage_kb.py ops strategy <span style="color: #aed581; font-weight: 600;">genetics_joo_mdd_cog_v1</span>
</div>

---

## 🗺️ How to Navigate

### → "I need to understand a specific FM"

!!! example "Example: Understanding Caduceus"
    1. **Overview:** [Caduceus model docs](models/genetics/caduceus.md)
    2. **Step-by-step:** [Caduceus Code Walkthrough](code_walkthroughs/caduceus_walkthrough.md)
    3. **Code:** `external_repos/caduceus/`
    4. **Metadata:** `kb/model_cards/caduceus.yaml`

### → "I want to run CCA / prediction baselines"

1. **Read the playbook:** `docs/integration/integration_strategy.md`
2. **Check the recipe:** `kb/integration_cards/embedding_strategies.yaml`
3. **Use the config:** `configs/experiments/01_cca_gene_smri.yaml` or `02_prediction_baselines.yaml`

### → "How do I preprocess [modality]?"

- **Genetics:** `docs/integration/modality_features/genomics.md`
- **sMRI:** `docs/integration/modality_features/smri.md`
- **fMRI:** `docs/integration/modality_features/fmri.md`

### → "Which harmonization method?"

<div style="font-family: monospace; background: #263238; color: #ce93d8; padding: 12px 16px; border-radius: 6px; border-left: 4px solid #1565c0;">
python scripts/manage_kb.py ops harmonization <span style="color: #aed581; font-weight: 600;">murd_t1_t2</span>
</div>

Or read: `docs/integration/integration_strategy.md` (Harmonization section)

---

## 🚀 Jan-Feb Action Plan

!!! success "Meeting Goals: Jan-Feb Wrap-Up"
    - Test with 20-participant toy sample
    - Use new NVIDIA Spark GPU (128GB)  
    - Offline genetics embeddings (pending)
    - Brain features (fMRI parcellation pending)
    - Complete Stage-1 baselines

### **Week 1-2: Small Sample Testing (20 participants)**

**Goal:** Test pipeline on toy sample using new NVIDIA Spark GPU (128GB)

<div style="font-family: monospace; background: #263238; color: #aed581; padding: 16px; border-radius: 8px; line-height: 1.8; border-left: 4px solid #f57c00;">
<span style="color: #78909c;"># 1. Download 20-participant sample</span><br>
<span style="color: #78909c;">#    - <span style="color: #64b5f6;">Brain features</span> (fMRI parcellation)</span><br>
<span style="color: #78909c;">#    - <span style="color: #4fc3f7;">Genomics embeddings</span> (offline, pre-trained)</span><br>
<br>
<span style="color: #78909c;"># 2. Test embedding extraction</span><br>
python scripts/manage_kb.py ops strategy <span style="color: #4fc3f7; font-weight: 600;">genetics_joo_mdd_cog_v1</span><br>
<br>
<span style="color: #78909c;"># 3. Run on NVIDIA Spark GPU</span><br>
<span style="color: #78909c;"># 4. Verify pipelines work end-to-end</span>
</div>

**What to test:**
- Brain feature download works
- Genomics embeddings load correctly
- CCA runs without errors
- Prediction baselines produce AUROCs

### **Week 3-4: Run Stage-1 Experiments**

**Goal:** Gene ↔ Brain correlation + prediction baselines

**Use these configs:**
1. `configs/experiments/01_cca_gene_smri.yaml`
   - Gene ↔ sMRI CCA + 1,000 permutations
   - Check if ρ₁–ρ₃ are significant (p < 0.05)

2. `configs/experiments/02_prediction_baselines.yaml`
   - Gene-only → MDD
   - Brain-only → MDD  
   - Fusion (Gene+Brain) → MDD
   - DeLong test: Is Fusion > max(Gene, Brain)?

3. Document results in `kb/results/`

### **Week 5-8: Decide on Escalation**

**Decision criteria:**

| Result | Signal | Next Action |
|:-------|:-------|:------------|
| `Fusion > max(Gene, Brain)` p < 0.05 | <span class="strong">Strong</span> | Consider two-tower contrastive |
| `Fusion ≈ best single modality` | <span class="weak">Weak</span> | Focus on improving per-modality models |
| CCA strong (ρ₁ > 0.3, p < 0.001) | <span class="strong">Strong</span> | Supports two-tower alignment |
| CCA weak (ρ₁ < 0.2 or p > 0.05) | <span class="none">None</span> | Keep late fusion, check preprocessing |

**Templates available:**
- Two-tower patterns: `docs/integration/design_patterns.md`
- MoT/BAGEL patterns: `docs/integration/multimodal_architectures.md`

---

## What You Can Do Now (Before Data)

### ✅ Available Now

1. **Read model code walkthroughs** — Understand how each FM works
2. **Study embedding recipes** — Know what preprocessing to apply
3. **Review experiment configs** — Understand analysis pipeline
4. **Validate YAML cards** — `python scripts/manage_kb.py validate models`
5. **Clone external repos** — Familiarize with FM codebases

### 🟡 Waiting For

- **UKB data access approval** (fMRI/sMRI features)
- **Genetics embeddings** (offline pre-trained)
- **Cha Hospital developmental cohort** (future)

### 📚 Onboarding New Team Members

**Recommended reading order:**
1. This guide (TEAM_GUIDE.md)
2. `README.md` — High-level overview
3. `docs/integration/integration_strategy.md` — THE PLAYBOOK
4. `configs/experiments/01_cca_gene_smri.yaml` — See what we're running
5. Pick one FM code walkthrough to read in detail

---

## 🔬 Stage-1 Experiments

!!! abstract "Experiment 1: CCA (Gene ↔ Brain Association)"
**Config:** `configs/experiments/01_cca_gene_smri.yaml`

**What it does:**
    
- Tests if gene embeddings share structure with brain embeddings
- 1,000 permutations to assess significance
- Reports ρ₁–ρ₃ (canonical correlations) with p-values

**Success criteria:**
    
- ρ₁ > 0.2 with p < 0.05 → significant association
- Gene/ROI loadings interpretable

!!! abstract "Experiment 2: Prediction (Gene vs Brain vs Fusion)"
**Config:** `configs/experiments/02_prediction_baselines.yaml`

**What it does:**
    
- Compares 3 baselines for MDD prediction:
  - Gene-only (512-D)
  - Brain-only (512-D)
  - Fusion (1024-D concatenation)
- Uses LR + LightGBM + CatBoost
- DeLong test to compare AUROCs

**Success criteria:**
    
- If Fusion > max(Gene, Brain) p < 0.05 → integration adds value
- Document which modality is stronger

!!! abstract "Experiment 3: LOGO Attribution"
**Config:** `configs/experiments/03_logo_gene_attribution.yaml`

**What it does:**
    
- Leave-one-gene-out ΔAUC
- Identifies which genes contribute most to prediction
- Wilcoxon test + FDR correction

**Success criteria:**
    
- Find significant genes (p < 0.05 FDR-corrected)
- Compare with literature (SOD2, HOXA10, etc.)

---

## Escalation Decision Tree

<div style="font-family: monospace; background: #f5f5f5; padding: 20px; border-radius: 8px; line-height: 1.8; border-left: 4px solid #f57c00;">
<span style="color: #f57c00; font-weight: 700;">Start:</span> Run Stage-1 (CCA + Prediction + LOGO)<br>
&nbsp;&nbsp;│<br>
&nbsp;&nbsp;├─ <span style="color: #f57c00;">Fusion > single-modality (p < 0.05)?</span><br>
&nbsp;&nbsp;│&nbsp;&nbsp;│<br>
&nbsp;&nbsp;│&nbsp;&nbsp;├─ <span style="color: #2e7d32; font-weight: 600;">YES</span> → CCA also significant?<br>
&nbsp;&nbsp;│&nbsp;&nbsp;│&nbsp;&nbsp;│<br>
&nbsp;&nbsp;│&nbsp;&nbsp;│&nbsp;&nbsp;├─ <span style="color: #2e7d32; font-weight: 600;">YES</span> → <span style="color: #1565c0;">Consider two-tower contrastive</span><br>
&nbsp;&nbsp;│&nbsp;&nbsp;│&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(frozen FMs + small projectors)<br>
&nbsp;&nbsp;│&nbsp;&nbsp;│&nbsp;&nbsp;│<br>
&nbsp;&nbsp;│&nbsp;&nbsp;│&nbsp;&nbsp;└─ <span style="color: #c62828; font-weight: 600;">NO</span> → Keep late fusion, improve single-modality<br>
&nbsp;&nbsp;│&nbsp;&nbsp;│<br>
&nbsp;&nbsp;│&nbsp;&nbsp;└─ <span style="color: #c62828; font-weight: 600;">NO</span> → <span style="color: #2e7d32;">Focus on better per-modality embeddings</span><br>
&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Try harmonization (ComBat, MURD)
</div>

---

## 📊 Data Status

!!! warning "Note: Data Documentation vs Availability"
    This KB documents **how to use data**, not **when data is ready**.  
    Actual data availability is project-specific and tracked elsewhere.

| Dataset | Docs | Status | Access | Notes |
|:--------|:----:|:-------|:-------|:------|
| <span class="genetics">hg38 reference</span> | ✓ | <span class="ready">Ready</span> | Public | Reference genome |
| <span class="genetics">Genomic benchmarks</span> | ✓ | <span class="ready">Ready</span> | Public | Standard benchmarks |
| <span class="brain">UKB fMRI/sMRI</span> | ✓ | <span class="pending">Pending</span> | Restricted | Features can be downloaded |
| <span class="genetics">Genetics embeddings</span> | ✓ | <span class="pending">Pending</span> | Internal | Offline pre-trained embeddings |
| <span class="brain">Cha Hospital dev</span> | ✓ | <span class="future">Future</span> | Restricted | Developmental research |

---

## Utilities

<div style="font-family: monospace; background: #263238; color: #aed581; padding: 16px; border-radius: 8px; line-height: 1.8; border-left: 4px solid #f57c00;">
<span style="color: #78909c;"># Validate all YAML cards</span><br>
python scripts/manage_kb.py <span style="color: #64b5f6;">validate models</span><br>
python scripts/manage_kb.py <span style="color: #64b5f6;">validate datasets</span><br>
<br>
<span style="color: #78909c;"># Query embedding recipe</span><br>
python scripts/manage_kb.py ops strategy <span style="color: #4fc3f7;">genetics_joo_mdd_cog_v1</span><br>
<br>
<span style="color: #78909c;"># Query harmonization method</span><br>
python scripts/manage_kb.py ops harmonization <span style="color: #ce93d8;">combat_smri</span><br>
<br>
<span style="color: #78909c;"># View docs locally</span><br>
mkdocs serve <span style="color: #78909c;"># Visit http://localhost:8000</span><br>
<br>
<span style="color: #78909c;"># Online docs</span><br>
<span style="color: #64b5f6;">https://allison-eunse.github.io/neuro-omics-kb/</span>
</div>

---

## ❓ FAQ

!!! question "Which genetics FM should I use?"
    **Answer:** Start with the recommended pipeline (`genetics_joo_mdd_cog_v1`):
    
    - 38 MDD genes from Yoon et al.
    - RC-averaged embeddings
    - Pre-validated gene set
    
    Then compare with other FMs if needed (Caduceus, DNABERT-2, Evo2)

!!! question "Should I use sMRI or fMRI features?"
    **Answer:** Both are documented:
    
    - **sMRI:** FreeSurfer ROIs (~176 features) → Good for structural analysis
    - **fMRI:** Parcellation data → Follow fMRI-gene analysis recipes in integration docs
    
    Start with whichever is available first.

!!! question "Do I need to build a new FM?"
    **No!** Stage-1 uses:
    
    - **Existing genetics FMs** (pre-trained embeddings)
    - **Existing brain FMs** (SwiFT, BrainLM, etc.)
    - **Late fusion** = just concatenate embeddings
    
    Only escalate to two-tower/unified FM if Stage-1 shows clear fusion benefit.

!!! question "What about Cha Hospital / developmental data?"
    **Future work.** The KB has:

- Dataset card template: `kb/datasets/cha_dev_longitudinal.yaml`
- Embedding recipes: `cha_dev_smri_pca64_v1`, `cha_dev_eeg_fm_v1`, `cha_dev_behaviour_latent_v1`
- Experiment templates: `configs/experiments/dev_01_brain_only_baseline.yaml`

    **Focus on UKB first** (Jan-Feb wrap-up), then extend to developmental.

---

## Key Principle

**This KB answers:**
- ✅ "How do I extract embeddings?"
- ✅ "Which FM should I use?"
- ✅ "How do I run CCA?"
- ✅ "When should I escalate to two-tower?"

---

## Questions?

- **Model choice:** Check `docs/models/<category>/index.md`
- **Integration strategy:** Read `docs/integration/integration_strategy.md`
- **Embedding recipes:** Query `python scripts/manage_kb.py ops strategy <id>`
- **Everything else:** Ask Allison or check online docs

---

**Bottom Line:** This repo is your **map + spec**. Run Stage-1 experiments (CCA + prediction baselines) end-to-end, then decide on escalation based on results.

**Jan-Feb Goal:** Complete Stage-1 with offline genetics embeddings + brain features → document results → decide next steps.

