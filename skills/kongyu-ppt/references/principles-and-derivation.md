# Presentation Principles and Scenario Derivation

This reference separates what should remain true across presentations from the methods and practices that should change with the situation.

```text
principles
→ scenario variables
→ derived method
→ concrete practices
→ purpose-matched validation
```

A principle constrains judgment. A method organizes work for a class of situations. A practice is a concrete move in one presentation. Do not promote a successful practice into a principle merely because it worked once.

## Universal principles

### 1. Optimize for audience change

The object of a presentation is a change in what the audience can understand, decide, predict, remember, or do under real time and attention constraints. Coverage, page count, visual polish, and file quality are subordinate.

### 2. Preserve the audience's limited attention

Every visible or spoken entity consumes attention. Keep an entity only when it helps the audience select, organize, integrate, inspect, or act on the current idea. “Less” is not the goal; coherent use of attention is.

### 3. Externally represent the necessary relation

The key relation the audience must reason about should be externally represented rather than left entirely in working memory. Choose the form from that relation—causality, time, state, comparison, quantity, hierarchy, space, responsibility, uncertainty, or authority. The representation may be a diagram, table, structured statement, formula, quotation, timeline, matrix, demonstration, or another inspectable form; no medium is universally required.

### 4. Make information access satisfy dependency constraints

Any prerequisite required for a judgment must be available before or at the point of use. This is a dependency constraint, not a mandatory story order: a presentation may be prerequisite-first, conclusion-first, result-first, threat-first, chronology-first, branchable, or non-linear when the audience and delivery mode support it. Source order, organization charts, section quotas, and template page types do not determine access.

### 5. Match language to epistemic status

Keep observations, source facts, interpretations, proposals, proof obligations, boundaries, and measured results distinct. A clear model explains; it becomes evidence only when the claim and evidence type warrant that role.

### 6. Orchestrate screen, speech, and time as one system

The screen, the speaker, builds, transitions, pauses, and audience interaction share one communication budget. Do not evaluate slides as static documents when their job depends on timing, narration, or live inspection.

### 7. Let feedback match the intended outcome

Validation must observe the audience capability named in the objective. Visual inspection validates attention and craft; source review validates fidelity; rehearsal validates delivery; recall, explanation, prediction, decision, or transfer tasks validate different audience changes. No proxy closes a different layer.

### 8. Derive the form; do not universalize a recipe

There is no universally correct spine, page density, slide count, title style, visual grammar, animation strategy, or review ritual. The chosen method must be explainable from the current scenario variables and remain replaceable when feedback contradicts it.

## Scenario variables

Capture only variables that change the method:

| Variable | Questions |
|---|---|
| Purpose | Teach, persuade, defend, decide, report results, coordinate action, or support later reading? |
| Audience state | What do they already know, confuse, resist, or care about? How heterogeneous is prior knowledge? |
| Evidence maturity | Observed result, established source, proposed design, hypothesis, or unresolved question? |
| Content topology | Event/process, causal mechanism, comparison, dataset, decision, hierarchy, state machine, proof, or portfolio? |
| Delivery mode | Speaker-led, reading-first, hybrid, interactive workshop, demo, or asynchronous review? |
| Time and control | Fixed slot, user-paced, presenter-paced, interruptible, or discussion-heavy? |
| Consequence of misunderstanding | Cosmetic confusion, wrong decision, unsafe action, invalid scientific claim, or implementation risk? |
| Available evidence | Figures, measurements, source text, code behavior, examples, counterexamples, simulations, or only a proposal? |

Do not collect variables that do not change a choice. A detailed audience persona, long requirements form, or style taxonomy that leaves the method unchanged is ceremony.

## Derivation

### Step 1. Name the audience capability

Write one observable end state: what should the audience be able to explain, decide, predict, compare, or do? Avoid “understand the topic” and “know the architecture.”

### Step 2. Identify the dominant reasoning task

Ask what operation produces that capability:

| Reasoning task | Candidate spine families |
|---|---|
| Follow change through time | event replay, chronology, state transition |
| Understand why a mechanism exists | problem–failure–mechanism, worked example, counterexample |
| Judge a claim | assertion–evidence, argument–objection–boundary |
| Compare alternatives | common-axis comparison, trade-off, decision tree |
| Review an unimplemented design | proof obligations, attack path, invariant and failure analysis |
| Act or coordinate | current state, decision, owner, next action |
| Learn a procedure | demonstration, worked example, guided practice, fading |

These are candidates, not prescriptions. Combine only when each family pays distinct rent.

### Step 3. Choose the abstraction ramp

