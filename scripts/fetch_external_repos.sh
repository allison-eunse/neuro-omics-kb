#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="$ROOT/external_repos"

mkdir -p "$TARGET_DIR"

clone_or_update() {
  local name="$1"
  local url="$2"
  local dest="$TARGET_DIR/$name"
  if [ -d "$dest/.git" ]; then
    echo "[update] $name"
    git -C "$dest" fetch --prune --tags
    git -C "$dest" pull --ff-only
  elif [ -d "$dest" ]; then
    echo "[skip] $name exists but is not a git repo; remove it to allow cloning"
  else
    echo "[clone] $name"
    git clone --depth=1 "$url" "$dest"
  fi
}

while read -r name url; do
  [ -z "$name" ] && continue
  clone_or_update "$name" "$url"
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
REPOS

echo "All external repositories fetched in $TARGET_DIR"
