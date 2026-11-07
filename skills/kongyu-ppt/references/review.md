# Presentation Review Loop

Use this reference for deck-level review, prototype gates, rehearsal, and deciding whether multiple agents should participate.

## Pre-production correction replay

For a new deck or substantive rewrite:

1. Where Karma is configured, run `karma watch --surface ppt` before planning and apply its relevant open corrections. If the user cites earlier lessons, use Karma's active/archive lookup and inspect the actual human revision; use Akasha when raw history is needed. An empty reminder list does not establish that no lesson exists. Keep retrieval scoped to this task's failure pattern.
2. Separate the recurring failure from its old setting. Preserve necessary local conditions, reading-first explanation, and legitimate comparisons; do not import a prior page quota or layout recipe.
3. In the existing project spec, record the failure pattern, affected presentation unit, required change, and what the visible result must demonstrate. Reuse an existing feedback item for recurrence.
4. If the user rejected the current explanation, mark affected content readiness as needing revision. Repair reasoning and downstream page jobs before regeneration. This is a work-order constraint, not a new permission step.

For each page, identify the audience operation and the visible information that enables it. Naming a capability or putting labels in boxes does not explain a method. Make the relevant objects and relations available through a definition, example, comparison, figure, or formal account suited to the audience. Do not force a toy example into an expert reference deck.

When a deck raises a problem and then presents a taxonomy or literature map, show what the map helps the audience answer about that problem, at the level supported by the sources. Do not let a list of names impersonate an operational method or invent missing algorithm details.

For a requested **research map**, first select its purpose using `kongyu-writing/references/research-landscape-synthesis.md`: taxonomy, conceptual relations, evidence coverage and research findings need different evidence and encodings. A matrix with explicit coding can show research coverage; a conceptual dependency graph cannot substitute for evidence of results. For relationship maps, state the classification axis, place representative work, and label what connections mean. For coverage maps, define row/column categories, cell encoding and the included corpus. Do not add decorative arrows to qualify as a map. Permit cross-cutting studies with explicit coding rules. An empty cell does not establish novelty. In an overview-to-detail deck, put the selected overview before individual methods and retain its branch labels through the detail pages.

Validate the rendered map by asking whether a reader can locate a method, explain why it belongs there, distinguish a neighboring approach, and decode a cell, branch or connection as appropriate without consulting notes. Record one classification decision and one encoded meaning in the project review. A correct paper list or successful export does not pass this check.

## Information sufficiency before concision

Use this check when readers say the deck does not explain, lacks necessary information, or is poorly organized. First distinguish a missing definition, missing process link, wrong chapter order, unexplained abstraction, and redundant copy. They need different repairs. Do not use reduced word count as evidence that understanding improved.

1. **Reconstruct the reader's questions at chapter level.** For an approved outline, map each requested question to a visible page or sequence; mark omitted requirements and pages whose purpose belongs elsewhere. Rebuild dependent pages before polishing wording. An outline request means return an outline first; once approved, execute without adding another approval ritual.
2. **Check enough information is visible.** For a system/process, follow a concrete input through the operation, output and downstream action; include the decision conditions, failure path or feedback only when the requested scope needs them. If integration is being taught, show the essential request/response identities or hand-off fields rather than a box labelled “call API”. For a method, identify its input, actual operation, output and evidence needed to use that output. Names and arrows alone are not an explanation.
3. **Write concrete sentences.** Give abstract terms an identifiable object and action. A reader should be able to say who does what to which material and what changes. Do not invent algorithm details to fill a gap; narrow the claim or return to the evidence.
4. **Preserve distinct evidence roles.** In a research progress deck, distinguish what prior work established, what we actually did, what changed our understanding, and what remains planned. “New to us” is not a new contribution. A next-step slide names a deliverable and the decision or uncertainty it will resolve.
5. **Then apply the deletion test.** Remove supporting copy only after the explanation is sufficient. Notes may hold detail and citations, but cannot supply a premise needed to understand the visible reasoning. When grouping several papers, show which operation or distinction each supports; do not imply they jointly validated a combined workflow.

