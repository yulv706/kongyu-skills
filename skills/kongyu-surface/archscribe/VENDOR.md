# Vendored Archscribe engine

- Upstream: https://github.com/lazypay/Archscribe
- License: MIT (see LICENSE)
- Role: diagram renderer for kongyu-surface (not a standalone Codex skill)
- Layout: keep scripts/ and assets/ as siblings so ROOT=Path(__file__).parents[1] stays valid
- Omitted from vendor tree: .git, README*, docs/, tests/, assets/previews/, agents/, top-level SKILL.md
- Install: pip install -r requirements.txt
- Optional full browser renderer: pip install -r requirements-browser.txt && python -m playwright install chromium
