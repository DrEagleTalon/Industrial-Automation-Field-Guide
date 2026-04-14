#!/usr/bin/env python3
"""
Industrial Automation Field Guide — Markdown → HTML Converter
=============================================================
Usage:
    python convert_to_html.py

Converts every .md file in the repo to a matching .html file in the same
directory. Original .md files are left untouched.

Dependencies (auto-installed if missing):
    pyyaml, markdown
"""

import os
import re
import sys
import html as _html
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# ── Dependency bootstrap ──────────────────────────────────────────────────────

def _ensure(pkg, import_as=None):
    mod = import_as or pkg
    try:
        __import__(mod)
    except ImportError:
        import subprocess
        print(f"  [setup] Installing {pkg}…")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", pkg],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

_ensure("pyyaml", "yaml")
_ensure("markdown")

import yaml
import markdown as _md_lib

# ── Regex patterns ────────────────────────────────────────────────────────────

FRONTMATTER_RE         = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
WIKILINK_RE            = re.compile(r'\[\[([^\]]+)\]\]')
CHECKBOX_CHECKED_RE    = re.compile(r'<li>\[x\]', re.IGNORECASE)
CHECKBOX_UNCHECKED_RE  = re.compile(r'<li>\[ \]')

# ── Markdown → HTML ───────────────────────────────────────────────────────────

EXTENSIONS = ['extra', 'toc', 'sane_lists']
EXTENSION_CONFIGS = {
    'toc': {
        'permalink':  False,
        'toc_depth':  '2-4',
    }
}


def md_to_html(text: str):
    """Return (body_html, toc_html)."""
    converter = _md_lib.Markdown(
        extensions=EXTENSIONS,
        extension_configs=EXTENSION_CONFIGS,
    )
    body = converter.convert(text)
    toc  = getattr(converter, 'toc', '')
    return body, toc

# ── Frontmatter ───────────────────────────────────────────────────────────────

def parse_frontmatter(text: str):
    """Return (meta_dict, remaining_content)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, text[m.end():]

# ── Helpers ───────────────────────────────────────────────────────────────────

def scalar(val) -> str:
    """Flatten a YAML value that may be list, str, or None."""
    if val is None:
        return ''
    if isinstance(val, list):
        parts = [str(v).strip() for v in val if v and str(v).strip().lower() != 'none']
        return ', '.join(parts)
    s = str(val).strip()
    return '' if s.lower() == 'none' else s


def build_file_map(root: Path) -> dict:
    """Return {stem.lower(): Path_of_html_output} for every .md file."""
    fmap = {}
    for p in root.rglob('*.md'):
        fmap[p.stem.lower()] = p.with_suffix('.html')
    return fmap


def resolve_wikilinks(text: str, current: Path, fmap: dict) -> str:
    """Convert [[WikiLinks]] (and [[Target|Display]]) to <a> tags."""
    def _replace(m):
        inner = m.group(1).strip()
        if '|' in inner:
            target, display = inner.split('|', 1)
        else:
            target = display = inner
        key = target.strip().lower()
        if key in fmap:
            rel = os.path.relpath(fmap[key], current.parent).replace('\\', '/')
            return f'<a href="{rel}">{_html.escape(display.strip())}</a>'
        return f'<span class="broken-link">{_html.escape(display.strip())}</span>'
    return WIKILINK_RE.sub(_replace, text)


def fix_checkboxes(html: str) -> str:
    """Restyle task-list items that the markdown lib renders as plain text."""
    html = CHECKBOX_CHECKED_RE.sub(
        '<li class="task checked"><span class="checkbox">&#x2611;</span>', html)
    html = CHECKBOX_UNCHECKED_RE.sub(
        '<li class="task unchecked"><span class="checkbox">&#x2610;</span>', html)
    return html


def get_breadcrumb(md_file: Path, root: Path) -> str:
    rel   = md_file.relative_to(root)
    parts = list(rel.parts)
    crumbs = []
    for i, part in enumerate(parts):
        label = part.replace('.md', '')
        if i == len(parts) - 1:
            crumbs.append(f'<span class="bc-current">{_html.escape(label)}</span>')
        else:
            crumbs.append(f'<span class="bc-part">{_html.escape(label)}</span>')
    sep = '<span class="bc-sep"> / </span>'
    return sep.join(crumbs)


def build_meta_block(meta: dict) -> str:
    if not meta:
        return ''

    def row(label, val_html):
        if not val_html:
            return ''
        return (f'<div class="meta-row">'
                f'<span class="meta-label">{label}</span>'
                f'<span class="meta-value">{val_html}</span>'
                f'</div>')

    status = scalar(meta.get('status', ''))
    status_cls = re.sub(r'[^a-z]', '', status.lower())

    tags_raw = meta.get('tags', [])
    if isinstance(tags_raw, list):
        tags_html = ' '.join(
            f'<span class="tag">{_html.escape(str(t))}</span>'
            for t in tags_raw if t
        )
    elif tags_raw:
        tags_html = f'<span class="tag">{_html.escape(str(tags_raw))}</span>'
    else:
        tags_html = ''

    status_badge = (
        f'<span class="status-badge status-{status_cls}">'
        f'{_html.escape(status.title())}</span>'
    ) if status else ''

    rows = [
        row('Status',       status_badge),
        row('Version',      _html.escape(str(meta.get('version', '')))),
        row('Difficulty',   _html.escape(scalar(meta.get('difficulty', '')))),
        row('Category',     _html.escape(scalar(meta.get('category')))),
        row('Author',       _html.escape(scalar(meta.get('author')))),
        row('Last Updated', _html.escape(str(meta.get('last-updated', '')))),
        row('Standards',    _html.escape(scalar(meta.get('standards')))),
        row('Equipment',    _html.escape(scalar(meta.get('equipment')))),
        row('Tags',         tags_html),
    ]
    body = '\n'.join(r for r in rows if r)
    return f'<div class="meta-block">\n{body}\n</div>' if body else ''

# ── CSS ───────────────────────────────────────────────────────────────────────

CSS = """
/* ── Reset ───────────────────────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: 16px; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
               "Helvetica Neue", Arial, sans-serif;
  line-height: 1.7;
  color: #1a1a1a;
  background: #f4f4f0;
}
a { color: #1a56a0; text-decoration: none; }
a:hover { text-decoration: underline; }

/* ── Layout ──────────────────────────────────────────────────────────────── */
#layout {
  display: grid;
  grid-template-columns: 260px 1fr;
  min-height: 100vh;
}