Use audience prior knowledge and content topology to decide whether the sequence should move from concrete to abstract, abstract to concrete, overview to detail, failure to mechanism, or claim to evidence. Preserve mappings between representations so that a change of abstraction does not force the audience to rebuild the world.

### Step 4. Choose the presentation unit

The unit may be a slide, build, animation step, demonstration action, spoken question, or pause. Bound it by one audience inference or decision, not by a fixed amount of text. Keep prior state visible when later reasoning depends on it.

### Step 5. Divide screen, speech, and detail layers

Place on screen what must be jointly inspected now. Put explanation, nuance, and transitions in speech. Put exhaustive fields, citations, alternatives, and audit detail in notes, appendix, or a separate document unless they are the current object of judgment.

### Step 6. Derive visual grammar and rhythm

Use the chosen reasoning tasks to determine page families and visual continuity. Repetition is useful when it preserves a mental model; variation is useful when the reasoning task changes. Neither sameness nor variety is a goal by itself.

### Step 7. Derive the validation protocol

Choose checks from the intended audience capability and delivery mode. A decision deck may require choice consistency; a teaching talk may require explanation and transfer; a design review may require finding a violated invariant; a reading document may require unaided navigation and source traceability.

### Step 8. Keep claims proportional to evidence

Passing one prototype supports only the tested version, audience, task, and conditions. Comparative superiority requires comparable alternatives and the same outcome measures. Do not turn one successful use into a universal method rule.

## Derivation examples

These examples demonstrate different outputs from the same principles. They are not templates.

| Scenario | Variable signature | Plausible derived method and practices | Purpose-matched validation |
|---|---|---|---|
| Novice teaching | low prior knowledge; causal or procedural content; speaker-led; misunderstanding blocks later learning | prerequisite model, segmented worked example or demonstration, coordinated visuals and speech, guided explanation, later fading | explanation, delayed reconstruction, and transfer to an unseen case |
| Expert design review | high domain knowledge; proposed design; high cost of hidden failure; discussion-heavy | threat or invariant framing, proof obligations, attack/counterexample paths, alternatives and boundaries near claims | reviewers find violated assumptions, distinguish evidence status, and make a defensible go/change/stop decision |
| Academic results | domain-literate audience; measured evidence; fixed slot; claims must remain traceable | research question or central finding, interpreted figures, alternative explanations, limitations before conclusion | claim-to-source traceability, correct result interpretation, objection handling, timed rehearsal |
| Executive decision | heterogeneous knowledge; choice required; limited time; consequences matter more than mechanism completeness | decision first, common-axis options, material trade-offs, reversibility, recommendation and action | decision consistency, ability to state the governing trade-off, owner and next action clarity |
| Incident or operations review | shared operational context; temporal evidence; responsibility and recovery matter | timeline, observed state transitions, causal fork, containment/recovery actions, owner boundaries | participants can identify trigger, state change, current risk, owner, and next safe action |
| Reading-first document | no speaker; reader controls pace; future retrieval and traceability matter | layered summary, navigation, local definitions, denser tables where comparison requires them, expandable detail and sources | unaided navigation, question answering, source lookup, and correct interpretation without narration |

If two rows produce the same method, the scenario variables were probably too vague or the derivation is being replaced by a preferred recipe.

## Scenario-family routing

After derivation, load only the relevant scenario reference:

| Scenario family | Derived emphasis | Reference |
|---|---|---|
| Speaker-led unfamiliar technical system | prerequisite model, causal segmentation, worked-example or failure candidates, sequential human test | [teaching-complex-systems.md](teaching-complex-systems.md) |
| Academic talk or research defense | claim/source discipline, result interpretation, objections, limitations | [academic.md](academic.md) |
| Deck review and real-use validation | failure-layer separation, visual/readback checks, rehearsal and audience evidence | [review.md](review.md) |
| General story and slide contracts | ending, question chain, slide jobs, screen/speech split | [directing.md](directing.md) |

Project-specific stories, named technologies, local attack cases, page sequences, and validation questions belong in the owning project's presentation contract or research artifact, not in this universal reference.

## Derived-method output

Before page production, record the smallest useful chain:

```text
audience capability:
scenario variables that changed the method:
selected method family or combination:
why each selected component is needed:
rejected plausible alternatives:
abstraction ramp:
screen / speech / detail split:
validation matched to the purpose:
project-specific practices:
known uncertainty:
```

This chain is an explanation of why the method fits. It is not a second specification schema and need not become a new file when the existing project contract can carry it.

## Boundary

This reference owns universal presentation principles and the derivation interface. Scenario tactics belong to the routed references. Visual styling belongs to `kongyu-surface`; artifact construction belongs to `ppt-master`; domain truth and project-specific methods remain with their owning project and evidence sources.
