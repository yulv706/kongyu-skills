# Teaching Unfamiliar Technical Systems

## Derived scenario method

This reference is a method family derived from [principles-and-derivation.md](principles-and-derivation.md), not a universal presentation doctrine. Use it only when the scenario variables indicate a speaker-led or interactive presentation, low or uneven audience familiarity, a technical system whose behavior unfolds through causality or state, and a need to explain rather than merely document.

Do not load it merely because a deck contains technology. Expert design review, result reporting, executive decision, incident coordination, and reading-first documents may derive different spines and validation.

Before applying any practice below, preserve the derivation chain: audience capability → scenario variables → selected method → project-specific practice → validation. Named technologies, local stories, exact page sequences, and attack cases stay in the project contract.

## Why ordinary claim-first directing is insufficient

An assertion title and a coherent title chain can still fail when the listener has not built the objects needed to understand the assertion. “One cognitive job” is also too weak when that job silently requires five new abstractions.

For a proposed system, a diagram is usually an **explanatory model**, not evidence that the system is secure or works. Mark the distinction explicitly:

- observed result or source behavior → evidence;
- proposed mechanism or state machine → explanation of intent;
- proof obligation or experiment → future evidence;
- boundary or counterexample → limit on the claim.

Do not let a clean mechanism diagram upgrade a design claim into a result.

## Choose the teaching spine before constructing pages

There is no universal order for unfamiliar technical systems. Compare these candidates when the choice is material:

- **knowledge-system expansion** — useful when listeners need to learn unfamiliar objects, their structures and processes, and the interfaces between several foundations before judging a combined idea;
- **worked-event replay** — useful when one concrete event exposes the important state changes and can support the intended explanation;
- **attack / failure first** — useful when the audience already recognizes the actors and the main question is why a mechanism is necessary;
- **proof-obligation first** — useful for expert design review, but usually too abstract as a novice opening.

A hybrid may organize chapters by knowledge subjects, use a local worked event to explain each mechanism, and place failures or proof obligations beside the claims they constrain. Another talk may genuinely follow one event throughout. Choose from the audience's missing knowledge and the material's dependencies; neither a single story nor a fixed chapter recipe is a research-proven default.

## Construct the knowledge-system candidate

Use this route when the audience's task is to explain an idea and its foundations, rather than primarily follow an incident or evaluate a known system's result. Keep presentation-specific access structure here; general heading roles and technical explanations belong to `kongyu-writing`.

1. **Establish the knowledge subjects.** For each unfamiliar foundation, explain what it is, what it is for, and which objects it involves. A feature slogan, acronym expansion or list of component names is not a complete introduction.
2. **Build each necessary model.** Explain the structure and one normal operating process before asking listeners to interpret its properties or failure cases. Include the input, operation, output and downstream use needed for the next inference. These are coverage obligations, not one-page-per-item requirements.
3. **Expose the combination interface.** Compare the foundations' inputs, state or object being changed, output purpose and assumptions. Name what the proposal preserves, adapts or replaces. The same word or symbol in two foundations does not establish the same role.
4. **Separate evidence maturity.** Source behavior, an original mechanism, a new proposal, bounded checks and system measurements must remain distinguishable at their point of use.

For a chapter → subsection organization:

- A chapter names a coherent knowledge subject or major reasoning question. Its subsections answer related questions at a comparable level: purpose, architecture, operating process, properties or evaluation, as appropriate to that subject.
- A subsection may contain several pages when they complete one process or related distinction. Split different questions when one label would hide their differences; combine material when a single visible relation carries it clearly. Do not split merely to create another heading.
- Avoid a miscellaneous subsection such as “comparison, limits and next steps” unless these items jointly answer one stated reader question. Give each subsection an informative object, relationship or process name, or a question it actually answers.
- The main title names this page's subject or supported result. The navigation names the actual chapter and subsection, not only a number or the repeated chapter name. Keep the directory and page labels aligned.
- Examples serve their local explanation. Different foundations may need different examples; do not force one incident through unrelated knowledge merely to maintain a story.

### Chapter–subsection–page coverage gate

