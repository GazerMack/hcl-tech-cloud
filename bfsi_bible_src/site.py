"""HTML site builder for the BFSI Techno-Functional Bible.

Composable helpers that emit HTML. No templating engine.
The output tree is:

    bfsi_bible/
      index.html
      foundations/index.html
      foundations/01-transactions.html
      ...
      assets/{css,js,vendor}
"""
from __future__ import annotations

from dataclasses import dataclass, field
from html import escape
from pathlib import Path
from typing import Iterable, Optional, Sequence


ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = ROOT / "bfsi_bible"


# ----------------------------------------------------------------- structure

@dataclass
class TopicLink:
    slug: str       # filename without .html
    title: str      # short display title in sidebar
    code: str       # e.g. "I.1"


@dataclass
class Part:
    roman: str      # "I"
    folder: str     # "foundations"
    name: str       # "Foundations"
    subtitle: str   # "The banker's IT map"
    blurb: str      # one-paragraph intro for the Part landing page
    topics: list[TopicLink] = field(default_factory=list)


@dataclass
class SiteIndex:
    parts: list[Part]


# ----------------------------------------------------------------- helpers

def _id(text: str) -> str:
    out, prev_dash = [], False
    for ch in text.lower():
        if ch.isalnum(): out.append(ch); prev_dash = False
        elif not prev_dash: out.append("-"); prev_dash = True
    return "".join(out).strip("-")


def render_sidebar(idx: SiteIndex, *, root_rel: str) -> str:
    parts_html = []
    for p in idx.parts:
        parts_html.append(
            f'<div class="part">{escape(p.roman)} — {escape(p.name)}</div>'
        )
        parts_html.append(
            f'<a href="{root_rel}{p.folder}/index.html">Overview</a>'
        )
        for t in p.topics:
            parts_html.append(
                f'<a class="topic" href="{root_rel}{p.folder}/{t.slug}.html">'
                f'{escape(t.code)} · {escape(t.title)}</a>'
            )
    nav = "\n".join(parts_html)
    return f"""
<aside class="sidebar">
  <div class="brand">
    <h1>BFSI Tech Bible</h1>
    <span class="subtitle">Techno-Functional Leader Reference</span>
  </div>
  <input class="search" type="search" placeholder="Filter sections…" />
  <nav>
    <a href="{root_rel}index.html">Home</a>
    <a href="{root_rel}glossary.html">Glossary</a>
    {nav}
  </nav>
</aside>
"""


def page_shell(*, title: str, body: str, idx: SiteIndex, root_rel: str,
               prev_link: Optional[tuple[str, str]] = None,
               next_link: Optional[tuple[str, str]] = None) -> str:
    nav_html = ""
    if prev_link or next_link:
        left = (f'<a href="{prev_link[0]}"><span class="dir">← Previous</span>{escape(prev_link[1])}</a>'
                if prev_link else "<span></span>")
        right = (f'<a href="{next_link[0]}"><span class="dir">Next →</span>{escape(next_link[1])}</a>'
                 if next_link else "<span></span>")
        nav_html = f'<nav class="page-nav">{left}{right}</nav>'

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="color-scheme" content="dark">
  <title>{escape(title)} · BFSI Tech Bible</title>
  <link rel="stylesheet" href="{root_rel}assets/css/style.css">
</head>
<body>
<div class="layout">
  {render_sidebar(idx, root_rel=root_rel)}
  <main class="content">
    {body}
    {nav_html}
  </main>
  <aside class="toc-right"><div class="label">On this page</div></aside>
