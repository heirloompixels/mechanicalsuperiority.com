# Mechanical Superiority

Zola site for mechanicalsuperiority.com. Scaffold only — the content and
design are still to come.

## Local development

```sh
zola serve
```

## Build

```sh
zola build
```

## Deployment

- Source repo: `git@github.com:heirloompixels/mechanicalsuperiority.com.git`
- GitHub Actions builds on pushes to `main` (`.github/workflows/main.yml`)
- Published branch: `gh-pages`
- Public URL, for now: `https://heirloompixels.github.io/mechanicalsuperiority.com/`

### Moving the domain

The site is on the GitHub Pages project URL until the domain is pointed here.
When it moves:

1. Set `base_url = "https://mechanicalsuperiority.com"` in `config.toml`.
2. Add `static/CNAME` containing `mechanicalsuperiority.com` — the deploy
   action copies it to the published branch, and Pages reads it from there.
3. Point the DNS at GitHub Pages (apex A/AAAA records, or a `www` CNAME to
   `heirloompixels.github.io`).
4. Set the custom domain under Settings → Pages and turn on Enforce HTTPS
   once the certificate is issued.

## Project structure

- `content/`: Zola sections and pages
- `templates/`: shared layout and page templates
- `static/`: assets copied verbatim into the built site
- `config.toml`: Zola configuration
