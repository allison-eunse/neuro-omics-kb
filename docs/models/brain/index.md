# 🧠 Brain Foundation Models

> **Neuroimaging foundation models for brain representation learning**

This section documents the **brain imaging foundation models** that extract embeddings from structural MRI (sMRI), functional MRI (fMRI), and other brain imaging modalities for downstream integration with genomic data, behavioral phenotypes, and clinical outcomes.

---

## 📋 Overview

All brain FMs documented here:

- **Operate on neuroimaging data** (volumetric MRI, parcel time series, or raw BOLD signals)
- **Support subject-level embeddings** via aggregation across spatial regions or temporal windows
- **Are pretrained on large multi-site datasets** (UK Biobank, HCP, ABCD, etc.)
- **Enable cross-modal alignment** with genomic and behavioral representations

---

## 🎯 Model Registry

| Model | Modality | Architecture | Key Feature | Documentation |
|-------|----------|-------------|-------------|---------------|
| 🧠 [**BrainLM**](brainlm.md) | fMRI | ViT-MAE | Masked autoencoding; site-robust | [Walkthrough](../../code_walkthroughs/brainlm_walkthrough.md) |
| 🧠 [**Brain-JEPA**](brainjepa.md) | fMRI | JEPA | Joint-embedding prediction; lower-latency | [Walkthrough](../../code_walkthroughs/brainjepa_walkthrough.md) |
| 🧠 [**Brain Harmony**](brainharmony.md) | sMRI + fMRI | ViT + TAPE | Multi-modal fusion via TAPE | [Walkthrough](../../code_walkthroughs/brainharmony_walkthrough.md) |
| 🧠 [**BrainMT**](brainmt.md) | sMRI + fMRI | Mamba-Transformer | Efficient long-range dependencies | [Walkthrough](../../code_walkthroughs/brainmt_walkthrough.md) |
| 🧠 [**SwiFT**](swift.md) | fMRI | Swin Transformer | Hierarchical spatiotemporal modeling | [Walkthrough](../../code_walkthroughs/swift_walkthrough.md) |

---

## 🔄 Usage Workflow

### For fMRI models (BrainLM, Brain-JEPA, SwiFT)

1. **Preprocess** rs-fMRI: parcellation (Schaefer/AAL), bandpass filter, motion scrubbing
2. **Tokenize** parcel time series (or 4D volumes for SwiFT)
3. **Embed** via pretrained encoder
4. **Pool** to subject-level representation (mean over tokens/time)
5. **Project** to 512-D for cross-modal alignment

### For sMRI models (BrainMT, Brain Harmony)

1. **Run** FreeSurfer or FSL FAST for tissue segmentation
2. **Extract** IDPs (cortical thickness, subcortical volumes) or feed raw T1w volumes
3. **Embed** via pretrained encoder
4. **Pool** to subject-level representation
5. **Project** to 512-D for fusion

---

## 🔑 Key Considerations

### Site/scanner harmonization
Multi-site pretraining (e.g., BrainLM on UKB+HCP) improves site robustness, but **residualize scanner/site effects** before fusion:

- Regress site dummy variables from embeddings
- Use ComBat or similar harmonization if needed (see [Integration Strategy](../../integration/integration_strategy.md))

### Motion artifacts
fMRI embeddings are sensitive to head motion. **Quality control:**

- Exclude high-motion frames (FD > 0.5 mm)
- Regress mean FD as confound in downstream prediction
- Report motion distributions stratified by diagnosis (e.g., ADHD vs TD)

### Multimodal fusion
**Brain Harmony** natively fuses sMRI and fMRI via TAPE (Target-Aware Projection Ensemble). For other models, use **late fusion** (concatenate embeddings) or **two-tower contrastive** alignment (see [Design Patterns](../../integration/design_patterns.md)).

---

## 🔗 Integration Targets

Brain embeddings are integrated with:

- **Genetics** embeddings (Caduceus, DNABERT-2) for gene–brain association discovery
- **Behavioral phenotypes** (cognitive scores, psychiatric diagnoses) via multimodal prediction
- **Clinical data** (longitudinal assessments, EHR records) for developmental trajectories

**Learn more:**
- [Integration Strategy](../../integration/integration_strategy.md) - Fusion protocols
- [Modality Features: sMRI](../../integration/modality_features/smri.md) - sMRI preprocessing
- [Modality Features: fMRI](../../integration/modality_features/fmri.md) - fMRI preprocessing

---

## 📦 Source Repositories

<details>
<summary><b>Click to view all source repositories</b></summary>

All brain FM source code lives in `external_repos/`:

| Model | Local Path | GitHub Repository |
|-------|------------|-------------------|
| BrainLM | `external_repos/brainlm/` | [vandijklab/BrainLM](https://github.com/vandijklab/BrainLM) |
| Brain-JEPA | `external_repos/brainjepa/` | [janklees/brainjepa](https://github.com/janklees/brainjepa) |
| Brain Harmony | `external_repos/brainharmony/` | [hzlab/Brain-Harmony](https://github.com/hzlab/Brain-Harmony) |
| BrainMT | `external_repos/brainmt/` | [arunkumar-kannan/brainmt-fmri](https://github.com/arunkumar-kannan/brainmt-fmri) |
| SwiFT | `external_repos/swift/` | [Transconnectome/SwiFT](https://github.com/Transconnectome/SwiFT) |

Each model page includes:
- ✅ Detailed code walkthrough in `docs/code_walkthroughs/`
- ✅ Structured YAML card in `kb/model_cards/`
- ✅ Integration recipes and preprocessing specs

</details>

---

## 🚀 Next Steps

- ✅ Validate brain embedding reproducibility across cohorts (UK Biobank, Cha Hospital developmental cohort)
- ✅ Benchmark fMRI encoder stability across different parcellation schemes (Schaefer 100/200/400, AAL)
- 🔬 Explore **EEG/EPhys** foundation models for pediatric/clinical settings (e.g., LaBraM, TBD)
- 🔬 Integrate **diffusion MRI** embeddings for white matter microstructure (exploratory)
