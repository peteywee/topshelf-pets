# Deployment

## Cloudflare Pages (no build step)
- **Build command:** (leave blank)
- **Build output directory:** `site`

CLI:
```bash
npx wrangler pages project create topshelf-pets --production-branch main || true
npx wrangler pages deploy ./site --project-name topshelf-pets
npx wrangler pages domains add topshelf-pets topshelf.it.com
```

## Workers (static assets)
Create `wrangler.toml` (already included):

```toml
name = "topshelf-pets-v3"
compatibility_date = "2025-08-13"
assets = { directory = "./site" }
routes = [ { pattern = "topshelf.it.com", custom_domain = true } ]
```

Deploy:
```bash
npx wrangler deploy
```

## Notes
- `/go/*` responses are noindex via `_headers` and meta.
- Update the ClickBank hoplink inside `site/go/clickbank.html` if needed.
