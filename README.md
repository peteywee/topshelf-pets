# Topshelf Pets — Starter v3

A zero-build static affiliate site focused on new dog/cat owners (0–6 months). Ready for **Cloudflare Pages** or **Workers (assets)**.

## Quick start (Pages CLI)
```bash
# from repo root (this folder contains `site/`)
npx wrangler pages project create topshelf-pets --production-branch main || true
npx wrangler pages deploy ./site --project-name topshelf-pets
npx wrangler pages domains add topshelf-pets topshelf.it.com   # optional custom domain
```

## Quick start (Workers + static assets)
```bash
# Deploy to *.workers.dev or custom domain (requires Cloudflare-managed DNS)
npx wrangler deploy
```

- Build command: **leave blank**
- Build output directory: **site**
- `/go/*` is marked noindex via `_headers` and per-page meta.
- See `docs/DEPLOYMENT.md` for details.
