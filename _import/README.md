# Imported from the Ghost site

Everything in this directory was taken off the live
`www.mechanicalsuperiority.com` on **2026-09-17**. It is raw material, not
content: nothing here is wired into `content/` or built. Move a file out of
here when it has been read, edited and given a home.

The live site is **Ghost 6.64**, launched September 2022 by Mark Mataczynski,
and it is nearly empty. The whole of it is:

- **`/`** — the Ghost Solo/Source theme index. Tagline: *"Custom engineering
  solutions, education for all things mechanical."* Three tag rails (News,
  Education, Racing) that all surface the same single post.
- **`/about/`** — Ghost's stock "About this site" boilerplate, unedited. It is
  the default copy about subscriptions and "start your own thing using Ghost."
  **Nothing in it is his writing.** Not imported.
- **`/coming-soon/`** — the stock placeholder post, likewise Ghost's own words.
  Not imported.
- **`/power-vs-torque/`** — the one real piece of writing on the site, and the
  reason to bother with any of this. Imported here in full.

## What is here

- `power-vs-torque.md` — the post, 3,000 words, converted HTML → markdown with
  pandoc and given Zola frontmatter. Published 2023-02-28, tagged Education
  and Racing.
- `images/` — the four images the post uses, plus `cover-image-1500.png`, the
  site's 1500×450 header cover.

## Two things to know before using the post

1. **It contains LaTeX.** Eight `$ … $` inline expressions — the speed,
   torque and power equations the argument is built on. Ghost was rendering
   them with its own math support; Zola will not. Either add KaTeX, or render
   the eight to SVG and inline them. The post does not work without them.
2. **One alt text is a joke about a Tropic Thunder line**, carried over
   verbatim from Ghost. Read the alt text before it ships.

## The logo

`static/logo.png` (1196×264, the wordmark with the bearing) and
`static/logo-mark.png` (700×700, the bearing alone) came from the same place;
`static/favicon.png` is the 256×256 favicon. The brand is two colors on
white: black, and `#e5fe15` — a hard chartreuse. It is a fine field and
border color and it **fails contrast as text or as a link color on white**,
so `style.css` keeps it as `--brand-accent` and does not use it for type.
