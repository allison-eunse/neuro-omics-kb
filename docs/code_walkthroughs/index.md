# Code Walkthrough Hub

Each walkthrough now surfaces the KB scaffolding you need to turn narrative notes into living cards and experiment configs.

## 🔗 Quick Links

- [Integration baseline plan](../decisions/2025-11-integration-plan.md)
- [Integration strategy](../integration/integration_strategy.md)
- [Modality features — Genomics](../integration/modality_features/genomics.md)
- [Modality features — sMRI](../integration/modality_features/smri.md)
- [Modality features — fMRI](../integration/modality_features/fmri.md)
- KB templates (model/integration/method/dataset): `kb/templates/`
- Experiment config stub: `kb/templates/experiment_config_stub.md`

## 📚 Walkthrough Roster

### 🧠 Brain Foundation Models

| Model | Code Walkthrough | Model Card | Modality Spec |
|:------|:-----------------|:-----------|:--------------|
| <span class="brain">**BrainLM**</span> | [Code Walkthrough](brainlm_walkthrough.md) | [Model Card](../models/brain/brainlm.md) | [fMRI features](../integration/modality_features/fmri.md) |
| <span class="brain">**Brain-JEPA**</span> | [Code Walkthrough](brainjepa_walkthrough.md) | [Model Card](../models/brain/brainjepa.md) | [fMRI features](../integration/modality_features/fmri.md) |
| <span class="brain">**Brain Harmony**</span> | [Code Walkthrough](brainharmony_walkthrough.md) | [Model Card](../models/brain/brainharmony.md) | [fMRI](../integration/modality_features/fmri.md) + [sMRI](../integration/modality_features/smri.md) |
| <span class="brain">**BrainMT**</span> | [Code Walkthrough](brainmt_walkthrough.md) | [Model Card](../models/brain/brainmt.md) | [fMRI features](../integration/modality_features/fmri.md) |
| <span class="brain">**SwiFT**</span> | [Code Walkthrough](swift_walkthrough.md) | [Model Card](../models/brain/swift.md) | [fMRI features](../integration/modality_features/fmri.md) |

### 🧬 Genetics Foundation Models

| Model | Code Walkthrough | Model Card | Modality Spec |
|:------|:-----------------|:-----------|:--------------|
| <span class="genetics">**Caduceus**</span> | [Code Walkthrough](caduceus_walkthrough.md) | [Model Card](../models/genetics/caduceus.md) | [Genomics features](../integration/modality_features/genomics.md) |
| <span class="genetics">**DNABERT-2**</span> | [Code Walkthrough](dnabert2_walkthrough.md) | [Model Card](../models/genetics/dnabert2.md) | [Genomics features](../integration/modality_features/genomics.md) |
| <span class="genetics">**Evo 2**</span> | [Code Walkthrough](evo2_walkthrough.md) | [Model Card](../models/genetics/evo2.md) | [Genomics features](../integration/modality_features/genomics.md) |
| <span class="genetics">**GENERator**</span> | [Code Walkthrough](generator_walkthrough.md) | [Model Card](../models/genetics/generator.md) | [Genomics features](../integration/modality_features/genomics.md) |

### 🏥 Multimodal & Clinical Models

| Model | Code Walkthrough | Model Card | Architecture Reference |
|:------|:-----------------|:-----------|:----------------------|
| <span class="multimodal">**BAGEL**</span> | [Code Walkthrough](bagel_walkthrough.md) | [Model Card](../models/multimodal/bagel.md) | [Multimodal architectures](../integration/multimodal_architectures.md) |
| <span class="multimodal">**Flamingo**</span> | [Code Walkthrough](flamingo_walkthrough.md) | [Model Card](../models/multimodal/flamingo.md) | [Design patterns](../integration/design_patterns.md) |
| <span class="multimodal">**MoT**</span> | [Code Walkthrough](mot_walkthrough.md) | [Model Card](../models/multimodal/mot.md) | [Multimodal architectures](../integration/multimodal_architectures.md) |
| <span class="multimodal">**M3FM**</span> | [Code Walkthrough](m3fm_walkthrough.md) | [Model Card](../models/multimodal/m3fm.md) | [Design patterns](../integration/design_patterns.md) |
| <span class="multimodal">**Me-LLaMA**</span> | [Code Walkthrough](melamma_walkthrough.md) | [Model Card](../models/multimodal/me_llama.md) | [Multimodal architectures](../integration/multimodal_architectures.md) |
| <span class="multimodal">**TITAN**</span> | [Code Walkthrough](titan_walkthrough.md) | [Model Card](../models/multimodal/titan.md) | [Design patterns](../integration/design_patterns.md) |
| <span class="reference">**FMS-Medical**</span> | [Code Walkthrough](fms_medical_walkthrough.md) | [Model Card](../models/multimodal/fms_medical.md) | [Reference catalog](../models/multimodal/fms_medical.md) |

### 🏗️ Architecture References

| Architecture | Code Walkthrough | Model Card | Reference Purpose |
|:-------------|:-----------------|:-----------|:------------------|
| <span class="genetics">**HyenaDNA / StripedHyena**</span> | [Code Walkthrough](hyena_walkthrough.md) | [HyenaDNA card](../models/genetics/hyenadna.md) | Long-context genomic modeling (1M tokens), architectural reference for Evo2-style systems |
