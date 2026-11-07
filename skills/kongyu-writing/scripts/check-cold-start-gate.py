#!/usr/bin/env python3
"""Structural opening smoke for HTML reports (karma #509/#511).

Rejects a raw data table or an empty opening. When an explicit structure-diagram
requirement applies, checks that the first element after the title block is a
diagram (svg, img, figure, or a Mermaid container). This does not verify the
reader-facing answer, evidence, boundary, or next action.

Placement rule (karma #521): the diagram belongs BELOW the title block
(topline/header), centered and width-limited — not as the page's first element.
So the check is: the first visible element after the title block is a diagram.

Usage:
    python check-cold-start-gate.py <html-file> [--unfamiliar-topic]
    --unfamiliar-topic: enforce the diagram structure check only when the
                         current task explicitly requires a first-screen diagram.

Exit 0 = pass, exit 1 = fail.
"""
import re
import sys
from pathlib import Path


def extract_body_content(html: str) -> str:
    m = re.search(r"<body[^>]*>(.*)</body>", html, re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else html


def strip_noise(body: str) -> str:
    """Remove non-content elements: nav/header/script/style/aside and hidden divs."""
    cleaned = body
    for tag in ["nav", "header", "script", "style", "aside"]:
        cleaned = re.sub(rf"<{tag}\b[^>]*>.*?</{tag}>", "", cleaned, flags=re.DOTALL | re.IGNORECASE)
    cleaned = re.sub(r'<[^>]*style="[^"]*display:\s*none[^"]*"[^>]*>.*?</div>', "", cleaned, flags=re.DOTALL | re.IGNORECASE)
    return cleaned.strip()


def first_visible_element(body: str) -> str:
    cleaned = strip_noise(body)
    if not cleaned:
        return "empty"
    m = re.match(r"<(\w+)", cleaned)
    return m.group(1).lower() if m else "text"


def after_title_element(body: str) -> str:
    """First visible element after the title block (h1/topline).

    Locates the topline container div (class containing "topline") that holds
    the h1, then walks forward tracking div open/close depth (h1 and other
    non-div tags do not nest) until the topline div closes. The first element
    after that close is returned.
    """
    cleaned = strip_noise(body)
    if not cleaned:
        return "empty"
    tm = re.search(r'<div\b[^>]*class="[^"]*topline[^"]*"[^>]*>', cleaned)
    if not tm:
        return first_visible_element(cleaned)
    i = tm.end()
    depth = 1
    guard = 0
    while i < len(cleaned) and depth > 0 and guard < 500:
        seg = cleaned[i:]
        m_div = re.search(r"<div\b[^>]*>", seg)
        m_divc = re.search(r"</div>", seg)
        m_h1 = re.search(r"<h1\b[^>]*>", seg)
        m_h1c = re.search(r"</h1>", seg)
        candidates = []
        for m2, step in [(m_div, "<div>"), (m_divc, "</div>"), (m_h1, "<h1>"), (m_h1c, "</h1>")]:
            if m2:
                candidates.append((m2.start(), m2.group(0), step))
        if not candidates:
            i += 1
            continue
        s, _tag, step = min(candidates, key=lambda x: x[0])
        if step == "<div>":
            depth += 1
        elif step == "</div>":
            depth -= 1
            if depth == 0:
                i += s + len("</div>")
                break
        i += s + len(step)
        guard += 1
    rest = cleaned[i:].lstrip()
    if not rest:
        return "empty"
    m2 = re.match(r"<(\w+)\b([^>]*)>", rest)
    if not m2:
        return "text"
    tag = m2.group(1).lower()
    attrs = m2.group(2)
    if tag in {"pre", "div"} and re.search(
        r"""\bclass\s*=\s*["'][^"']*\bmermaid\b[^"']*["']""",
        attrs,
        re.IGNORECASE,
    ):
        return "mermaid"
    return tag


def check(html_path: str, unfamiliar: bool) -> int:
    html = Path(html_path).read_text(encoding="utf-8", errors="replace")
    body = extract_body_content(html)
    first = first_visible_element(body)
    after_title = after_title_element(body)

    diagram_tags = {"svg", "img", "canvas", "picture", "figure", "mermaid"}
    table_tags = {"table"}
    visible_text = re.sub(r"<[^>]+>", "", strip_noise(body)).strip()
    has_graphic = bool(
        re.search(r"<(?:svg|img|canvas|picture|figure)\b", body, re.IGNORECASE)
        or re.search(
            r"""\bclass\s*=\s*["'][^"']*\bmermaid\b[^"']*["']""",
            body,
            re.IGNORECASE,
        )
    )
    if not visible_text and not has_graphic:
        print("FAIL structure: opening has no readable content or diagram")
        return 1

    if unfamiliar:
        if after_title in diagram_tags:
            print(f"PASS structure: element after title block is <{after_title}> (diagram position only)")
            return 0
        else:
            print(f"FAIL structure: element after title block is <{after_title}>, expected a diagram container for this explicitly diagram-led report")
            return 1
    else:
        if first in table_tags or after_title in table_tags:
            print(f"FAIL: raw data table before context (first=<{first}>, after-title=<{after_title}>)")
            return 1
        else:
            print(f"PASS structure: first element is <{first}>, after-title is <{after_title}>; semantic cold-start review remains required")
            return 0


def main():
    args = sys.argv[1:]
    unfamiliar = "--unfamiliar-topic" in args
    args = [a for a in args if a != "--unfamiliar-topic"]
    if not args:
        print("Usage: check-cold-start-gate.py <html-file> [--unfamiliar-topic]")
        return 2
    return check(args[0], unfamiliar)


if __name__ == "__main__":
    sys.exit(main())
