---
name: kongyu-ppt
description: "流云演示. Use for designing, restructuring, or reviewing a presentation/PPT/deck as a live communication system: audience change, reasoning/access structure, slide jobs, claim-evidence structure, cognitive load, rehearsal, and presentation-level QA. For academic talks also load the academic reference. For visual styling use kongyu-surface; for SVG/PPTX implementation, templates, rendering, or export use ppt-master."
---

# L1uyun PPT

## Output contract

Completion requires an audience capability, scenario variables, a derived
reasoning/access structure, claim/evidence mapping, and a validation plan; output those decisions and
the remaining uncertainty before handing artifact work to `ppt-master`.

Own the **presentation director layer**: establish the general constraints that make communication work, derive a method from the actual situation, and only then specify concrete slide practices. A presentation is not a document broken into pages and not a file-generation task.

## Boundary

| Layer | Owner | Decides |
|---|---|---|
| Presentation principles and method derivation | **This skill** | audience capability, scenario variables, reasoning spine, evidence status, screen/speech/detail split, validation |
| Domain evidence | Relevant domain skill or project source | what may be claimed, source strength, uncertainty, domain conventions |
| Visual surface | `kongyu-surface` | typography, colour, composition, page families, diagrams, visual polish |
| Artifact execution | `ppt-master` | project files, SVG/PPTX authoring, template intake, rendering, export, notes/audio/animation tooling |

Do not absorb templates, SVG/PPTX code, brand assets, rendering instructions, or file conversion. Do not put project-specific technologies, attacks, stories, or page sequences into the universal principle layer.

## Use / Do not use

Use when the user asks to make, redesign, outline, explain, review, or improve a presentation; when a deck feels dense, flat, discontinuous, template-like, or unlike a human talk; or when slides must teach, persuade, defend, support a decision, or survive live questioning.

Do not use for pure PPTX conversion/export, content-preserving native edits, notes/audio/transitions, or package repair after story and slide meaning are already locked. Route those directly to `ppt-master`.

## Method architecture

Keep five levels distinct:

```text
universal principles
→ scenario variables
→ derived method
→ project-specific practices
→ purpose-matched validation
```

- **Principles** constrain judgment across presentations.
- **Scenario variables** describe the audience, purpose, evidence maturity, content topology, delivery mode, time, and cost of misunderstanding.
- **Method** organizes the reasoning for a class of situations.
- **Practices** are concrete moves in one deck.
- **Validation** observes the audience capability named by the purpose.

When creating or substantially restructuring a deck, read [references/principles-and-derivation.md](references/principles-and-derivation.md) before selecting any story recipe or page pattern.

## Reuse corrections before production