Before drawing, use the existing presentation contract to map each promised chapter and subsection to its reader question, prerequisite concepts and visible pages. Then inspect the planned explanation in order:

- Can listeners identify the foundation and its purpose before interpreting its mechanism?
- Can they replay a normal process, including the result and its use, before judging a property or attack?
- Is the interface to the combined proposal explicit rather than inferred from shared terminology?
- Does each subsection label cover its pages without concealing a different reader question?
- Does every required introduction or process step appear on screen at the necessary moment? Notes can expand an explanation, but cannot substitute for a missing relation listeners must jointly inspect.

When the user supplies a knowledge order, preserve its dependencies in the actual page sequence. A coverage gap invalidates the affected page contracts; repair those contracts before drawing. Do not close the gap by renaming the old directory, adding a glossary or deleting foundations to meet a page quota.

After export, reconstruct this mapping from the rendered directory, navigation and page content with the planning notes closed. This checks that the intended hierarchy and explanation reached the artifact. It does not establish audience understanding; timed rehearsal and unassisted retelling remain separate evidence.

## Construct the worked-event candidate

When the worked-event route is selected, choose one concrete event that can survive the whole talk: one user, one task, one failure, one recovery attempt, and one observable outcome. Reuse the same actors, labels, and spatial positions.

Teach the system as repeated passes over that event:

1. **Outcome pass:** show only what happened and what must remain true. No internal names.
2. **Mechanism pass:** replay the same event and add only the minimum state needed to explain the next decision.
3. **Adversary pass:** replay the same path with one attacker capability changed; show the first rejection or success point and the final state.

If a page abandons the anchor event for a taxonomy, field list, or unrelated toy example, require a reason. A new example must remove more confusion than the context switch creates. Also keep one concurrency or cross-layer counterexample available: a single event can oversimplify systems whose guarantees do not lift across sessions or layers.

## Concrete → represented → named

For an unfamiliar abstraction whose meaning depends on a concrete distinction, this is a useful introduction sequence:

```text
observable event
→ visible relation or state change
→ short name / symbol
→ reuse of that name in later reasoning
```

Do not begin with an unexplained symbol table. A concise definition may precede a normal event when it gives listeners the names needed to follow that event. An ordinary term or a term immediately explained on a visible object needs no staged reveal.

Before approving a beat, list its prerequisites. If it requires an undefined object, move it later or explain that object before or at its point of use. A definition card alone does not replace the causal model the later reasoning needs.

Treat the research transfer explicitly:

```text
original research task
→ directly supported learning result
→ plausible technical-talk adaptation
→ untested project-specific hypothesis
```

Do not collapse the last two steps into an evidence-backed rule. Pretraining is not “add more background”; segmenting is not “make more slides”; concreteness fading and worked examples are conditional findings, not universal deck recipes.

## Teach foundations as runnable causal models

When the target design combines two or more unfamiliar systems, one definition card per system is usually not enough. A listener cannot reason about the combination until each foundation works as a small causal model in their head.

For every foundation that later carries a design claim, provide only the smallest complete model that lets the listener predict one normal event and one boundary:

1. **Job** — what problem this system already solves;
2. **Actors and state** — which objects persist and which disappear;
3. **One normal event** — how input becomes an observable result;
4. **One boundary** — the tempting inference that is not true;
5. **Handoff question** — the unresolved condition that makes the next system necessary.

This is an existence test, not a five-slide quota. Several items may fit in one slide or build when the relation stays visible. Conversely, a three-item glossary can still fail if the listener cannot replay the event.

For a composition talk, place the interface mismatch before the proposed combination:

```text
foundation A works under assumptions A
+ foundation B works under assumptions B
→ one assumption or object does not map
→ preserve / adapt / replace decision
→ combined mechanism
```

Name which property is preserved, which mechanism is adapted, and which source of security or evidence is replaced. Without this bridge, the audience will either assume the systems compose directly or treat the adaptation as unexplained invention.

Validate foundations with generation, not recognition. Ask the listener to redraw the actors and state, replay the normal event, and predict the boundary without seeing the page. Correctly repeating a definition or acronym is not evidence that the prerequisite model exists.

