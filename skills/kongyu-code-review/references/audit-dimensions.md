# Structural Audit (Layer B)

Layer B reference: slop trait checklist, audit workflow, scoring rubric, 25-dimension checklist for Mode 2, and the Audit Verdict output template.

## Mode 1: Slop Diagnosis — Strong Slop Traits

Diagnose AI slop taste: code that feels generated, over-expanded, fallback-heavy, state-foggy.

Strong slop traits:
- [ ] Surplus nouns: Gateway, Control Plane, Runtime, Provider, Capability, Harness, Pipeline where a single function would do
- [ ] Fallback hydra: every failure path adds another retry, resolver, compatibility shim, legacy alias
- [ ] State fog: nullable ids, boolean flags, maps, timers, pending/finalized/completed sets, duplicated sources of truth
- [ ] Dead code paths: hardcoded booleans making entire branches unreachable
- [ ] Duplicate logic: same algorithm implemented N times with slight variations (different timeout, different error handling)
- [ ] Stringly lifecycle: event names, phases, run ids composed from strings and normalized repeatedly
- [ ] Adapter lace: thin modules rename fields, coerce strings, normalize ids, hide boundary uncertainty
- [ ] Control-plane fetish: internal plumbing becomes the product surface

## Mode 2: Full Audit — 25 Dimensions

- [ ] Pick relevant subset based on project type

| Dimension | What to check |
|---|---|
| architecture | boundary ownership, dependency direction, state ownership |
| security | auth, injection, secrets, dependencies |
| stability | panic paths, error handling, concurrency, lifecycle |
| performance | hot paths, memory, I/O, startup cost |
| testing | coverage, test types, fragility |
| maintainability | complexity, coupling, duplication, naming |
| design | engineering principles, design risk |
| release | CI/CD, versioning, rollback |
| documentation | accuracy, setup, ops guide |
| observability | logs, metrics, tracing, health checks |
| configuration | validation, defaults, env isolation |
| data-integrity | transactions, idempotency, migration |
| fallback | silent degrade, empty catch, defensive guess |
| dead-code | unreachable branches, hardcoded flags, obsolete paths |
| duplicate-logic | same algorithm N times, inconsistent timeout/error handling |
| state-fog | nullable ids, boolean flags, maps, timers, pending/finalized sets |
| naming | surplus nouns, generic verbs, inconsistent conventions |
| coupling | god files, cross-layer mutation, circular dependencies |
| error-handling | swallowed exceptions, generic catch, missing retry classification |
| resource-lifecycle | unclosed connections, leaked file handles, orphaned processes |
| type-safety | unsafe blocks, type assertions, boundary types |
| frontend-state | component size, state duplication, side effects |
| api-consistency | API contract, validation, N+1, data flow |
| dependency-weight | heavy deps, build toolchain bloat |
| comment-coverage | doc quality, stale comments, missing docs |

### Selection Guide

- [ ] Python service: architecture, stability, maintainability, fallback, dead-code, duplicate-logic, error-handling, resource-lifecycle
- [ ] Frontend app: architecture, state-fog, frontend-state, naming, coupling, dead-code
- [ ] CLI tool: stability, error-handling, configuration, dependency-weight
- [ ] Worker/queue system: stability, fallback, dead-code, duplicate-logic, resource-lifecycle, error-handling

## Audit Workflow

- [ ] Map user flows: name 1-3 primary flows, trace entrypoint to storage to UI
- [ ] Locate ownership: single owner for each state/resource; mark duplicated owners
- [ ] Inspect state shape: parallel booleans, nullable ids, maps, timers, pending/final/fallback triplets
- [ ] Inspect fallback shape: classify each as product contract / migration / compatibility / retry / paper-over
- [ ] Find dead code: hardcoded booleans, unreachable branches, functions that return constants
- [ ] Find duplicate logic: same operation implemented multiple times with slight variations
- [ ] Inspect tests: good tests prove primary flow; slop tests encode internal maps and fake backends
- [ ] Produce scorecard: evidence with file paths, line numbers, concrete snippets

## Scoring Rubric

Rate each category 0-5:
- 0: Sharp. Direct, owned, typed, user-flow-first
- 1: Pragmatic. Some adapters with clear contracts
- 2: Slight slop. Minor naming sheen, manageable state
- 3: Visible slop. Generic nouns, growing flags, unclear ownership
- 4: God surfaces, fallback hydra, session fog, dead code
- 5: Slopmax. The whole module is plumbing for its own sake

Any category at 5 is a blocker for clean status.

## Audit Verdict Output Template

```
## Audit Verdict: [Clean / Slight Slop / Visible Slop / Heavy Slop]

### Scorecard
| Category | Score | Key Evidence |
|---|---|---|
| ... | 0-5 | file:line, snippet |

### Critical Findings (P0)
- [P0] description -- file:line -- fix recommendation

### Should Fix (P1)
- [P1] description -- file:line -- fix recommendation

### Nice to Fix (P2)
- [P2] description -- file:line -- fix recommendation

### Refactoring Priority
1. First thing to delete/merge
2. Second thing
3. Third thing

### Dead Code Summary
- function/branch -- why dead -- safe to delete?
```
