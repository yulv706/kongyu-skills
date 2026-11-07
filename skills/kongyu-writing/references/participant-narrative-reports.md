# Participant-Narrative Reports

Use the full gate for participant-facing retrospectives or insight reports built from session history, personal material, interviews, or lived experience, when the task asks for discoveries about relationships, mechanisms, turns, or contradictions. For a simple interview tidy-up, chronology, transcript edit, or personal prose polish, use only the information-horizon, source-fidelity, and machine-identifier boundaries below; do not require discovery work. The participant is a reader inside the events, not an outside analyst's camera.

## Coverage and discovery ledgers

For a retrospective or insight report, read the primary source artifacts named by the task or project rather than reconstructing them from conversation memory, a final verdict, or a later summary. Build two linked records before outlining:

1. A coverage ledger that preserves each phase, conditional positive, negative result, turning point, and unresolved boundary.
2. A discovery ledger in which every candidate insight states: a question or problem the participants may not have named; exact evidence; a new relationship, turning point, mechanism, contradiction, or boundary; counterevidence or an alternative explanation; and confidence or uncertainty.

Reject a discovery candidate that merely rearranges the same material by person, time, or topic, or replaces concrete evidence with an abstract label. Reindexing and renaming are organization, not discovery. In an insight report, each main chapter must map to at least one candidate that passed the discovery gate. A faithful digest or chronology may instead use natural time, person, or topic divisions without claiming a discovery.

## Information horizon

Write from the participant's information horizon rather than an outside analyst's camera:

```text
what was visible then -> how it was understood then -> what new reference appeared later -> how the old experience changes in that light -> what remains uncertain
```

Start from concrete scenes and ordinary narrative grammar, and organize around qualified relationships, turning points, mechanisms, contradictions, or boundaries. karma #362/#365.

## Title and opening stance

Title and opening are part of stance, not decoration. Title the report — and each chapter — by the change or problem being explained, not by a retrospective mood, preset epiphany, or soft conclusion the reader is assumed to share; reject titles that sigh for the participant or pre-sell discovery. The first paragraph enters a concrete lived situation immediately and never opens by explaining camera, viewpoint, method, report design, or how the writing works. Before delivery, check that title promise, first-paragraph landing, and narrative person agree.

## Machine-identifier scrubbing

Keep discovery evidence traceable in the agent source layer, but do not make the participant read the audit machinery. Message IDs, episode IDs, run names, row/line numbers, confidence fields, and similar machine provenance stay in a separate verification layer; the source layer may retain exact provenance and confidence fields. The participant-facing body uses human-readable scenes, dates only when useful, and ordinary references.

## Audit language that leaks into the reader layer

Machine-identifier scrubbing is not enough. Several audit registers pass the ID test and still read as an internal log. Move them to an appendix or delete them:

| Reader layer leaks | Put in appendix / write as |
| --- | --- |
| sample size, field names, extraction rules | one sentence on scope, or an appendix section |
| error counts of one's own analysis ("439 quotes checked, 13 misattributed") | appendix, framed as what was overturned |
| analyst nouns (agent, subagent, prompt, pass, run) | drop; name only what the reader can act on |
| taxonomy labels used as headings ("coverage ledger", "boundary ruled in/out") | name the change or the problem instead |
| "this method cannot answer X" | say "the record cannot show X" in the scene's own terms |
| standing schema words used mid-prose ("material cannot determine") | one plain sentence per case |

Two tests before delivery. Run the gate, then read for person directly:

```bash
python scripts/check_reader_layer.py <md-or-html> [--json]
```

The gate greps for the register terms above plus third-person names in a second-person body (inline code is exempt, so quoted messages do not trip it). Blocking findings must move to an appendix or be rewritten; warnings are judgement calls. **Do not delete the underlying claim to satisfy the gate** -- an appendix carrying method and error counts is its intended home. The gate exists because it found register phrases a careful manual pass had already declared clean.

Then read for person: **the body must use one narrative person throughout.** A draft that opens in second person and reverts to third-person names in the evidence sections reads as two documents stitched together, and bulk name replacement is not the fix — it silently corrupts quoted messages (a participant's own nickname or stage name inside a quote is not a third-party reference). Replace inside quotes only after checking the original row.

## Conclusions and the faithful-digest fallback

A later conclusion may organize qualified discoveries but must not relabel conditional findings as failures or erase earlier paths for narrative cleanliness; it also must not outrun the evidence. Abstract labels and person/time/topic reindexing do not count as findings; when no candidate survives evidence and counterevidence, present the result as a faithful digest or chronology rather than an insight report. If any required source is unavailable or unread, mark the report partial and name the gap instead of presenting a complete storyline. karma #327/#368/#369/#370.