## Use question–prediction–reveal–consequence beats

A teaching beat is stronger than a page topic or assertion:

Use prediction and reveal where a genuine uncertainty helps teach the mechanism. A definition or structural overview may need a direct explanation with identifiable objects and relations; do not invent a question, quiz or surprise for every subsection.

| Beat field | Required question |
|---|---|
| `question` | What would the listener naturally ask now? |
| `prediction` | What plausible answer or failure should they anticipate? |
| `reveal` | What single visible change resolves the uncertainty? |
| `consequence` | What can they now infer or decide? |
| `new_terms` | Which names became necessary only after the reveal? |
| `off_screen` | Which details belong to speech, notes, appendix, or document? |

Several slides or animation builds may serve one beat. Page count follows visible reveals, not section quotas.

For security design, introduce objections beside the mechanism they test. Do not teach the entire architecture and postpone all attacks until the end. A useful local rhythm is:

```text
problem → proposed invariant → mechanism → immediate attack → surviving boundary
```

## Progressive disclosure is a semantic constraint

Show the objects needed for the current inference. A complete, compact architecture or record table may be necessary to follow one whole path or compare jointly relevant components. It becomes overload when listeners must decode unrelated objects before making that inference. Progressive disclosure does not require animation or removing necessary context. Keep a shared scene when its relations persist; reveal changes when change is the subject.

Prefer:

- builds within one slide when the audience should see the same scene change;
- consecutive slides with identical geometry and one changed state when native builds are impractical;
- dimmed prior state rather than redrawing the whole system;
- before/after pairs for state changes, hierarchies for classifications, and architecture or flow diagrams for system relations; choose the representation by the relation being taught.

Fail the beat when the speaker must first explain the legend, then decode the diagram, then make the point. The visible change itself should carry the point.

## Screen / speech split

Keep on screen:

- the current uncertainty;
- the object or relation that changes;
- labels required to read that change;
- one boundary that prevents the most likely wrong inference.

Keep off screen unless it is the current decision:

- complete protocol fields and state records;
- exhaustive alternatives, threat matrices, and test inventories;
- implementation names before the audience needs them;
- citations that do not constrain the current claim;
- prose that merely repeats what the speaker will say.

## Sequential prototype gate

Representative pages can validate visual range but cannot validate learning continuity. When an independent listener is available, test a short **sequential prototype** covering one complete causal arc, often 4–8 beats in order. If no listener is available, continue building the artifact with `audience-validation: pending`; do not describe it as audience-ready.

To claim a human-tested sequence or audience readiness, the reviewer must see or hear the sequence, not inspect isolated screenshots. Record:

- the human reviewer;
- the exact sequence shown;
- an unassisted retell of the central event and why the design changes it;
- the first loss or wrong inference, even if later repaired;
- terms the reviewer used incorrectly or could not explain.

Before `audience-ready`, add at least one unseen transfer case whose answer was not stated verbatim in the prototype, plus one short-delay reconstruction. For a system talk, useful transfer cases change an attacker capability, remove one prepared state, or cross a layer boundary and ask the listener to predict the result.

AI restatement, title-chain coherence, source correctness, artifact QA, and visual cleanliness cannot satisfy this gate.

Use `scripts/audience_use_gate.py <project-or-evidence-file> --phase full-build` only when the owning project explicitly requires human approval before full production. It accepts either the existing Markdown evidence file or a project directory containing `spec_lock.md`; do not create a second spec merely to satisfy the script. This is not the universal permission to produce an artifact. Use `--phase audience-ready` before claiming audience readiness; without human evidence, deliver the file as `artifact-ready / audience-validation: pending` when its artifact checks pass.

## Completion boundary

A deck may be structurally complete while still being audience-unvalidated. Report those states separately.

- `artifact-ready`: file opens, renders, and contains the intended pages.
- `presenter-rehearsed`: a spoken run exposed timing and explanation failures and they were dispositioned.
- `audience-ready`: a human listener followed the sequential talk, reconstructed the intended model after a short delay, and used it to solve an unseen transfer case.

Do not collapse these into one “done” state.
