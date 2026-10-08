#!/usr/bin/env python3
"""Write llms-full.txt: every page of the built site as markdown, in one file.

    zola build && python3 bin/llms-full.py public static/llms-full.txt && zola build

It reads the built HTML, not content/, because much of the site's text lives
in its templates. Pages come in the order static/llms.txt lists them, and
only the <main> of each is kept, so the header, nav and footer are not
repeated thirteen times. Equations become their TeX. A page in the sitemap
that llms.txt does not list is reported, because llms.txt is written by hand
and a new page has to be added to it.

Standard library only: CI runs it with whatever Python the runner has.
"""

import html as htmllib
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

SITE = "https://mechanicalsuperiority.com/"

BLOCK = {"p", "div", "section", "article", "header", "footer", "aside",
         "figure", "figcaption", "blockquote", "ul", "ol", "li", "table",
         "thead", "tbody", "tr", "dl", "dt", "dd", "hr", "pre",
         "h1", "h2", "h3", "h4", "h5", "h6"}
SKIP = {"script", "style", "svg", "nav", "form", "button", "noscript", "template"}


class Markdown(HTMLParser):
    def __init__(self, url):
        super().__init__(convert_charrefs=True)
        self.url = url
        self.depth = 0          # >0 while inside <main>
        self.skip = 0           # >0 while inside an element we drop
        self.math = None        # TeX being collected, or None
        self.math_block = False
        self.in_tex = False
        self.blocks = []        # finished markdown blocks
        self.line = []          # inline text of the block being built
        self.lists = []         # stack of ["ul"|"ol", counter]
        self.quote = 0
        self.heading = 0
        self.links = []         # hrefs of open <a>, None if not kept
        self.row = None         # cells of the table row being built
        self.table = None       # rows of the table being built
        self.caption = False
        self.cell = 0

    # The inline buffer becomes one block, prefixed for its context.
    def flush(self):
        text = re.sub(r"[ \t\r\n]+", " ", "".join(self.line)).strip()
        self.line = []
        if not text:
            return
        if self.row is not None:
            self.row.append(text.replace("|", "\\|"))
            return
        if self.heading:
            text = "#" * self.heading + " " + text
        elif self.caption:
            text = "*" + text + "*"
        elif self.lists:
            kind, n = self.lists[-1]
            mark = f"{n}." if kind == "ol" else "-"
            text = "  " * (len(self.lists) - 1) + mark + " " + text
        if self.quote:
            text = "> " + text
        self.blocks.append(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "main":
            self.depth += 1
            return
        if not self.depth:
            return
        if self.skip:
            if tag in SKIP:
                self.skip += 1
            return
        if tag in SKIP:
            self.skip = 1
            return
        if tag == "math":
            self.math = ""
            self.math_block = a.get("display") == "block"
            return
        if self.math is not None:
            self.in_tex = tag == "annotation" and a.get("encoding") == "application/x-tex"
            return
        if tag in BLOCK:
            self.flush()
        if tag in ("ul", "ol"):
            self.lists.append([tag, 0])
        elif tag == "li" and self.lists:
            self.lists[-1][1] += 1
        elif tag == "blockquote":
            self.quote += 1
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.heading = int(tag[1])
        elif tag == "figcaption":
            self.caption = True
        elif tag == "table":
            self.table = []
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th") and self.row is not None:
            self.flush()
            self.cell = len(self.row)
        elif tag in ("strong", "b"):
            self.line.append("**")
        elif tag in ("em", "i"):
            self.line.append("*")
        elif tag == "code":
            self.line.append("`")
        elif tag == "br":
            self.line.append(" ")
        elif tag == "a":
            href = a.get("href")
            if href and not href.startswith("#"):
                self.links.append(urljoin(self.url, href))
                self.line.append("[")
            else:
                self.links.append(None)
        elif tag == "img":
            alt = (a.get("alt") or "").strip()
            src = a.get("src")
            if alt and src:
                self.line.append(f"![{alt}]({urljoin(self.url, src)})")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in ("img", "br", "hr"):
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag == "main" and self.depth:
            self.flush()
            self.depth -= 1
            return
        if not self.depth:
            return
        if self.skip:
            if tag in SKIP:
                self.skip -= 1
            return
        if tag == "math" and self.math is not None:
            tex = self.math.strip()
            self.math = None
            if self.math_block:
                self.flush()
                self.blocks.append(f"$$ {tex} $$")
            else:
                self.line.append(f"${tex}$")
            return
        if self.math is not None:
            if tag == "annotation":
                self.in_tex = False
            return
        if tag in ("strong", "b"):
            self.line.append("**")
        elif tag in ("em", "i"):
            self.line.append("*")
        elif tag == "code":
            self.line.append("`")
        elif tag == "span":
            # Label and value often sit in adjacent spans with no space.
            self.line.append(" ")
        elif tag == "a" and self.links:
            href = self.links.pop()
            if href:
                self.line.append(f"]({href})")
        if tag in BLOCK:
            self.flush()
        if tag in ("ul", "ol") and self.lists:
            self.lists.pop()
        elif tag == "blockquote" and self.quote:
            self.quote -= 1
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.heading = 0
        elif tag == "figcaption":
            self.caption = False
        elif tag == "tr" and self.row is not None:
            if self.table is not None and self.row:
                self.table.append(self.row)
            self.row = None
        elif tag == "table" and self.table is not None:
            rows, self.table = self.table, None
            if rows:
                width = max(len(r) for r in rows)
                rows = [r + [""] * (width - len(r)) for r in rows]
                out = ["| " + " | ".join(rows[0]) + " |",
                       "|" + " --- |" * width]
                out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
                self.blocks.append("\n".join(out))
        elif tag in ("td", "th") and self.row is not None:
            self.flush()
            if len(self.row) == self.cell:
                self.row.append("")

    def handle_data(self, data):
        if not self.depth or self.skip:
            return
        if self.math is not None:
            if self.in_tex:
                self.math += data
            return
        self.line.append(data)

    def markdown(self):
        self.flush()
        return "\n\n".join(self.blocks)


def page_file(public, url):
    rel = url[len(SITE):]
    return public / rel / "index.html"


def meta(html, name):
    m = re.search(rf'<meta name="{name}" content="([^"]*)"', html)
    return htmllib.unescape(m.group(1)) if m else ""


def main():
    public, out = Path(sys.argv[1]), Path(sys.argv[2])
    llms = (Path(__file__).resolve().parent.parent / "static" / "llms.txt").read_text()
    order = re.findall(r"\]\((" + re.escape(SITE) + r"[^)]*)\)", llms)

    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    mapped = [e.text for e in ET.parse(public / "sitemap.xml").getroot().findall("s:url/s:loc", ns)]
    for url in mapped:
        if url not in order and "/tags/" not in url and not url.endswith("/writing/"):
            print(f"::warning::{url} is in the sitemap but not in static/llms.txt", file=sys.stderr)

    blurb = re.search(r"^> (.*)$", llms, re.M).group(1)
    parts = [
        "# Mechanical Superiority: the full text",
        f"> {blurb}",
        f"Every page of {SITE} as markdown, in the order of {SITE}llms.txt, "
        "made from the built site each time it deploys. Everything here may be "
        "read, indexed, quoted, summarized and used to train models.",
    ]
    for url in order:
        f = page_file(public, url)
        if not f.exists():
            print(f"::warning::{url} is in llms.txt but was not built", file=sys.stderr)
            continue
        html = f.read_text()
        p = Markdown(url)
        p.feed(html)
        body = p.markdown()
        desc = meta(html, "description")
        head = f"Source: {url}" + (f"\nSummary: {desc}" if desc else "")
        parts.append("---\n\n" + head + "\n\n" + body)

    out.write_text("\n\n".join(parts) + "\n")
    print(f"{out}: {len(order)} pages, {out.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
