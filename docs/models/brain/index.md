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
|:------|:---------|:-------------|:------------|:--------------|
| <span class="brain">**[BrainLM](brainlm.md)**</span> | fMRI | ViT-MAE | Masked autoencoding; site-robust | [Code Walkthrough](../../code_walkthroughs/brainlm_walkthrough.md) |
| <span class="brain">**[Brain-JEPA](brainjepa.md)**</span> | fMRI | JEPA | Joint-embedding prediction; lower-latency | [Code Walkthrough](../../code_walkthroughs/brainjepa_walkthrough.md) |
| <span class="brain">**[Brain Harmony](brainharmony.md)**</span> | sMRI + fMRI | ViT + TAPE | Multi-modal fusion via TAPE | [Code Walkthrough](../../code_walkthroughs/brainharmony_walkthrough.md) |
| <span class="brain">**[BrainMT](brainmt.md)**</span> | sMRI + fMRI | Mamba-Transformer | Efficient long-range dependencies | [Code Walkthrough](../../code_walkthroughs/brainmt_walkthrough.md) |
| <span class="brain">**[SwiFT](swift.md)**</span> | fMRI | Swin Transformer | Hierarchical spatiotemporal modeling | [Code Walkthrough](../../code_walkthroughs/swift_walkthrough.md) |

---

## 🔄 Usage Workflow

### For fMRI models (BrainLM, Brain-JEPA, SwiFT)

<div style="font-family: monospace; background: #263238; color: #64b5f6; padding: 16px; border-radius: 8px; line-height: 1.8; overflow-x: auto;">
<span style="color: #78909c;"># 1.</span> <span style="color: #64b5f6;">Preprocess rs-fMRI:</span> parcellation (Schaefer/AAL), bandpass filter, motion scrubbing<br>
<span style="color: #78909c;"># 2.</span> <span style="color: #64b5f6;">Tokenize</span> parcel time series (or 4D volumes for SwiFT)<br>
<span style="color: #78909c;"># 3.</span> <span style="color: #64b5f6;">Load checkpoint</span> (BrainLM, Brain-JEPA, SwiFT)<br>
<span style="color: #78909c;"># 4.</span> <span style="color: #64b5f6;">Forward pass</span> → per-token embeddings<br>
<span style="color: #78909c;"># 5.</span> <span style="color: #64b5f6;">Pool</span> to subject-level (mean over tokens/time)<br>
<span style="color: #78909c;"># 6.</span> <span style="color: #64b5f6;">Project</span> to 512-D for cross-modal alignment<br>
<span style="color: #78909c;"># 7.</span> <span style="color: #f9a825;">Log:</span> parcellation_scheme, motion_exclusion_threshold, embedding_strategy_id
</div>

### For sMRI models (BrainMT, Brain Harmony)

<div style="font-family: monospace; background: #263238; color: #64b5f6; padding: 16px; border-radius: 8px; line-height: 1.8; overflow-x: auto;">
<span style="color: #78909c;"># 1.</span> <span style="color: #64b5f6;">Run FreeSurfer</span> or FSL FAST for tissue segmentation<br>
<span style="color: #78909c;"># 2.</span> <span style="color: #64b5f6;">Extract IDPs</span> (cortical thickness, subcortical volumes) or feed raw T1w<br>
<span style="color: #78909c;"># 3.</span> <span style="color: #64b5f6;">Residualize confounds</span> (age, sex, site, ICV)<br>
<span style="color: #78909c;"># 4.</span> <span style="color: #64b5f6;">Embed</span> via pretrained encoder<br>
<span style="color: #78909c;"># 5.</span> <span style="color: #64b5f6;">Pool</span> to subject-level representation<br>
<span style="color: #78909c;"># 6.</span> <span style="color: #64b5f6;">Project</span> to 512-D for fusion<br>
<span style="color: #78909c;"># 7.</span> <span style="color: #f9a825;">Log:</span> freesurfer_version, harmonization_method, embedding_strategy_id
</div>

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

**All brain FM source code is tracked in** `external_repos/`:

| Model | GitHub Repository | Local Clone |
|:------|:------------------|:------------|
| <span class="brain">**BrainLM**</span> | [vandijklab/BrainLM](https://github.com/vandijklab/BrainLM) | `external_repos/brainlm/` |
| <span class="brain">**Brain-JEPA**</span> | [janklees/brainjepa](https://github.com/janklees/brainjepa) | `external_repos/brainjepa/` |
| <span class="brain">**Brain Harmony**</span> | [hzlab/Brain-Harmony](https://github.com/hzlab/Brain-Harmony) | `external_repos/brainharmony/` |
| <span class="brain">**BrainMT**</span> | [arunkumar-kannan/brainmt-fmri](https://github.com/arunkumar-kannan/brainmt-fmri) | `external_repos/brainmt/` |
| <span class="brain">**SwiFT**</span> | [Transconnectome/SwiFT](https://github.com/Transconnectome/SwiFT) | `external_repos/swift/` |

**Each model has three interconnected resources:**

- <span class="multimodal">**Code Walkthrough**</span> → Step-by-step implementation guide
- <span class="brain">**YAML Model Card**</span> → Structured metadata and specs
- <span class="fusion">**Integration Recipe**</span> → Embedding extraction and fusion protocols

</details>

---

## 🚀 Next Steps

- ✅ Validate brain embedding reproducibility across cohorts (UK Biobank, Cha Hospital developmental cohort)
- ✅ Benchmark fMRI encoder stability across different parcellation schemes (Schaefer 100/200/400, AAL)
- 🔬 Explore **EEG/EPhys** foundation models for pediatric/clinical settings (e.g., LaBraM, TBD)
- 🔬 Integrate **diffusion MRI** embeddings for white matter microstructure (exploratory)
