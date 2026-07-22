# scandent-web

Public marketing + legal site for **ScanDent** (iOS + Apple Watch).

Separate from the private iOS repo so GitHub Free Pages works.

## Pages

| URL | File |
|---|---|
| `/` | `index.html` |
| `/terms/` | `terms/index.html` |
| `/privacy/` | `privacy/index.html` |

Live: **https://albaylar.github.io/scandent-web/**

## Assets

| File | Source |
|---|---|
| `assets/logo.png` | ScanDent app logo (512px) |
| `assets/logo-mark.png` | Header / nav mark (180px) |
| `assets/app-icon.png` | Apple touch icon |
| `assets/favicon.png` | Browser favicon |
| `assets/watch/today.png` | Watch Today screen |
| `assets/watch/brush-timer.png` | Watch brush timer screen |

Logo copied from iOS `AppLogo.imageset` / `AppIcon.appiconset`.

## GitHub Pages setup

1. Public repo: `Albaylar/scandent-web`
2. Push this folder
3. **Settings → Pages** → Branch: `main` · Folder: **`/ (root)`**

## Custom domain (optional)

Point `scandent.app` CNAME to `albaylar.github.io` in GitHub Pages settings.

## Local preview

```bash
cd scandent-web
python3 -m http.server 8080
# open http://localhost:8080
```

## Deploy

```bash
git add .
git commit -m "feat: refresh marketing site with app logo and Watch/pricing"
git push origin main
```

GitHub Pages updates in ~1–2 minutes.