Replay both sides in the existing project review: one missing link restored and one redundant sentence kept off-screen. Review the rendered sequence, not just the titles. An expert reference deck may omit already-known basics, and a content-preserving formatting edit does not need a new outline. The repair does not mandate a fixed chapter count, an example on every slide, or code in every system talk. Human comprehension remains unverified until actually tested.

## Review separate failure layers

| Layer | Question | Evidence |
|---|---|---|
| Source | Are facts and borrowed visuals traceable? | source map, figure/code/page lookup |
| Argument | Does the conclusion follow? | ending, title chain, objections, boundaries |
| Slide semantics | What does this page make newly understandable? | job–claim–evidence contract |
| Attention | Is the intended first look obvious? | full-screen three-second test, room-distance test |
| Visual relation | Does the visual encode the real relation? | rendered page and montage |
| Artifact | Does the file open, edit, render and present correctly? | native PowerPoint/PDF render, package checks |
| Use | Can the speaker finish and can a listener follow? | timed rehearsal and independent listener notes |

No layer substitutes for another. A valid PPTX can tell a broken story. An AI can restate a dense slide that a room cannot read. A visual reviewer cannot certify domain truth.

## Review order

1. **Ending review:** is the final claim precise, useful, and bounded?
2. **Title/navigation check:** hide bodies and visuals, then inspect what the titles let the audience locate or anticipate. For a linear argument, test the claim chain; for a map, reading-first deck, or branchable session, test the chosen navigation and category structure instead of forcing a linear story.
3. **Contact sheet:** inspect the whole deck small. Look for rhythm, repeated compositions, missing turns, and an “all dense” pattern.
4. **Representative full-screen review:** inspect the hardest page roles at projection scale.
5. **Artifact checks:** run the producer's structural, overflow, font, image, chart, and native-render checks.
6. **Sequential listener test:** show or speak one complete causal arc in order. Ask for an unassisted retell, and record the first loss, wrong inference, or undefined term. AI restatement and expert source review do not count.
7. **Spoken rehearsal:** time the actual talk. Record where the speaker explains a slide instead of advancing the argument and where an independent listener loses the thread.

Return problems to their owner: weak claim → director; unsupported claim → evidence/domain layer; poor hierarchy → surface; overflow/rendering → executor.

