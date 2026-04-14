#!/usr/bin/env python3
"""
Industrial Automation Field Guide — Single-File Markdown → HTML Converter
=========================================================================

Convert ONE .md file to a matching .html file. The bulk converter
(`convert_to_html.py`) walks the whole repo; this script does just one page,
which is handy when you're iterating on a single document.

Three ways to use it
--------------------

1. Edit the TARGET_FILE constant below, then run with no arguments:

       python scripts/convert_one_to_html.py

2. Run with no arguments and TARGET_FILE empty — the script will ask:

       $ python scripts/convert_one_to_html.py
       Path to markdown file: markdown/04_Motor_Control/Soft Starters.md

3. Pass the path on the command line (most useful from any shell):

       python scripts/convert_one_to_html.py "markdown/04_Motor_Control/Soft Starters.md"
       python scripts/convert_one_to_html.py path/to/file.md -o build/file.html

Path resolution
---------------
Relative paths are resolved against the current working directory first,
then against the repository root. Absolute paths are used as-is.

Output
------
By default the .html lands next to the source .md (same as the bulk script).
Use `-o/--output` (or set `OUTPUT_FILE`) to write somewhere else.

Dependencies are inherited from `convert_to_html.py` (pyyaml, markdown).
"""

# ─── User-configurable defaults (used when no CLI argument is given) ──────
# Leave both blank to be prompted at runtime.
TARGET_FILE = "instructions/git-and-github-guide.md"    # e.g. "markdown/04_Motor_Control/Soft Starters.md"
OUTPUT_FILE = "instructions/git-and-github-guide.html"    # e.g. "build/Soft Starters.html"; blank = next to the .md
# ──────────────────────────────────────────────────────────────────────────

import argparse
import html as _html
import sys
from pathlib import Path

# Reuse all the heavy lifting (CSS, template, helpers) from the bulk script.
# We add the script's own folder to sys.path so this works no matter where
# the user runs it from.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from convert_to_html import (  # noqa: E402  (intentional late import)
    REPO_ROOT,
    CSS,
    PAGE_TEMPLATE,
    build_file_map,
    build_meta_block,
    fix_checkboxes,
    get_breadcrumb,
    md_to_html,
    parse_frontmatter,
    resolve_wikilinks,
)


# ─── Conversion ───────────────────────────────────────────────────────────

def convert_one(md_path: Path, out_path: Path | None = None, *, quiet: bool = False) -> Path:
    """Convert a single .md file to .html and return the output path."""
    md_path = md_path.resolve()

    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")
    if md_path.suffix.lower() != ".md":
        raise ValueError(f"Not a .md file: {md_path}")

    # The page template uses paths relative to the repo root (for breadcrumb
    # and root_rel). Require the input to live inside REPO_ROOT.
    try:
        md_path.relative_to(REPO_ROOT)
    except ValueError as exc:
        raise ValueError(
            f"File must be inside the repository ({REPO_ROOT}): {md_path}"
        ) from exc

    # Wikilink map needs the whole repo so [[Other Topic]] still resolves.
    fmap = build_file_map(REPO_ROOT)
    if not quiet:
        print(f"Repository root : {REPO_ROOT}")
        print(f"Wikilink targets: {len(fmap)} markdown file(s)")
        print(f"Converting      : {md_path.relative_to(REPO_ROOT)}")

    # ── Mirror the per-file pipeline from convert_to_html.convert_file ──
    text = md_path.read_text(encoding="utf-8", errors="replace")

    meta, content = parse_frontmatter(text)
    content = resolve_wikilinks(content, md_path, fmap)
    body_html, toc_html = md_to_html(content)
    body_html = fix_checkboxes(body_html)

    title = str(meta.get("title") or md_path.stem)
    version = str(meta.get("version", ""))
    status = str(meta.get("status", ""))

    version_parts = [f"v{version}" if version else "", status.title() if status else ""]
    version_line = " &mdash; ".join(p for p in version_parts if p)
    if version_line:
        version_line = " &mdash; " + version_line

    depth = len(md_path.relative_to(REPO_ROOT).parts) - 1
    root_rel = ("../" * depth) if depth > 0 else "./"

    breadcrumb = get_breadcrumb(md_path, REPO_ROOT)
    meta_block = build_meta_block(meta)

    toc_block = ""
    if toc_html and "<li>" in toc_html:
        toc_block = f'      <div id="toc">\n      {toc_html}\n      </div>'

    html = PAGE_TEMPLATE.format(
        title=_html.escape(title),
        css=CSS,
        root_rel=root_rel,
        breadcrumb=breadcrumb,
        toc_block=toc_block,
        meta_block=("        " + meta_block) if meta_block else "",
        content=body_html,
        version_line=version_line,
    )

    final_out = out_path.resolve() if out_path else md_path.with_suffix(".html")
    final_out.parent.mkdir(parents=True, exist_ok=True)
    final_out.write_text(html, encoding="utf-8")
    return final_out


# ─── Path resolution ──────────────────────────────────────────────────────

def _resolve_input(raw: str) -> Path:
    """Strip surrounding quotes/whitespace, then resolve against CWD or REPO_ROOT."""
    s = raw.strip().strip('"').strip("'")
    p = Path(s)
    if p.is_absolute():
        return p
    cwd_candidate = (Path.cwd() / p).resolve()
    if cwd_candidate.exists():
        return cwd_candidate
    return (REPO_ROOT / p).resolve()


def _pick_target(args: argparse.Namespace) -> tuple[Path, Path | None]:
    """Decide which file to convert based on (in order): CLI arg, constant, prompt."""
    # 1. Command-line argument
    if args.file:
        target = _resolve_input(args.file)
    # 2. Constant edited in this file
    elif TARGET_FILE.strip():
        target = _resolve_input(TARGET_FILE)
    # 3. Interactive prompt
    else:
        try:
            answer = input("Path to markdown file: ")
        except EOFError:
            answer = ""
        if not answer.strip():
            print(
                "\nNo file given. Either:\n"
                "  • pass a path on the command line\n"
                "  • edit TARGET_FILE near the top of this script\n"
                "  • type a path at the prompt",
                file=sys.stderr,
            )
            sys.exit(2)
        target = _resolve_input(answer)

    # Output path: CLI > constant > None (default location)
    if args.output:
        out = _resolve_input(args.output)
    elif OUTPUT_FILE.strip():
        out = _resolve_input(OUTPUT_FILE)
    else:
        out = None

    return target, out


# ─── Entry point ──────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="convert_one_to_html.py",
        description=(
            "Convert one Industrial Automation Field Guide markdown file to "
            "HTML. With no arguments, uses the TARGET_FILE constant inside "
            "the script, or prompts if that is empty."
        ),
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="Path to the .md file (relative to CWD or repo root, or absolute).",
    )
    parser.add_argument(
        "-o", "--output",
        help="Optional output .html path. Defaults to the same folder as the source.",
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress informational output.",
    )
    args = parser.parse_args()

    target, out = _pick_target(args)

    try:
        result = convert_one(target, out, quiet=args.quiet)
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERR  {exc}", file=sys.stderr)
        sys.exit(1)
    except Exception:  # pragma: no cover  -- show full trace for unexpected errors
        import traceback
        traceback.print_exc()
        sys.exit(1)

    rel = result
    try:
        rel = result.relative_to(REPO_ROOT)
    except ValueError:
        pass
    print(f"OK   {rel}")


if __name__ == "__main__":
    main()
