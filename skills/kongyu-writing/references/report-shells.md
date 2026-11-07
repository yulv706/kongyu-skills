# Report Shells

Use these shells as starting points. Remove sections that do not pay rent for the current reader.

The default ordering principle is cognitive entropy reduction: the reader should know the answer, status, or recommended decision before they see the process trace. That answer should still feel naturally grown from evidence, constraints, and rejected alternatives, not pasted above the report. Use chronology only when the timeline itself is the object of judgment.

Place each material limitation beside the result it qualifies. Add a final boundary section only for remaining report-wide uncertainty; use a reader-facing title and do not repeat identical limitations. Research-result reports follow `references/report/result.md` for the first screen, examples and tables.

When in-scope artifacts already contain a metacognitive record, reuse it instead of reconstructing the turning story from chat logs. The default fields are:

- starting hypothesis
- decisive evidence
- boundary or claim change
- cost-model correction
- process/tooling issue
- next gate

Only surface this layer when it helps the current reader judge a pivot, a false start, a cost surprise, or a workflow redesign.

## Progress Report

```text
title/status
current answer/status
why it matters
why this follows
what changed
evidence
risks/boundaries
metacognitive turning points (if direction/cost changed)
next action
remaining report-wide boundary, if any (no fixed title)
appendix/provenance
```

Use when work is still active and the reader needs to know whether progress is real.

## Closure Report

```text
title/status
final result
why the result can be accepted
acceptance checks
changed artifacts
verification evidence
intentionally not done
remaining risks
metacognitive turning points (if direction/cost changed)
remaining report-wide boundary, if any (no fixed title)
reopen condition
appendix/source record
```

Use when a task, phase, or goal is being closed. Do not close with a vague "completed"; map requirements to evidence.

## Decision Memo

```text
question
recommended decision
why now
options considered
evidence table
tradeoffs and boundary
metacognitive turning points (if direction/cost changed)
decision trigger / stop condition
next action
remaining report-wide boundary, if any (no fixed title)
appendix/source record
```

Use when the reader needs to choose among options. Put the recommendation before the long evidence trail.

## Handoff Report

```text
current state / resume answer
what is preserved
what is unfinished
where to resume
commands/artifacts to verify
risks and ownership
metacognitive turning points (if direction/cost changed)
remaining report-wide boundary, if any (no fixed title)
appendix/log excerpts
```

Use when another agent or human should continue without reconstructing the whole session.

## Evidence Package

```text
claim or question
answer / evidence posture
evidence summary
source table
what each source proves
what each source does not prove
coverage gaps
metacognitive turning points (if direction/cost changed)
next check
remaining report-wide boundary, if any (no fixed title)
raw source appendix
```

Use when traceability matters. Search snippets, generated summaries, and relaxed retrieval results are discovery evidence, not final proof unless backed by source text or a stronger artifact.

## Self-Contained Chinese HTML

Default front-layer order:

```text
title/status chips
current decision/result
why this report exists
why this follows from the evidence
key evidence tables or ranked findings
boundaries and not-done items
metacognitive turning points (if direction/cost changed)
next action
结果适用范围（仅补充未就地说明的总体边界）
appendix with raw sources/provenance
```

Practical rules:

- Set `lang="zh-CN"` unless another language is requested.
- Keep the visible navigation and section headings Chinese.
- Use stable tables for decisions, evidence, acceptance checks, and provenance.
- A quantitative table needs a one-sentence caption and column headers that say what each column measures, its unit or denominator, and the applicable comparison. Give higher/lower direction only when the measure has an evaluative direction; descriptive quantities need no preferred direction. Rows are named in the reader's words. Replace source-layer labels (registered, matched, config A/B, K1, S3) with the real difference in sample or method. Put filters and comparison limits in one table note, and state the one most important difference in prose instead of reading out cells. See `references/report/result.md`.
- Separate source and reader layers. Markdown, CSV, JSON, or wide tables can be the machine/agent source of truth; HTML is the human reading interface. If a claim, label, field, or research-plan row is wrong, repair the source first and then synchronize the HTML. Never leave the source stale while only polishing the reader surface.
- Keep raw original-language material in appendices or collapsible sections.
- Avoid internal English workflow terms in the front layer when a natural Chinese phrase exists.
- Include enough embedded source material for offline review when the report is meant to be self-contained.
- For XiaoLab-facing reports, pass the portal identity, return-link target, and available `assets/xiaolab-portal-logo.png` to `kongyu-surface`. The surface owner chooses the live palette, logo placement, visual hierarchy, component shapes, and responsive behavior; this writing reference does not define a second visual system.
- Put the reader's decision path before implementation structure. Keep internal APIs, route names, run ids, and service labels out of the main reading path unless they change the next action. Frames, cards, tables, and spacing are chosen by `kongyu-surface` for that reading task.
- For a large portfolio, specify the questions readers must answer through search, grouping, comparison, and source lookup. Hand the resulting content and control requirements to the surface owner rather than prescribing a card layout.
- For large research-plan portfolios, make label semantics explicit near the filter controls. Do not expose bare `A/B/C/D` unless a legend states what they mean; prefer reader concepts such as `ready for pilot`, `needs narrowing`, `weak signal`, or `park/drop` when those labels are actually used by the source.
- For research-plan portfolios with levels, show `current_level` and `next_level_gate` separately from screening labels. The reader should see whether a plan is L1, L1+, L2-ready, L3-piloted, or parked, and what evidence would move it up. Do not let a strong screening label imply the plan has completed `Gamma_s/Omega_s/f*`.
- Do not expose internal project codes, temporary ranking labels, or agent-side shorthand in the reader-facing layer unless the page explains them before first use. If a code is only useful for internal continuity, replace it with the reader concept, for example `article-disclosure direction`, `claim-citation audit`, or `formal rerun validation`.
- For portfolio identifiers with multiple code systems, separate their legends. A family prefix such as `D/G/B/X` and a screening label such as `A/B/C/D` must not share one undifferentiated legend, because the same letter can mean different things.
- A long report may need section navigation so readers can find the relevant judgment or evidence. The surface owner chooses its placement and mobile behavior; the writing layer specifies the section names and their information order.
- Check that long identifiers, tables, formulas, and code remain readable in the declared target environment. Responsive overflow and print layout belong to `kongyu-surface`; the writing layer identifies which content must remain visible and in what reading order.
- Basic retrieval controls are part of a large portfolio's readability. Provide at least keyword search, the main category filter, the screening/status filter when labels exist, a clear/reset action, a visible result count, and an empty state. When method badges are shown, make method type filterable as well.
- In repeated plan cards, use progressive disclosure. The always-visible layer should show the plan identity, method/object badge, core question, and first low-cost pilot path. Put threats, mentor questions, caveats, and long provenance in `details/summary` or a visually secondary section unless the report's purpose is to compare those fields directly.
- Add method badges when they reduce scan cost, for example `text coding`, `API audit`, `public-record comparison`, `metadata check`, or `static artifact review`. Badges must describe the actual evidence operation, not a decorative category.
- Filtering and search need an empty state that tells the reader no records match the current filters and how to recover. Avoid silent blank grids.
- When regenerating HTML from a structured source table, run mechanical consistency checks before claiming the artifact is current: source row count, source column count, HTML card count, visible level/filter controls, stale internal-code scan, stale constraint-language scan, and `data-search` freshness. If a generated HTML card count is zero or mismatched, treat that as a failed build, not a cosmetic issue.
- Default ordering must respect the reader relationship. If the artifact is a map for advisor/human screening, do not default to an implied recommendation ranking such as `A -> D` unless the user explicitly asked for a ranked shortlist. Prefer neutral source order, family grouping, or user-controlled sorting; when sorting is used, state the sort key and keep non-ranked language.

## Anti-Patterns

- Chat dump: chronological messages without a reader-facing decision.
- Log dump: raw commands or service logs before the conclusion.
- Chronology trap: ordering sections by agent action sequence when the reader needs judgment first.
- Pasted conclusion: putting a decision at the top without showing how evidence and constraints make it the natural answer.
- Wrong house style: letting a tool's default theme replace the current XiaoLab project style without `kongyu-surface` review.
- Smooth hindsight: flattening a pivot into a clean ending and hiding the failed assumption or turning evidence when that turn matters.
- No failure surface: omitting the hidden assumptions or conditions under which the report's conclusion would be wrong.
- Mixed shell: Chinese headings with unexplained English workflow phrases throughout the front layer.
- Evidence theater: many sources listed without saying what they prove.
- False finish: "done" without acceptance checks or remaining-risk accounting.