Research basis: [Duarte's Glance Test](https://www.duarte.com/resources/guides-tools/the-glance-test/), [PPTAgent](https://aclanthology.org/2025.emnlp-main.728/), [PresentBench](https://arxiv.org/abs/2603.07244), and [SlideBench](https://www.slidebench.org/methodology).

## Learning from human revisions

When a user supplies a manually edited deck or asks to learn from revisions,
inspect the native pages and speaker notes before rewriting. Deletions, changed
order, and small mechanism labels are feedback too; do not read only comments
or compare word counts. Artifact tooling owns extraction and preservation.

For a requested learning comparison, distinguish the original draft (A), human
revision (B), and subsequent integrated result (C). Align corresponding pages
despite reordering. A→B supports observations about human changes; B→C checks
execution; A→C shows the combined result. Missing originals limit attribution;
a reconstruction is not the original. Do not require three new files for a
simple edit that does not need this comparison.

- Separate observed edits, explicit requests, inferred reasons, and verified
  outcomes. Unchanged pages are not approvals; edits made later by the agent
  are not evidence of human preference.
- Diagnose deleted language before adding more explanation: repetition,
  irrelevant detail, an undefined term, and a missing prerequisite need
  different repairs. Deleting a correct caveat does not refute it or imply
  that every page should be sparse. Put a necessary boundary at the judgment
  it qualifies; move optional detail to speech or reference material.
- Preserve the **function** of a deletion, not just its exact wording. If the
  rejected pattern is redundant explanation, do not restore a paraphrase in
  a footer, conclusion strip, or another corner. In speaker-led decks, do not
  automatically add an explanatory sentence or source/status string to every
  page. Keep a citation or condition visible when it is needed to identify the
  evidence or interpret the current decision; a reading-first slide may need
  more self-contained explanation.
- When asked to reduce pages, inventory repeated audience jobs before cutting
  content. Merge adjacent steps that form one inspectable event; move protocol
  inventories and secondary exceptions to notes or the companion document.
  Do not meet a page quota by shrinking text, dropping prerequisites, or
  splitting one explanation into many sparse pages. Keep a separate page only
  when its inference or visual change needs separate attention.
- For complaints about unnatural language, rewrite sentence-like explanatory
  copy as actor, action, object, and result: who checks what, what changes,
  and what happens next. Titles, entity/state labels, and other naming roles
  follow the text-role rule in `SKILL.md`; do not turn them into action sentences.
  Keep precise technical terms when necessary, but explain them at first use;
  do not replace an abstraction with a different unexplained abstraction.
  Read the actual slide copy aloud, not the accompanying design rationale.
- Preserve useful human-added step or mechanism labels. A title can orient
  and make a claim; do not force every title into the same assertion-only form.
  Across related diagrams, check whether changed actor positions or arrow
  directions make the audience rebuild an otherwise unchanged mental model.
- If feedback changes the design itself, settle that change before drawing
  and trace it through dependent slides and notes. Check the final artifact
  against B so regeneration does not restore deleted text or obsolete logic.

Before regeneration, translate the current correction into a small acceptance
check in the existing project contract. Inspect the exported slide content and
rendered placement, not only the plan or source. Exact-string checks can protect
particular deletions but cannot detect their paraphrases or misplaced function.
For a recurring failure, add a faithful project-level check through the artifact
owner, replay the rejected example, and include a near-neighbor that must remain
allowed (for example, a condition inside an attack diagram). Use semantic review
where no mechanical check is faithful. A passed rule-replay or revised skill
paragraph is not evidence that the next delivered deck obeys the correction.

Derive only the smallest reusable lesson supported by the edit and its role in
the talk. State its applicable scenario and a counterexample; keep local page
counts, technologies, layouts, and preferred density in the project. Native
rendering checks execution, not whether the human audience learned more.

## When a comparison is hard to follow

Hold the compared task, inputs, assumptions, and timing constant before showing
different outcomes. Put the shared setup once beside aligned paths; show each
path's relevant action or check and its resulting state. Do not make listeners
remember one system's case across several pages to compare it with another.

For attacks, name what the attacker obtained, when it was obtained, and whether
access continues. If event order changes the result, show that order. For claims
of incremental benefit, distinguish the effect of adding a check from the effect
of the proposed mechanism itself; use a simpler same-condition control when
needed to isolate the contribution. Do not invent evidence or weaken the
baseline to make the preferred option win. Keep equal outcomes and failures
visible too. These are comparison obligations, not a mandatory table, diagram
layout, third baseline, or fixed number of scenarios for every deck.

## Multi-agent boundary

Parallelize independent source search, evidence extraction, alternative access-structure proposals, and adversarial review. Keep one owner for the final conclusion and selected reasoning/access structure.

Do not split page production across agents before the page contracts and representative visual system are locked. After that point, parallel production is acceptable only when the artifact method preserves a shared visual context and a single reviewer can reconcile the result. Sequential authorship is safer for editable SVG/PowerPoint work whose geometry and rhythm depend on adjacent pages.

The value of multiple agents is independent judgment, not headcount.

## Prototype gate

Use a representative-page gate when the deck is long, the visual language is unsettled, or prior attempts expanded a bad pattern across the whole deck. Do not use it as a ritual for a three-slide deck or as permission to decide the story from the first five pages.

Pass the visual-range prototype when real viewers can identify each page's first look and retained claim, the pages span different roles, and the system expands without defaulting to cards or document pages. Pass the separate sequential prototype only when a human can retell the central event, causal change, and boundary after viewing the pages in order.

## Completion claim

### Final-output correction check

Inspect the exported pages and their actual copy, with the spec and notes closed:

- Reconstruct the explanation from what the audience can see. Record the first missing premise or unsupported step and its page. Reading-first material may use a lookup or comparison path rather than a linear story.
- Apply the deletion test below to visible text across the entire page, including subtitles, in-diagram captions, citations and adjacent caveats. A sentence does not become useful by moving out of the footer or next to a relevant object.
- Inventory the complete title chain and diagram labels from the rendered pages. For each title, determine whether it orients to an object, relation, or process; states a supported result; names an ordered step; or asks a question the page resolves. For each diagram label, distinguish an entity or state from an action or relation. Correct a label that narrates an action where the audience needs a stable entity name, but retain verbs that explain a real transition. Do not replace a clear sentence with an opaque noun phrase or require every page to use the same title form. Record the page number and reason for a corrected label and an intentionally retained action before export is called content-ready.
- Check whether titles orient the reader without carrying the whole paragraph. Topic, mechanism, step, and assertion titles remain available; no universal title form or character limit applies.
- Replay the applicable rejected pattern and one legitimate near-neighbor. Record page-specific observations in the existing validation record: what was removed or repaired, what was retained, and why. A generic “all checked” does not close a recurring correction.

This pass can establish that a correction appears in the artifact. It cannot establish human understanding or guarantee that a future deck will comply.

### Deletion test: does this text change the current inference?

For a redundancy correction, keep the page's job fixed and inspect the rendered page. Temporarily disregard each supporting sentence. State the specific relationship, decision, or evidence interpretation the reader would lose, or the concrete wrong inference its removal would cause. If none can be named, remove it from the screen. Preserve useful detail in notes when needed. Truth, relevance to the wider subject, proximity to a diagram, and "extra rigor" are not sufficient reasons to retain text.

Audit the whole deck for the same **function**, not just the rejected wording or location:

| Candidate pattern | Remove or move off-screen when | Keep when |
| --- | --- | --- |
| Repeated summary | The title, diagram or example already makes the same point | It integrates several results into a new conclusion the page needs |
| Defensive caveat | It answers an imagined criticism rather than a plausible reading of this page | Omitting it changes the scope of the displayed result or decision |
| Author/process commentary | It says why a slide exists, how it was researched, or what was not tested, without affecting the depicted claim | The evaluation process itself is the subject under comparison |
| Source/status caption | It only proves the author looked something up | Readers need the source identity to compare evidence, distinguish versions, or meet an explicit credit requirement |
| Generic advice | It could be pasted unchanged onto unrelated pages and supplies no missing premise | It specifies an operative rule, threshold, denominator, or exception used in the visible reasoning |

Use a compact contrast for calibration: on a page explaining **input → operation → action**, an extra "format correctness does not guarantee correctness" warning usually contributes no step; on a page evaluating correctness, that distinction may be the main point. Likewise, "no measurements shown" adds nothing beside an explicitly hypothetical example, while **measured versus simulated** must remain distinguishable when numerical results are compared. Retain the denominator of a percentage and the condition activating a decision branch: removing either changes the claim.

When a user rejects one instance, inspect the same pattern elsewhere before delivery. In the existing project review record, name the removed text, the page job, and why deletion preserves it; name a nearby retained condition and what removing it would break. Do not accept "necessary caveat" or "local condition" as a justification without that concrete consequence. A coordinate test or a forbidden-string check can prevent exact recurrence only; it cannot certify this semantic judgment.

Report separately what passed: source/argument review, rendered visual review, artifact checks, presenter rehearsal, and human listener comprehension. `artifact-ready`, `presenter-rehearsed`, and `audience-ready` are distinct states. If rehearsal or human comprehension has not happened, say so; do not close that gap with structural checks.
