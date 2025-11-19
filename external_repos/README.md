# External Research Repositories

This knowledge base intentionally **does not vendor third-party model code**. Instead, please fetch the original repositories on demand so our git history stays lightweight and avoids licensing ambiguity.

## How to fetch everything

```bash
./scripts/fetch_external_repos.sh
```

The script clones (or fast-forwards) each repo into `external_repos/<name>` without disturbing any local modifications. Remove a directory first if you need to reclone from scratch.

## Repository map

| Directory | Upstream project |
| --- | --- |
| `brainlm` | https://github.com/vandijklab/BrainLM |
| `brainmt` | https://github.com/arunkumar-kannan/brainmt-fmri |
| `brainjepa` | https://github.com/janklees/brainjepa |
| `brainharmony` | https://github.com/hzlab/Brain-Harmony |
| `caduceus` | https://github.com/kuleshov-group/caduceus |
| `dnabert2` | https://github.com/Zhihan1996/DNABERT2 |
| `evo2` | https://github.com/ArcInstitute/evo2 |
| `generator` | https://github.com/GenerTeam/GENERator |
| `swift` | https://github.com/Transconnectome/SwiFT |
| `titan` | https://github.com/mahmoodlab/TITAN |
| `me-lamma` | https://github.com/BIDS-Xu-Lab/Me-LLaMA |
| `M3FM` | https://github.com/ai-in-health/M3FM |
| `fms-medical` | https://github.com/YutingHe-list/Awesome-Foundation-Models-for-Advancing-Healthcare |

Feel free to edit `scripts/fetch_external_repos.sh` if you need to add another upstream.
