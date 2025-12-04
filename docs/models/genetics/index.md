# 🧬 Genetics Foundation Models

> **DNA sequence foundation models for genomic representation learning**

This section documents the **genetics foundation models** used to extract gene-level embeddings from raw genomic sequences (DNA/RNA) for downstream integration with brain imaging, behavioral phenotypes, and clinical outcomes.

---

## 📋 Overview

All genetics FMs documented here:

- **Operate on nucleotide sequences** (A, C, G, T) rather than pre-computed variant calls or SNP arrays
- **Support gene-level embeddings** via forward/reverse-complement (RC) averaging and pooling strategies
- **Enable interpretability** through attribution methods like LOGO ΔAUC
- **Are pretrained on large genomic corpora** (human reference genomes, multi-species datasets, or RefSeq)

---

## 🎯 Model Registry

| Model | Architecture | Key Feature | Integration Role | Documentation |
|:------|:-------------|:------------|:-----------------|:--------------|
| <span class="genetics">**[Caduceus](caduceus.md)**</span> | Mamba (BiMamba) + RC-equivariance | Strand-robust, efficient long-context | Primary gene encoder for UK Biobank WES | [Code Walkthrough](../../code_walkthroughs/caduceus_walkthrough.md) |
| <span class="genetics">**[DNABERT-2](dnabert2.md)**</span> | BERT (multi-species) | BPE tokenization, cross-species transfer | Alternative gene encoder; comparison baseline | [Code Walkthrough](../../code_walkthroughs/dnabert2_walkthrough.md) |
| <span class="genetics">**[Evo 2](evo2.md)**</span> | StripedHyena (1M context) | Ultra-long-range dependencies | Exploratory; regulatory region capture | [Code Walkthrough](../../code_walkthroughs/evo2_walkthrough.md) |
| <span class="genetics">**[GENERator](generator.md)**</span> | Generative 6-mer LM | Generative modeling, sequence design | Reference for generative vs discriminative | [Code Walkthrough](../../code_walkthroughs/generator_walkthrough.md) |
| <span class="genetics">**[HyenaDNA](hyenadna.md)**</span> | Hyena implicit convolutions (1M context) | Single-nucleotide, ultra-long genomic modeling | Conceptual long-context genomics reference | [Code Walkthrough](../../code_walkthroughs/hyena_walkthrough.md) |

---

## 🔄 Usage Workflow

<div style="font-family: monospace; background: #263238; color: #aed581; padding: 16px; border-radius: 8px; line-height: 1.8; overflow-x: auto;">
<span style="color: #78909c;"># 1.</span> <span style="color: #4fc3f7;">Extract gene sequences</span> from hg38 reference (GENCODE annotations)<br>
<span style="color: #78909c;"># 2.</span> <span style="color: #4fc3f7;">Tokenize</span> with model-specific vocabulary (6-mer, BPE, or single-nucleotide)<br>
<span style="color: #78909c;"># 3.</span> <span style="color: #4fc3f7;">Load pretrained checkpoint</span> (Caduceus, DNABERT-2, Evo2, etc.)<br>
<span style="color: #78909c;"># 4.</span> <span style="color: #4fc3f7;">Forward pass</span> → per-position embeddings<br>
<span style="color: #78909c;"># 5.</span> <span style="color: #4fc3f7;">Verify RC equivariance</span> (optional but recommended):<br>
<span style="color: #78909c;">#    </span> embed(seq) ≈ embed(reverse_complement(seq))<br>
<span style="color: #78909c;"># 6.</span> <span style="color: #4fc3f7;">Mean pool</span> over gene → gene-level vector<br>
<span style="color: #78909c;"># 7.</span> <span style="color: #4fc3f7;">Concatenate gene set</span> → subject genotype embedding<br>
<span style="color: #78909c;"># 8.</span> <span style="color: #f9a825;">Log:</span> gene_list, reference_version, embedding_strategy_id
</div>

**Detailed steps:**

1. **Extract sequences** from reference genome (hg38) for target genes
2. **Tokenize** using model-specific vocabularies (k-mers, BPE, or single-nucleotide)
3. **Embed** forward and reverse-complement sequences
4. **Pool** to gene-level representation (mean/CLS depending on model)
5. **Project** to 512-D for cross-modal alignment with brain embeddings

---

## 🔑 Key Considerations

### RC-equivariance
DNA has no inherent directionality; models like **Caduceus** enforce BiMamba RC-equivariance to avoid strand bias. For non-equivariant models, manually average forward and RC embeddings.

### Variant handling
Foundation models operate on **reference sequences by default**. To incorporate subject-specific variants:

- Patch reference with VCF alleles
- Re-embed variant sequences
- Compare ΔAUC between reference and variant embeddings (exploratory)

### Attribution
Use **LOGO (Leave-One-Gene-Out)** ΔAUC to assess which genes contribute most to downstream prediction tasks (e.g., MDD risk, cognitive scores). See [Yoon et al. BioKDD 2025](https://raw.githubusercontent.com/allison-eunse/neuro-omics-kb/main/docs/generated/kb_curated/papers-pdf/yoon_biokdd2025.pdf) for protocol details.

---

## 🔗 Integration Targets

Genetics embeddings are integrated with:

- **sMRI** IDPs (structural phenotypes) via CCA, late fusion, or contrastive alignment
- **fMRI** embeddings (e.g., BrainLM, Brain-JEPA) for gene–brain–behaviour triangulation
- **Behavioral phenotypes** (cognitive scores, psychiatric diagnoses) via multimodal prediction

**Learn more:**
- [Integration Strategy](../../integration/integration_strategy.md) - Fusion protocols
- [Modality Features: Genomics](../../integration/modality_features/genomics.md) - Preprocessing specs

---

## 📦 Source Repositories

<details>
<summary><b>Click to view all source repositories</b></summary>

**All genetics FM source code is tracked in** `external_repos/`:

| Model | GitHub Repository | Local Clone |
|:------|:------------------|:------------|
| <span class="genetics">**Caduceus**</span> | [kuleshov-group/caduceus](https://github.com/kuleshov-group/caduceus) | `external_repos/caduceus/` |
| <span class="genetics">**DNABERT-2**</span> | [Zhihan1996/DNABERT2](https://github.com/Zhihan1996/DNABERT2) | `external_repos/dnabert2/` |
| <span class="genetics">**Evo 2**</span> | [ArcInstitute/evo2](https://github.com/ArcInstitute/evo2) | `external_repos/evo2/` |
| <span class="genetics">**GENERator**</span> | [GenerTeam/GENERator](https://github.com/GenerTeam/GENERator) | `external_repos/generator/` |
| <span class="genetics">**HyenaDNA**</span> | [HazyResearch/hyena-dna](https://github.com/HazyResearch/hyena-dna) | `external_repos/hyena/` |

**Each model has three interconnected resources:**

- <span class="multimodal">**Code Walkthrough**</span> → Step-by-step implementation guide
- <span class="genetics">**YAML Model Card**</span> → Structured metadata and specs
- <span class="fusion">**Integration Recipe**</span> → Embedding extraction and fusion protocols

</details>

---

## 🚀 Next Steps

- ✅ Validate gene embedding reproducibility across cohorts (UK Biobank WES, Cha Hospital panel sequencing)
- ✅ Benchmark LOGO ΔAUC stability under different embedding projection dimensions (256, 512, 1024)
- 🔬 Explore regulatory region embeddings (enhancers, promoters) with long-context models like Evo 2