/* ── Sidebar ─────────────────────────────────────────────────────────────── */
#sidebar {
  background: #1e2736;
  color: #c8d0dc;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
  border-right: 1px solid #141b27;
  scrollbar-width: thin;
  scrollbar-color: #2e3a4e transparent;
}
#sidebar::-webkit-scrollbar { width: 5px; }
#sidebar::-webkit-scrollbar-thumb { background: #2e3a4e; border-radius: 3px; }

#sidebar-header {
  padding: 1.4rem 1.25rem 1.1rem;
  border-bottom: 1px solid #2e3a4e;
}
.site-title {
  color: #e8ecf1;
  font-weight: 700;
  font-size: 0.82rem;
  line-height: 1.45;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  display: block;
}
.site-title:hover { text-decoration: none; color: #fff; }

#toc { padding: 1rem 1.25rem; }
#toc ul { list-style: none; padding: 0; margin: 0; }
#toc ul li { margin: 0.1rem 0; }
#toc ul li a {
  color: #9aa5b4;
  font-size: 0.8rem;
  display: block;
  padding: 0.2rem 0.4rem;
  border-radius: 3px;
  transition: background 0.12s, color 0.12s;
  line-height: 1.4;
}
#toc ul li a:hover { background: #2e3a4e; color: #e8ecf1; text-decoration: none; }
#toc ul ul { padding-left: 0.85rem; margin-top: 0.05rem; }
#toc ul ul li a { font-size: 0.75rem; }
#toc ul ul ul li a { font-size: 0.71rem; color: #6b7585; }

/* ── Main area ───────────────────────────────────────────────────────────── */
#main {
  background: #ffffff;
  padding: 2.5rem 3.5rem;
  max-width: 960px;
  min-height: 100vh;
}

