#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="$ROOT/external_repos"

mkdir -p "$TARGET_DIR"

create_placeholder() {
  local name="$1"
  local url="$2"
  local dest="$TARGET_DIR/$name"

  echo "[placeholder] $name → $url"
  rm -rf "$dest"
  mkdir -p "$dest"
  cat > "$dest/README.upstream.md" <<EOF
# External Repository Placeholder: $name

This directory intentionally avoids vendoring the upstream project.

- **Upstream URL:** $url
- **Fetch command:** \`git clone $url\`

Run \`./scripts/fetch_external_repos.sh\` after removing this directory if you need a fresh clone locally.
EOF
}

while read -r name url; do
  [ -z "$name" ] && continue
  create_placeholder "$name" "$url"
  echo
done <<'REPOS'
brainlm https://github.com/vandijklab/BrainLM.git
brainmt https://github.com/arunkumar-kannan/brainmt-fmri.git
caduceus https://github.com/kuleshov-group/caduceus.git
dnabert2 https://github.com/Zhihan1996/DNABERT2.git
evo2 https://github.com/ArcInstitute/evo2.git
generator https://github.com/GenerTeam/GENERator.git
swift https://github.com/Transconnectome/SwiFT.git
brainjepa https://github.com/janklees/brainjepa.git
brainharmony https://github.com/hzlab/Brain-Harmony.git
titan https://github.com/mahmoodlab/TITAN.git
me-lamma https://github.com/BIDS-Xu-Lab/Me-LLaMA.git
M3FM https://github.com/ai-in-health/M3FM.git
fms-medical https://github.com/YutingHe-list/Awesome-Foundation-Models-for-Advancing-Healthcare.git
REPOS

echo "All external repositories fetched in $TARGET_DIR"
