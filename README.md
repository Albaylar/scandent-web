# scandent-web

Public marketing + legal site for **ScanDent** (iOS app).

Separate from the private iOS repo so GitHub Free Pages works.

## Pages

| URL | File |
|---|---|
| `/` | `index.html` |
| `/terms/` | `terms/index.html` |
| `/privacy/` | `privacy/index.html` |

Live (after GitHub Pages): `https://albaylar.github.io/scandent-web/`

## GitHub Pages setup

1. Create **public** repo: `Albaylar/scandent-web`
2. Push this folder
3. **Settings → Pages** → Branch: `main` · Folder: **`/ (root)`**

## Custom domain (optional)

Point `scandent.app` CNAME to `albaylar.github.io` in GitHub Pages settings.

## Local preview

```bash
python3 -m http.server 8080
```
