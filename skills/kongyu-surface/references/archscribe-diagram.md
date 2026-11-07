# Archscribe diagram track (surface-owned)

Human architecture / workflow / swimlane diagrams are part of the **human display layer**. They are not a separate Codex skill. The renderer is vendored under `archscribe/` inside this skill.

Upstream: [lazypay/Archscribe](https://github.com/lazypay/Archscribe) (MIT). See `archscribe/VENDOR.md` and `archscribe/LICENSE`.

## When to use this track

Use when the human-facing artifact is a **diagram deliverable**:

- architecture / system topology
- hand-drawn or Excalidraw-style tech diagram
- animated flow / GIF / MP4 architecture figure
- swimlane / comparison bands / free-form graph workflow
- Chinese triggers: 手绘架构图、动态架构图、泳道图、系统拓扑图、Excalidraw 风格图

Do **not** use this track for:

- product UI / page polish (use the main surface track)
- conversation-only interactive labs or simulators (`visualize` plugin skill)
- pure Mermaid one-liners when a fenced Mermaid block already answers the need
- machine-facing Markdown / contracts / schemas

## Layout choice

| Layout | Use for |
|--------|---------|
| `panorama` | whole system: inputs, core, decisions, detail panels |
| `swimlane` | parallel categories, roles, comparison bands |
| `graph` | custom topology, forks/joins, loops |

## Styles

- `default` — dark neon hand-drawn (brand hero)
- `paper` — light warm paper, DailyDoseOfDS-like

Prefer `paper` when the diagram will sit inside a light report/reader page. Prefer `default` for standalone dark architecture posters / GIF demos. Surface anti-slop bans on product **pages** still apply to UI chrome around the figure; the diagram engine's own neon style is intentional when `default` is chosen.

## Animation presets

`flow` (default) · `draw` · `relay` · `trace` · `chapter` · `failure-recovery`

Pillow renderer: reliable for `flow` → PNG / GIF / Excalidraw.  
Browser renderer (Playwright Chromium): full set including SVG / MP4 / interactive HTML and non-flow presets.

## Paths (this skill)

```text
SKILL_ROOT/archscribe/
  scripts/render_animated_diagram.py   # main entry
  scripts/doctor.py
  assets/default-spec.json
  assets/examples/
  assets/fonts/ assets/icons/ assets/vendor/
  archscribe/references/spec-format.md
  references/illustrated-icons.md
  requirements.txt
  requirements-browser.txt
```

Resolve paths from the skill root:

```text
ARCH = <this skill dir>/archscribe
```

## Workflow

1. **Doctor** (once per session if unsure):

```bash
python -X utf8 ARCH/scripts/doctor.py
```

- base packages missing → `python -m pip install -r ARCH/requirements.txt`
- browser path needed → `python -m pip install -r ARCH/requirements-browser.txt && python -m playwright install chromium`
- no Chromium → use `--renderer pillow` (PNG/GIF/Excalidraw)

2. **Write spec** from `ARCH/assets/default-spec.json` or `ARCH/assets/examples/`. Field reference: `ARCH/references/spec-format.md`. Keep titles short; put detail in bodies/notes.

3. **Validate**:

```bash
python -X utf8 ARCH/scripts/render_animated_diagram.py --spec SPEC.json --outdir OUT --validate-only
```

4. **Layout review PNG**:

```bash
python -X utf8 ARCH/scripts/render_animated_diagram.py --spec SPEC.json --outdir OUT --basename diagram --renderer pillow --formats png --check
```

5. **Publish set** (Pillow path):

```bash
python -X utf8 ARCH/scripts/render_animated_diagram.py --spec SPEC.json --outdir OUT --basename diagram --renderer pillow --formats png,gif,excalidraw --verify --check
```

6. **Full browser publish** (when Chromium available):

```bash
python -X utf8 ARCH/scripts/render_animated_diagram.py --spec SPEC.json --outdir OUT --basename diagram --formats gif,mp4,png,excalidraw,svg,html --verify --check --strict-formats
```

7. **Visual check** before delivery: overlap, crossing connectors, cramped labels, weak hierarchy, clipped sides. Fix the **spec**, not the PNG, when structure is wrong.

## Output placement

- Scratch: `_tmp/<task-slug>/` or the thread visualization dir when the app provides one
- Durable product/report figures: under the **owning project** `docs/figures/` (or project-owned assets), never skill tree, never workspace root
- Prefer shipping `.excalidraw` + `.png` together when the user may edit later; add `.gif`/`.mp4` only when motion helps explanation

## Ownership vs other tracks

| Need | Owner |
|------|--------|
| Page/UI/report reader polish, anti-slop, Chinese type | main `kongyu-surface` track |
| Hand-drawn / animated architecture diagram | **this track** (same skill) |
| Interactive conversation lab / adjustable simulator | `visualize` plugin skill |
| Report facts / evidence structure | Report skill first, then surface for human display |

## Quality gate (diagram-specific)

- [ ] Layout matches content type (panorama / swimlane / graph)
- [ ] Language matches user; titles short
- [ ] PNG checked for overlap / clip / hierarchy
- [ ] Requested formats actually exist; `--check` reports ok
- [ ] Editable `.excalidraw` kept when future edit is likely
- [ ] No standalone `archscribe` skill created; routing stays on `kongyu-surface`