/* ── Breadcrumb ──────────────────────────────────────────────────────────── */
.breadcrumb {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.1rem;
  font-size: 0.76rem;
  color: #888;
  margin-bottom: 0.8rem;
}
.bc-sep    { color: #ccc; margin: 0 0.05rem; }
.bc-part   { color: #888; }
.bc-current { color: #444; font-weight: 500; }

/* ── Page title ──────────────────────────────────────────────────────────── */
.page-title {
  font-size: 2.1rem;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.02em;
  color: #111;
  margin-bottom: 1.1rem;
}

/* ── Meta block ──────────────────────────────────────────────────────────── */
.meta-block {
  border: 1px solid #e4e4de;
  border-radius: 6px;
  padding: 0.8rem 1.1rem;
  margin-bottom: 2rem;
  background: #fafaf7;
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem 1.8rem;
}
.meta-row {
  display: flex;
  align-items: baseline;
  gap: 0.35rem;
  font-size: 0.8rem;
}
.meta-label {
  font-weight: 700;
  color: #666;
  text-transform: uppercase;
  font-size: 0.67rem;
  letter-spacing: 0.05em;
  white-space: nowrap;
}
.meta-value { color: #333; }

.status-badge {
  display: inline-block;
  padding: 0.1em 0.5em;
  border-radius: 3px;
  font-size: 0.69rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.status-final    { background: #d4edda; color: #155724; }
.status-draft    { background: #fff3cd; color: #856404; }
.status-inreview { background: #cce5ff; color: #004085; }
.status-review   { background: #cce5ff; color: #004085; }

.tag {
  display: inline-block;
  background: #eef1f8;
  color: #3b5ea6;
  padding: 0.1em 0.45em;
  border-radius: 3px;
  font-size: 0.71rem;
  font-family: ui-monospace, "SFMono-Regular", Consolas, monospace;
}

/* ── Article typography ──────────────────────────────────────────────────── */
#content h1,
#content h2,
#content h3,
#content h4,
#content h5,
#content h6 {
  font-weight: 700;
  line-height: 1.25;
  color: #111;
  margin-top: 2.25rem;
  margin-bottom: 0.65rem;
}
#content h1 {
  font-size: 1.8rem;
  border-bottom: 2px solid #e6e6e2;
  padding-bottom: 0.4rem;
}
#content h2 {
  font-size: 1.35rem;
  border-bottom: 1px solid #ebebeb;
  padding-bottom: 0.3rem;
}
#content h3 { font-size: 1.1rem; }
#content h4 { font-size: 1rem; }
#content h5 { font-size: 0.9rem; }
#content h6 { font-size: 0.85rem; color: #555; }

#content p { margin-bottom: 1rem; }

#content strong { font-weight: 700; }
#content em     { font-style: italic; }

#content code {
  font-family: ui-monospace, "SFMono-Regular", Consolas, "Courier New", monospace;
  font-size: 0.84em;
  background: #f0f0ec;
  padding: 0.15em 0.38em;
  border-radius: 3px;
  border: 1px solid #deded8;
}

#content pre {
  background: #1e2736;
  color: #c8d0dc;
  padding: 1.15rem 1.4rem;
  border-radius: 6px;
  overflow-x: auto;
  margin: 1.1rem 0 1.4rem;
  font-size: 0.84rem;
  line-height: 1.55;
  border: 1px solid #141b27;
}
#content pre code {
  background: none;
  padding: 0;
  border: none;
  border-radius: 0;
  color: inherit;
  font-size: inherit;
}

#content blockquote {
  border-left: 4px solid #b8c4d0;
  padding: 0.55rem 1.1rem;
  margin: 1.1rem 0;
  background: #f6f7fa;
  color: #555;
  border-radius: 0 5px 5px 0;
}
#content blockquote p:last-child { margin-bottom: 0; }

/* ── Tables ──────────────────────────────────────────────────────────────── */
.table-wrap {
  overflow-x: auto;
  margin: 1rem 0 1.6rem;
}
#content table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.875rem;
}
#content thead th {
  background: #1e2736;
  color: #e8ecf1;
  text-align: left;
  padding: 0.6rem 0.85rem;
  font-weight: 600;
  font-size: 0.77rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  border: 1px solid #141b27;
}
#content tbody tr:nth-child(even) { background: #f8f9fa; }
#content tbody tr:hover { background: #edf1f8; }
#content tbody td {
  padding: 0.5rem 0.85rem;
  border: 1px solid #e0e2e6;
  vertical-align: top;
  line-height: 1.55;
}

/* ── Lists ───────────────────────────────────────────────────────────────── */
#content ul,
#content ol {
  padding-left: 1.7rem;
  margin-bottom: 1rem;
}
#content li { margin-bottom: 0.3rem; }
#content li > ul,
#content li > ol { margin-top: 0.2rem; margin-bottom: 0; }

/* ── Task / checklist ────────────────────────────────────────────────────── */
#content li.task {
  list-style: none;
  margin-left: -1.7rem;
  padding-left: 2rem;
  position: relative;
}
#content li.task .checkbox {
  position: absolute;
  left: 0.15rem;
  font-size: 1rem;
  line-height: 1.4;
}
#content li.task.checked  { color: #555; }
#content li.task.checked  .checkbox { color: #2e7d32; }
#content li.task.unchecked .checkbox { color: #888; }

/* ── Horizontal rule ─────────────────────────────────────────────────────── */
#content hr {
  border: none;
  border-top: 1px solid #e6e6e2;
  margin: 1.75rem 0;
}

/* ── Broken wikilinks ────────────────────────────────────────────────────── */
.broken-link {
  color: #b22222;
  border-bottom: 1px dashed #b22222;
  font-style: italic;
  cursor: not-allowed;
}

