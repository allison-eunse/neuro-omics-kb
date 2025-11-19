# GitHub Pages Deployment Guide

## Current Status

✅ All documentation files have been updated with the new structure:
- "Knowledge Base Resources" + "Original Sources" format
- Consistent code walkthrough formatting
- Updated Use Cases section

✅ GitHub Actions workflow created: `.github/workflows/gh-pages.yml`

## To Enable GitHub Pages Deployment

### Step 1: Configure GitHub Pages Source

1. Go to your repository on GitHub: `https://github.com/allison-eunse/neuro-omics-kb`
2. Click **Settings** → **Pages** (in the left sidebar)
3. Under **"Source"**, select: **"GitHub Actions"** (NOT "Deploy from a branch")
4. Click **Save**

### Step 2: Verify Workflow Runs

1. Go to **Actions** tab in your repository
2. You should see "Deploy MkDocs to GitHub Pages" workflow
3. If it hasn't run yet, you can:
   - Wait for the next push to `main` (it will auto-trigger)
   - Or manually trigger it: Actions → "Deploy MkDocs to GitHub Pages" → "Run workflow"

### Step 3: Check Deployment Status

- The workflow will build the site and deploy it to GitHub Pages
- Once complete, your site at `https://allison-eunse.github.io/neuro-omics-kb/` will show all updates
- Deployment usually takes 1-2 minutes

## Troubleshooting

If the site still doesn't update:
1. Check the Actions tab for any workflow errors
2. Verify GitHub Pages is set to "GitHub Actions" (not a branch)
3. Try manually triggering the workflow
4. Clear browser cache and hard refresh (Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows)

