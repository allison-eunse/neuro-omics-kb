# Integration design patterns

> Late fusion via separate gene/brain heads **remains the default strategy** (see `integration_strategy.md`). The patterns below are cataloged for future escalation paths, with risks noted.

## Early fusion
- Merge genetics + brain embeddings before the task head (concatenate or stack)
- Risk: modality imbalance, covariate leakage, and overfitting when sample size is low

## Shared latent space
- Project modalities into a common latent prior to prediction (e.g., contrastive or CCA-inspired projections)
- Risk: harder interpretability and additional tuning burden

## Cross-modal transformer
- Alternating attention layers across modalities or hub-token fusion
- Risk: high compute/VRAM and more stringent preprocessing alignment

## Staged pretraining
- Pretrain per modality, freeze, then fine-tune joint layers
- Risk: stale frozen encoders if upstream distribution drifts

Documenting these options lets us reference them quickly once the late-fusion baseline shows significant gains and escalation is justified.