/* ── Footer ──────────────────────────────────────────────────────────────── */
#page-footer {
  margin-top: 3.5rem;
  padding-top: 1rem;
  border-top: 1px solid #e6e6e2;
  font-size: 0.76rem;
  color: #aaa;
  text-align: center;
}

/* ── Responsive: tablet / mobile ─────────────────────────────────────────── */
@media (max-width: 900px) {
  #layout { grid-template-columns: 1fr; }
  #sidebar { position: static; height: auto; }
  #main { padding: 1.75rem 1.5rem; max-width: 100%; }
  .page-title { font-size: 1.6rem; }
}
@media (max-width: 600px) {
  #main { padding: 1.25rem 1rem; }
  .page-title { font-size: 1.35rem; }
  .meta-block { flex-direction: column; gap: 0.35rem; }
}

/* ── Print ───────────────────────────────────────────────────────────────── */
@media print {
  #sidebar { display: none; }
  #layout  { grid-template-columns: 1fr; }
  #main    { max-width: 100%; padding: 0; box-shadow: none; }
  #content a::after { content: " (" attr(href) ")"; font-size: 0.75em; color: #666; }
  #content pre { background: #f4f4f0; color: #222; border: 1px solid #ccc; }
  #page-header, #page-footer { page-break-inside: avoid; }
}
"""

# ── HTML page template ────────────────────────────────────────────────────────

PAGE_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Industrial Automation Field Guide</title>
  <style>
{css}
  </style>
</head>
<body>
  <div id="layout">

    <!-- Sidebar / page TOC -->
    <nav id="sidebar" aria-label="Page contents">
      <div id="sidebar-header">
        <a href="{root_rel}index.html" class="site-title">
          Industrial Automation<br>Field Guide
        </a>
      </div>
{toc_block}
    </nav>

    <!-- Main content -->
    <div id="main">
      <header id="page-header">
        <nav class="breadcrumb" aria-label="Location">{breadcrumb}</nav>
        <h1 class="page-title">{title}</h1>
{meta_block}
      </header>

      <article id="content">
{content}
      </article>

      <footer id="page-footer">
        <p>Industrial Automation Field Guide{version_line}</p>
      </footer>
    </div>

  </div>
</body>
</html>
"""

# ── Per-file conversion ───────────────────────────────────────────────────────

def convert_file(md_file: Path, root: Path, fmap: dict) -> str:
    text = md_file.read_text(encoding='utf-8', errors='replace')

    meta, content = parse_frontmatter(text)
    content       = resolve_wikilinks(content, md_file, fmap)
    body_html, toc_html = md_to_html(content)
    body_html     = fix_checkboxes(body_html)

    title   = str(meta.get('title') or md_file.stem)
    version = str(meta.get('version', ''))
    status  = str(meta.get('status', ''))

    version_parts = [f'v{version}' if version else '', status.title() if status else '']
    version_line  = ' &mdash; '.join(p for p in version_parts if p)
    if version_line:
        version_line = ' &mdash; ' + version_line

    depth    = len(md_file.relative_to(root).parts) - 1
    root_rel = ('../' * depth) if depth > 0 else './'

    breadcrumb = get_breadcrumb(md_file, root)
    meta_block = build_meta_block(meta)

    # Only include the TOC sidebar block if there's real content
    toc_block = ''
    if toc_html and '<li>' in toc_html:
        toc_block = f'      <div id="toc">\n      {toc_html}\n      </div>'

    html = PAGE_TEMPLATE.format(
        title        = _html.escape(title),
        css          = CSS,
        root_rel     = root_rel,
        breadcrumb   = breadcrumb,
        toc_block    = toc_block,
        meta_block   = ('        ' + meta_block) if meta_block else '',
        content      = body_html,
        version_line = version_line,
    )

    out = md_file.with_suffix('.html')
    out.write_text(html, encoding='utf-8')
    return str(md_file.relative_to(root))

# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    root = REPO_ROOT
    print("Industrial Automation Field Guide — HTML Generator")
    print(f"Repository root: {root}\n")

    fmap = build_file_map(root)
    print(f"Found {len(fmap)} markdown file(s).\n")

    ok = err = 0
    for md_file in sorted(root.rglob('*.md')):
        try:
            rel = convert_file(md_file, root, fmap)
            print(f"  OK  {rel}")
            ok += 1
        except Exception as exc:
            import traceback
            print(f"  ERR {md_file.relative_to(root)}: {exc}")
            traceback.print_exc()
            err += 1

    print(f"\n{'─' * 55}")
    print(f"Finished.  {ok} converted, {err} error(s).")
    if err:
        sys.exit(1)


if __name__ == '__main__':
    main()