For new decks and substantive rewrites, apply [review.md § Pre-production correction replay](references/review.md#pre-production-correction-replay). When the user points to earlier lessons, retrieve the matching feedback and human revisions, including archived records; an empty reminder query does not establish that no lesson exists. In the existing project spec, map each applicable correction to the affected pages and a visible acceptance check. Carry forward the failure and its acceptance condition, not an old page count, density target, story recipe, or approval ritual.

If the user rejects the explanation, invalidate the affected content-readiness decision and repair its dependent page contracts before expanding or regenerating. A new motivation may change the argument, not merely add a page. Keep content-preserving artifact edits on their narrow route.

If the complaint is missing information, poor organization, or language that does not explain, run [review.md § Information sufficiency before concision](references/review.md#information-sufficiency-before-concision) before deleting copy. A shorter deck can preserve the same missing prerequisites. When the user supplies an outline, map its reader questions to visible pages and keep its approved order; do not preserve an obsolete story merely by renaming its sections.

For a literature/research-map request, use `kongyu-writing/references/research-landscape-synthesis.md` for source synthesis and choosing between taxonomy, conceptual relations, evidence coverage and results. Then apply [review.md](references/review.md#pre-production-correction-replay) to the presentation. A coded coverage matrix can be the appropriate map; a grouped paper list does not establish research findings.

## Director workflow

**Critical screen-copy rule — no automatic lower-left explanation.** Do not
fill the lower-left corner with a summary sentence, reminder, defensive caveat,
scope/status notice, or an explanation appended to a citation. A technically
correct sentence does not earn screen space merely by being correct. Put a
condition needed for the current inference beside the relevant diagram or
claim; put supplementary explanation in speaker notes. Required credits and
explicitly requested notes are not a license to add a prose tail. Check the
actual rendered slides for this pattern, including paraphrases and relocation
to another bottom strip; do not validate only a list of deleted strings.

1. **Classify the delivery system.** Speaker-led, reading-first, hybrid, interactive workshop, demo, or asynchronous review. Choose a primary mode.
2. **Name the audience capability.** State what the audience should be able to explain, decide, predict, compare, remember, or do—not merely what content they should see.
3. **Capture only method-changing variables.** Audience prior knowledge, resistance, evidence maturity, reasoning topology, time/control, available evidence, and consequence of misunderstanding.
4. **Derive and justify the method.** Compare plausible reasoning and access structures and choose the smallest combination that serves the audience capability. Do not begin from a favorite template, storytelling framework, or prior project tactic.
5. **Map epistemic status.** Separate facts, observations, interpretations, proposals, proof obligations, results, and boundaries before deciding what appears as evidence.
6. **Define the conclusion and access structure.** State the smallest useful conclusion and boundary. Make every required prerequisite available before or at its point of use; choose a linear, branchable, or non-linear structure from the delivery mode and reasoning task. Check chapter-level questions before page-level jobs. For a system explanation, ensure readers can connect inputs, operations, outputs and downstream use at the requested depth; for a research status report, keep prior work, our completed work, new information and plans distinguishable.

   For an unfamiliar idea built from several bodies of knowledge, consider a **knowledge-system structure**: establish each foundation's purpose, objects, structure, normal process and relevant properties before explaining the combination. If a chapter → subsection hierarchy is selected, apply [the knowledge-system route and coverage gate](references/teaching-complex-systems.md#construct-the-knowledge-system-candidate). Chapter names identify the knowledge subject; subsections organize its reader questions; pages explain the required relations. A worked example may support a subsection without becoming the whole talk's story. Renaming an old event-led outline does not establish this hierarchy.
7. **Assign presentation units.** A unit may be a slide, build, demonstration action, spoken question, or pause. Bound it by one audience inference or decision, not a word count.
8. **Divide screen, speech, and detail.** Keep jointly inspected material on screen; explanation and transition in speech; exhaustive material in notes, appendix, or a companion document.
9. **Prototype what is uncertain.** Visual range, sequential comprehension, interaction, or artifact mechanics are different uncertainties and require different prototypes.
10. **Validate the intended outcome.** Run source, argument, attention, visual, artifact, rehearsal, and audience checks only when they measure the layer being claimed.

## Presentation contract

Keep the intermediate contract human-readable and reuse the owning project's existing spec when possible.

At deck level, record only what changes execution:

| Field | Question |
|---|---|
| `audience_capability` | What observable audience change is the deck for? |
| `scenario_variables` | Which facts changed the selected method? |
| `derived_method` | Which reasoning/access path, abstraction ramp, and delivery pattern follow from those variables? |
| `method_rationale` | Why is each selected component necessary for this audience capability? |
| `rejected_methods` | Which plausible alternatives were rejected, and why? |
| `validation` | What evidence can establish the intended audience capability? |
| `known_uncertainty` | Which assumptions or method choices remain untested? |

For each slide or build, record only:

| Field | Question |
|---|---|
| `job` | What concrete object can the audience now explain, compare, locate, or decide about? |
| `claim` | What complete judgment should remain? |
| `support` | What visible evidence or explanatory model carries the reasoning? |
| `status` | Fact, observation, interpretation, proposal, proof obligation, result, or boundary? |
| `speaker` | What explanation stays off-screen? |
| `boundary` | What must not be overclaimed or confused? |
| `role` | Anchor, mechanism, evidence, comparison, attack, transition, decision, or conclusion? |

“Understand this page and proceed” is not a page job. Repeated jobs across builds need a distinct visible change or reader inference on every occurrence. The internal `claim` does not dictate the visible title: a short topic, mechanism, or step title may orient better. Do not copy planning rationale, status, or validation reminders onto slides merely because the contract needs them.

Choose visible wording by its job in the live explanation. A concept, structure, or research-map title may name the object, relation, or process with a specific noun phrase; a result page may state a supported finding in a sentence; a process page may name the process while its ordered steps use verbs. A question title is useful when the talk actually resolves that question. The planning `claim` need not become the visible title. Keep diagram entities and states identifiable, and put actions on links or steps when they express the relation. Do not turn every title into “how to…”, an action sentence, or a nominalized abstraction. Preserve a user's requested title form across navigation and main headings; avoid generic “Background/Method/Results” labels that hide the subject. This is the presentation-specific application of `kongyu-writing`'s text-role rule, not a separate rule for prose.

## Scenario references

Load only after the universal derivation identifies the relevant family:

- Speaker-led unfamiliar technical system: [references/teaching-complex-systems.md](references/teaching-complex-systems.md).
- Academic talk, group meeting, thesis defense, paper, or grant briefing: [references/academic.md](references/academic.md).
- General directing and slide contracts: [references/directing.md](references/directing.md).
- Deck review, human-edited version comparison, learning from revisions, prototype gates, rehearsal, or multi-agent review: [references/review.md](references/review.md).
- Visual direction and diagram craft: `kongyu-surface` after the method and page jobs are stable.
- Editable SVG/PPTX production: `ppt-master` after the presentation contract is approved.

## Universal checks

- The selected method is explained by current scenario variables, not habit or borrowed form.
- Every visible entity pays attention rent by supporting the current audience operation.
- The relation the audience must reason about is externally represented in a form suited to that relation; graphics are not mandatory.
- Every prerequisite needed for a judgment is available before or at its point of use; access may be linear or non-linear.
- Evidence language matches epistemic status; explanatory models do not impersonate results.
- Screen, speech, timing, builds, and interaction do not compete for the same attention.
- Density, repetition, variety, titles, animation, and page count are derived choices, not universal targets.
- Each completion claim names the layer actually validated; no proxy closes another layer.

## Completion

Before delivery, perform [review.md § Final-output correction check](references/review.md#final-output-correction-check) on the actual rendered pages. Inventory the title chain and diagram labels by their role: can the audience identify the subject, follow the relation, and distinguish a supported conclusion from an orienting title? For redundancy corrections, apply the deletion test across the deck: name what each questioned sentence adds to this page's inference; technically correct caveats and adjacent captions do not earn space by correctness or placement alone. Report page-specific findings for the applicable prior failure and a legitimate near-neighbor; a source/spec check cannot substitute for this pass. An unresolved explanation failure keeps the affected content unready even when export succeeds.

The director layer is ready for production when the audience capability, method-changing variables, derived method, epistemic boundaries, presentation units, detail split, and validation protocol are coherent enough that an executor need not invent the reasoning.

Report use-state separately when relevant: `artifact-ready`, `presenter-rehearsed`, and `audience-ready`. The evidence required for each is derived from purpose and delivery mode. File export, AI review, title-chain coherence, or source correctness prove only their own layers.
