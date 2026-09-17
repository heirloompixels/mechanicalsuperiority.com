# Mechanical Superiority

The site for **Mechanical Superiority LLC** — Mark Mataczynski's design and
fabrication shop in Fort Collins, Colorado. Zola, static, no JavaScript.

`CONTEXT.md` is the brief: who the business is, the positioning the copy
argues, and the open items Mark still owes. Read it before writing copy.
`docs/archive/site-update-plan.md` is the earlier plan `CONTEXT.md` supersedes
— kept for the record, not edited.

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

The domain still points at the Ghost site, which is being retired. When it
moves here:

1. Set `base_url = "https://mechanicalsuperiority.com"` in `config.toml`.
2. Add `static/CNAME` containing `mechanicalsuperiority.com` — the deploy
   action copies it to the published branch, and Pages reads it from there.
3. Point the DNS at GitHub Pages (apex A/AAAA records, or a `www` CNAME to
   `heirloompixels.github.io`).
4. Set the custom domain under Settings → Pages and turn on Enforce HTTPS
   once the certificate is issued.

Do not cancel Ghost before the DNS has moved and this site answers on the
domain. `TODO.md` carries the rest of the retirement.

## What is here

- `content/` — the pages. `_index.md` is the home page and carries its blocks
  in `[extra]`; `services.md`, `about.md` and `contact.md` are ordinary pages;
  `writing/` is the essays.
- `templates/` — `base` and `head` are shared; `index` is the home page,
  `page` the flat pages, `section` the writing index, `post` an essay.
- `static/` — `logo.png` (the wordmark), `logo-mark.png` (the bearing alone),
  `favicon.png`, `style.css`, and `images/` for the essay's photographs.
- `_import/` — what was taken off the Ghost site on 2026-09-17, kept as the
  record of the import. Nothing builds from it.
- `TODO.md` — what is missing, what is blocked on Mark, and what a second pass
  should do.

## Two things about the build

**No JavaScript, anywhere.** The essay's equations are **MathML**, rendered
once at import time with pandoc and baked into the markdown. No KaTeX, no
script tag, nothing to load. If another essay arrives with LaTeX in it, run it
through the same conversion rather than adding a math library.

**The URL `/power-vs-torque/` is fixed.** It is the one page with inbound
links and it is set explicitly with `path` in the post's frontmatter. Do not
let it move.

## Brand

Two colours on white: black, and `#e5fe15` off the logo. The chartreuse is
1.1:1 against white — it is a rule, field and highlight colour, never type and
never a link colour. The header is white because the logo is black on an
opaque white plate; inverting it merges the bearing's ring with its balls.
