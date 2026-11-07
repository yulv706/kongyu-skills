# Presentation Directing

Use this reference when the deck's reasoning path, sequence, or slide meaning is still being created or repaired. Its linear argument tactics apply to speaker-led argument decks; reading-first, reference, map, and branchable decks use the access structure derived in `principles-and-derivation.md`.

## Start from the audience, not the source

Write three sentences:

1. **Before:** what the audience already knows, assumes, or is likely to confuse.
2. **After:** what they should be able to explain, believe, compare, or decide.
3. **Resistance:** the strongest reasonable question that could prevent that change.

The source document supplies facts. It does not supply the order of attention. Organize around the audience's next question. Background deserves only the space needed to make the main claim evaluable.

## Write the ending first

Draft the final slide before the outline. It should contain:

- the smallest defensible conclusion;
- the consequence or decision it enables;
- the boundary that prevents overclaiming;
- the discussion question or next action, when one exists.

If this requires a paragraph, the argument is not yet sharp enough. Do not hide unresolved choices in a long agenda.

## Build a question-to-answer spine

A useful spine is a chain of cognitive states:

```text
current belief
→ new problem or contradiction
→ governing principle
→ mechanism or evidence
→ objection / attack
→ bounded conclusion
```

The exact structure depends on the task. Do not force Situation–Complication–Resolution, chronology, or a standard paper outline when the audience's questions imply another order.

For a linear speaker-led argument, read the titles alone to check whether each step prepares the next judgment. In a reading-first, map, reference, or branchable deck, use titles to test navigation, category boundaries, and retrieval instead; pages need not be ordered as one unavoidable chain. A movable page is a problem only when the selected access structure depends on its current position.

## One slide = one cognitive change

The unit is not “one topic” or “one bullet list.” It is the sentence the audience can now say that they could not say before.

This rule is not a complexity waiver. Before using it, ask which objects and relations the listener must already understand. If the slide's “one change” requires several new terms, a legend, and a paragraph of decoding, split the learning sequence or return to a concrete event. For unfamiliar technical systems, use [teaching-complex-systems.md](teaching-complex-systems.md).

Good slide contract:

```text
job: distinguish session lifetime from connection lifetime
claim: the Bash process must outlive every transport connection
evidence: one lifecycle diagram with three aligned timelines
speaker: explain the reconnect example and implementation owner
boundary: persistence does not imply authentication or recovery from process death
role: mechanism
```

Several annotations, labels, or examples may share a slide when they all support that claim. Conversely, several short cards still create several cognitive jobs when each points in a different direction.

## Assertion and visible evidence

When a page asks the audience to accept a result or judgment, use a supported complete claim as its title or dominant statement. Concept, structure, research-map, and process pages may instead use specific names that orient the audience; ordered steps use verbs. Pair the current page's claim or named relation with the smallest visible object that carries the reasoning:

- time or causality → sequence, timeline, state transition;
- system responsibility → architecture or ownership map;
- comparison → aligned table, slope, before/after, common axis;
- attack or failure → capability path with the first failed gate;
- quantity → chart with the conclusion annotated at the relevant mark;
- proof or protocol → minimal equation, message sequence, invariant, or counterexample.

Call that object **evidence** only when it is an observed/source result or a valid argument for the claim. A proposed architecture, KDF, state machine, or test plan is usually an explanatory model or proof obligation; it cannot establish that the system is secure merely because it is drawn clearly.

If deleting the visual does not weaken the argument, it is decoration. If the visual needs a paragraph elsewhere to decode it, the evidence and explanation are too far apart.

Research basis: [Assertion–Evidence](https://www.assertion-evidence.org/), Mayer's coherence/signaling/spatial-contiguity principles, and presentation-generation work such as [PPTAgent](https://aclanthology.org/2025.emnlp-main.728/).

## Live deck and leave-behind

For a speaker-led presentation, keep on screen:

- the current claim;
- the evidence the audience must inspect now;
- labels needed to decode that evidence;
- the minimum boundary needed to prevent a wrong inference.

Move definitions, exhaustive matrices, field lists, full citations, alternatives, and failure branches to speaker notes, appendix, or a separate reading document unless they are the current point.

A hybrid deck still needs a primary mode. Do not make every slide self-sufficient by turning it into a report page.

## Rhythm is semantic

Choose composition from page role, not from a default template:

| Role | First visual question |
|---|---|
| Anchor | What single situation or claim should stop the room? |
| Mechanism | What changes, moves, or hands off? |
| Evidence | What should the audience inspect? |
| Comparison | What must be aligned to compare fairly? |
| Attack / objection | What capability is gained and where does it stop? |
| Transition | What question has been answered and what becomes necessary next? |
| Conclusion | What remains true, and under what boundary? |

Consistency comes from shared visual language. Repeating one composition for every role destroys semantic difference.

## Representative prototypes

Prototype once the selected reasoning/access structure is stable. Select real-content pages that stress different jobs—for a speaker-led argument, these may include an opening anchor, mechanism, evidence, objection, and conclusion. Three may be enough; five is not a quota. Test a short causal sequence in order when the talk depends on one; for a reading-first or branchable deck, test a real lookup, comparison, or branch path. Isolated representative pages cannot prove that the chosen path works.

Approve the system only when:

- each page has one unmistakable visual subject;
- the title and visual support the same audience inference or decision;
- the pages feel like one talk without sharing one composition;
- the dense case remains readable without shrinking into document typography;
- the system can expand without inventing a card for every paragraph.

## Boundary

This reference owns story and slide semantics. Visual tokens and page craft belong to `kongyu-surface`; editable PowerPoint/SVG implementation belongs to `ppt-master`; domain truth remains with the relevant source/domain skill.