</div>
<script src="{root_rel}assets/vendor/mermaid.min.js"></script>
<script src="{root_rel}assets/js/main.js"></script>
<script src="{root_rel}assets/js/notes.js" defer></script>
</body>
</html>
"""


# ----------------------------------------------------------------- HTML helpers

def H1(text: str) -> str: return f"<h1>{escape(text)}</h1>"
def H2(text: str) -> str: return f'<h2 id="{_id(text)}">{escape(text)}</h2>'
def H3(text: str) -> str: return f'<h3 id="{_id(text)}">{escape(text)}</h3>'
def H4(text: str) -> str: return f"<h4>{escape(text)}</h4>"
def lead(text: str) -> str: return f'<p class="lead">{text}</p>'
def p(text: str) -> str: return f"<p>{text}</p>"

def ul(items: Iterable[str]) -> str:
    return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"

def ol(items: Iterable[str]) -> str:
    return "<ol>" + "".join(f"<li>{x}</li>" for x in items) + "</ol>"

def kv(items: Iterable[tuple[str, str]]) -> str:
    return "<ul>" + "".join(
        f"<li><strong>{escape(k)}</strong> — {v}</li>" for k, v in items
    ) + "</ul>"


def difficulty(level: str) -> str:
    lvl = level.lower()
    cls = {"basic": "pill-basic", "inter": "pill-inter",
           "intermediate": "pill-inter", "advanced": "pill-advanced"}[lvl]
    label = {"basic": "Basic", "inter": "Intermediate",
             "intermediate": "Intermediate", "advanced": "Advanced"}[lvl]
    return f' <span class="pill {cls}">{label}</span>'


def callout(label: str, body_html: str, kind: str = "info") -> str:
    return (f'<div class="callout {escape(kind)}">'
            f'<span class="label">{escape(label)}</span>{body_html}</div>')


def primer(body_html: str) -> str:
    return callout("Primer — read this even if you think you know it", body_html, "primer")


def it_anchor(body_html: str, title: str = "From what you already know — your laptop") -> str:
    return callout(title, body_html, "it")


def bfsi_anchor(body_html: str, title: str = "From what you already know — your bank account") -> str:
    return callout(title, body_html, "bfsi")


def analogy(body_html: str) -> str:
    return callout("Analogy", body_html, "analogy")


def example(title: str, body_html: str) -> str:
    return callout(f"Worked example — {title}", body_html, "example")


def red_flag(body_html: str) -> str:
    return callout("Red flag — push back if you hear this", body_html, "red")


def table(headers: Sequence[str], rows: Sequence[Sequence[str]]) -> str:
    th = "".join(f"<th>{escape(h)}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>"
        for row in rows
    )
    return f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def mermaid(code: str, caption: str = "") -> str:
    """Render a Mermaid block. We do NOT HTML-escape the diagram source —
    Mermaid reads textContent. We strip surrounding blank lines because
    leading whitespace inside a <div> is not literal but a stray empty line
    can still confuse Mermaid's parser. Inputs are author-controlled so XSS
    is not a concern. We use <div class="mermaid"> (Mermaid's documented
    default selector)."""
    cap = f'<div class="cap">{escape(caption)}</div>' if caption else ""
    body = code.strip("\n")
    return f'<figure class="figure"><div class="mermaid">{body}</div>{cap}</figure>'


def term(word: str, tip: str) -> str:
    return f'<span class="term" data-tip="{escape(tip)}">{escape(word)}</span>'


# ----------------------------------------------------------------- topic builder

@dataclass
class TopicSection:
    heading: str
    level: str          # basic | intermediate | advanced
    body_html: str


@dataclass
class TopicPage:
    code: str
    slug: str
    title: str
    one_liner: str
    sections: list[TopicSection] = field(default_factory=list)

    def to_html(self) -> str:
        parts = [
            H1(f"{self.code} · {self.title}"),
            lead(self.one_liner),
        ]
        for s in self.sections:
            parts.append(f'<h2 id="{_id(s.heading)}">{escape(s.heading)}{difficulty(s.level)}</h2>')
            parts.append(s.body_html)
        return "\n".join(parts)


# ----------------------------------------------------------------- writer

def write_site(*, idx: SiteIndex,
               pages: list[tuple[str, str, str, Optional[tuple[str, str]], Optional[tuple[str, str]]]],
               home_html: str, glossary_html: str) -> None:
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    (SITE_DIR / "index.html").write_text(
        page_shell(title="Home", body=home_html, idx=idx, root_rel=""),
        encoding="utf-8")
    (SITE_DIR / "glossary.html").write_text(
        page_shell(title="Glossary", body=glossary_html, idx=idx, root_rel=""),
        encoding="utf-8")
    for rel, title, body, prev_l, next_l in pages:
        depth = rel.count("/")
        root_rel = "../" * depth
        out = SITE_DIR / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            page_shell(title=title, body=body, idx=idx, root_rel=root_rel,
                       prev_link=prev_l, next_link=next_l),
            encoding="utf-8",
        )
