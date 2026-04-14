#!/usr/bin/env python3
"""
Page generator for the Industrial Automation Field Guide.
Reads structured content dicts and emits HTML matching the site style.
Only touches files under the content_data dictionary; leaves others alone.
"""
from pathlib import Path
import html as _h
import re
import sys

REPO = Path(__file__).resolve().parent.parent

# Read the CSS / shell from an existing page so style stays in sync.
SHELL_FILE = REPO / "03_Control_Devices" / "Relays & Interposing Relays.html"

def read_shell():
    raw = SHELL_FILE.read_text(encoding="utf-8")
    # Pull the <style> block
    m = re.search(r"<style>(.*?)</style>", raw, flags=re.DOTALL)
    css = m.group(1) if m else ""
    return css

CSS = read_shell()

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Industrial Automation Field Guide</title>
  <style>{css}</style>
</head>
<body>
  <div id="layout">
    <nav id="sidebar" aria-label="Page contents">
      <div id="sidebar-header">
        <a href="{root_rel}index.html" class="site-title">
          Industrial Automation<br>Field Guide
        </a>
      </div>
      <div id="toc">
      <div class="toc">
{toc}
      </div>
      </div>
    </nav>
    <div id="main">
      <header id="page-header">
        <nav class="breadcrumb" aria-label="Location"><span class="bc-part">{folder}</span><span class="bc-sep"> / </span><span class="bc-current">{title}</span></nav>
        <h1 class="page-title">{title}</h1>
        <div class="meta-block">
{meta_rows}
        </div>
      </header>
      <article id="content">
{content}
      </article>
      <footer id="page-footer">
        <p>Industrial Automation Field Guide &mdash; v{version} &mdash; {status}</p>
      </footer>
    </div>
  </div>
</body>
</html>
"""

def esc(s):
    return _h.escape(str(s), quote=False)

def slug(txt):
    s = re.sub(r"[^a-zA-Z0-9\s-]", "", txt).strip().lower()
    s = re.sub(r"\s+", "-", s)
    return s

def render_meta(meta):
    rows = []
    def row(lbl, val):
        if not val: return
        rows.append(f'<div class="meta-row"><span class="meta-label">{lbl}</span><span class="meta-value">{val}</span></div>')
    status = meta.get("status","final")
    row("Status", f'<span class="status-badge status-{slug(status).replace("-","")}">{esc(status.title())}</span>')
    row("Version", esc(meta.get("version","1.0.0")))
    row("Difficulty", esc(meta.get("difficulty","Intermediate")))
    row("Category", esc(meta.get("category","")))
    row("Last Updated", esc(meta.get("updated","2026-04-13")))
    if meta.get("standards"):
        row("Standards", esc(meta["standards"]))
    if meta.get("equipment"):
        row("Equipment", esc(meta["equipment"]))
    tags = meta.get("tags") or []
    if tags:
        tag_html = " ".join(f'<span class="tag">{esc(t)}</span>' for t in tags)
        row("Tags", tag_html)
    return "\n".join(rows)

def render_toc(sections):
    lines = ["<ul>"]
    for title in sections:
        lines.append(f'<li><a href="#{slug(title)}">{esc(title)}</a></li>')
    lines.append("</ul>")
    return "\n".join(lines)

def render_table(headers, rows):
    out = ['<table>','<thead><tr>']
    for h in headers: out.append(f"<th>{esc(h)}</th>")
    out.append("</tr></thead><tbody>")
    for r in rows:
        out.append("<tr>")
        for c in r:
            out.append(f"<td>{c}</td>")
        out.append("</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)

def render_section(title, body):
    return f'<h2 id="{slug(title)}">{esc(title)}</h2>\n{body}\n<hr />'

def render_paragraphs(*ps):
    return "\n".join(f"<p>{p}</p>" for p in ps)

def render_list(items, ordered=False):
    tag = "ol" if ordered else "ul"
    out = [f"<{tag}>"]
    for it in items:
        out.append(f"<li>{it}</li>")
    out.append(f"</{tag}>")
    return "\n".join(out)

def render_tasks(items):
    out = ["<ul>"]
    for it in items:
        out.append(f'<li class="task unchecked"><span class="checkbox">&#x2610;</span> {it}</li>')
    out.append("</ul>")
    return "\n".join(out)

def render_code(code):
    return f'<pre><code>{esc(code)}</code></pre>'

def render_related(links):
    items = []
    for link_text, target in links:
        items.append(f'<a href="{target}">{esc(link_text)}</a>')
    out = ["<ul>"]
    for l in items: out.append(f"<li>{l}</li>")
    out.append("</ul>")
    return "\n".join(out)

def make_page(folder, filename, page):
    sections_order = [s["title"] for s in page["sections"]]
    # Always end with Related + Changelog
    sections_order += ["Related Topics", "Local Changelog"]
    toc_html = render_toc(sections_order)

    content_parts = []
    # intro
    intro_meta = (f"<p><strong>Category:</strong> <code>{esc(page['meta'].get('category',''))}</code><br/>"
                  f"<strong>Tags:</strong> <code>{esc(' '.join(page['meta'].get('tags',[])))}</code><br/>"
                  f"<strong>Difficulty:</strong> <code>{esc(page['meta'].get('difficulty','Intermediate'))}</code><br/>"
                  f"<strong>Last Updated:</strong> <code>{esc(page['meta'].get('updated','2026-04-13'))}</code><br/>"
                  f"<strong>Version:</strong> <code>{esc(page['meta'].get('version','1.0.0'))}</code><br/>"
                  f"<strong>Status:</strong> <code>{esc(page['meta'].get('status','final'))}</code></p>")
    content_parts.append(intro_meta)
    content_parts.append("<hr />")

    for s in page["sections"]:
        content_parts.append(render_section(s["title"], s["body"]))

    # Related topics
    rel_links = page.get("related", [])
    related_body = render_related(rel_links) if rel_links else "<p>See the Index for related subjects.</p>"
    content_parts.append(render_section("Related Topics", related_body))

    # Local changelog
    cl = render_table(
        ["Date","Version","Author","Notes"],
        [["2026-04-13","1.0.0","Field Guide Team","Initial full content release."]]
    )
    content_parts.append(render_section("Local Changelog", cl))

    content = "\n".join(content_parts)

    depth = 1  # all pages are one level deep
    root_rel = "../"

    html = PAGE_TEMPLATE.format(
        title=esc(page["title"]),
        css=CSS,
        root_rel=root_rel,
        folder=esc(folder),
        toc=toc_html,
        meta_rows=render_meta(page["meta"]),
        content=content,
        version=esc(page["meta"].get("version","1.0.0")),
        status=esc(page["meta"].get("status","Final").title()),
    )

    out_path = REPO / folder / filename
    out_path.write_text(html, encoding="utf-8")
    return str(out_path.relative_to(REPO))


if __name__ == "__main__":
    # This stub will be populated by content modules imported below.
    from content_pages import ALL_PAGES
    ok = 0
    for folder, files in ALL_PAGES.items():
        for filename, page in files.items():
            try:
                rel = make_page(folder, filename, page)
                print(f"OK  {rel}")
                ok += 1
            except Exception as e:
                print(f"ERR {folder}/{filename}: {e}")
    print(f"\nGenerated {ok} pages.")
