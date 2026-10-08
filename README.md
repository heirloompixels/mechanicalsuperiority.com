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
- Public URL: `https://mechanicalsuperiority.com/` (the github.io address
  redirects there)

### The domain

Mark moved mechanicalsuperiority.com off Ghost and onto GitHub Pages on
2026-10-08, in Namecheap's Advanced DNS (Namecheap is registrar and DNS):

- `@` — four A records: `185.199.108.153`, `185.199.109.153`,
  `185.199.110.153`, `185.199.111.153`
- `www` — CNAME to `heirloompixels.github.io` (Pages redirects it to the apex)
- Mail is Namecheap's email forwarding (the `eforward` MX records and the SPF
  TXT). It was left alone and must stay.

On this side, `base_url` in `config.toml` is the domain, and `static/CNAME`
holds it so every deploy carries it into `gh-pages`. Without that file a
deploy would drop the custom domain. GitHub issued the certificate (for the
apex and `www`) within minutes of the move, and Enforce HTTPS is on.

Do not cancel Ghost before this site answers on the domain. `TODO.md` carries
the rest of the retirement.

### Being found

Mark wants the shop as visible as it can be, to search engines and to AI
alike, training included (2026-10-08). So:

- `templates/robots.txt` replaces Zola's default. It allows everything,
  names the search, AI and archive crawlers so none has to infer its
  welcome, carries `Content-Signal: search=yes, ai-input=yes, ai-train=yes`,
  and points at the sitemap. Never add a `Disallow`.
- `static/llms.txt` is the site in one page for language models, in the
  llmstxt.org shape. It is written by hand from each page's title and
  description, so **a new or renamed page goes into it too**.
- `head.html` asks search for full snippets and large image previews, gives
  each work page its own photograph as the share image, and carries the
  business (and, on the essay, a `BlogPosting`) as JSON-LD. Strings in the
  JSON-LD go through `json_encode`; HTML escaping would corrupt them.

## What is here

- `content/` — the pages. `_index.md` is the home page and carries its
  blocks in `[extra]`, in Mark's order of priority (design, reverse
  engineering, aluminum and stainless). `work/` is one page per project, each
  with its facts and pictures in `[extra]`. `about.md` carries the career
  timeline; `government.md` (the "Gov. Customers" page, `/government/`)
  carries NAICS codes and past performance. `services.md`, `contact.md`,
  `replacement-parts.md` and `remote-cad.md` are the rest; `writing/` is the
  essays, titled "Blog" on the site (Mark's word, 2026-10-08) at `/writing/`.
- `templates/` — `base` and `head` are shared; `index` is the home page;
  `macros.html` draws a project (model beside build) and its card;
  `work`, `project`, `about`, `government`, `replacement-parts` and
  `remote-cad` are their pages; `page` the plain ones, `section` the writing
  index, `post` an essay; `cta` and `timeline` are included pieces.
- `static/` — `logo.png` (the wordmark), `logo-mark.png` (the bearing alone),
  `favicon.png`, `style.css`, `images/` for the essay's photographs, and
  `images/work/` for the projects: web copies only, cropped, resized and with
  all metadata stripped, each with an `-sm` copy for cards. Originals stay in
  `from-mark/photos/`.
- `_import/` — what was taken off the Ghost site on 2026-09-17, kept as the
  record of the import. Nothing builds from it.
- `TODO.md` — what is missing, what is blocked on Mark, and what a second pass
  should do.
- `from-mark/` — **git-ignored and never committed.** What Mark sends (notes,
  original photos, documents made for him) and the sketchbook of site
  variations built from it. This repo is public; that folder is the private
  side. Only processed copies of photos, cropped and with metadata stripped,
  ever move into `static/`.

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
