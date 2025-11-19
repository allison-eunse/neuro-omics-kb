Integration cards capture multimodal pipelines:

```
id: unique_slug
name: Title
summary: 2–3 sentences
models:
  - model_id
  - ...
datasets:
  - dataset_id
pipelines:
  - bulleted free text describing scripts/configs
status: idea|designing|running
outputs:
  - path: relative/path
    description: artifact description
ci_checks:
  - optional list of preflight commands
verified: false
last_updated: YYYY-MM-DD
```

## Specialized card types

- **Embedding strategies** (`embedding_strategies.yaml`): Declare `strategies.<id>` entries with hierarchy (segment/run/subject), preprocessing, projector, harmonization hooks, intended use, and `sources` linking to walkthroughs or code.
- **Harmonization methods** (`harmonization_methods.yaml`): Declare `methods.<id>` entries describing whether the approach is statistical (e.g., ComBat) or deep (e.g., MURD), which modalities it touches, and how the project intends to evaluate it.
- **Preprocessing pipelines** (`rsfmri_preprocessing_pipelines.yaml`): Provide named stacks (e.g., `hcp_like_minimal`) so experiment configs can reference a consistent motion/distortion correction recipe.

Experiment configs should now reference these registries via IDs (`embedding_strategies.smri_free_surfer_pca512_v1`, `harmonization_methods.murd_t1_t2`) to keep subject-level embeddings and site handling reproducible.
