---
name: kongyu-code-review
description: "Use for reviewing code changes, diffs, PRs, or commits, and for auditing existing code quality, duplication, slop, or architecture. Not for unresolved pre-build requirements alignment."
---

# Code Review

Hybrid code review skill fusing three engines:

1. **Optional ocr delegate** (alibaba/open-code-review, Apache-2.0) — file selection, rule resolution, diff mode detection. Git and source inspection can provide the review input without OCR; independence requirements still apply to the selected reviewer.
2. **reviewer route** — Controller selects an existing review mechanism by independence requirement, authorization, availability, and read coverage. A bound ChatGPT workspace review may serve when it can read every changed surface; Herdr requires explicit delegation authorization or a higher-priority active policy; Servitor is only for a qualifying structured batch. Low-risk work may use deterministic checks plus controller inspection when maker/checker separation is not required.
3. **structural audit layer** — slop diagnosis and structural/architecture audit on the whole module or file, not just the diff. Evidence-driven taste + 25-dimension checklist.

## Architecture

```
Controller (local agent)
  │
  ├─ Layer A: diff-level review (ocr delegate + selected reviewer route)
  │   1. ocr delegate preview  → file list + mode/ref metadata
  │   2. ocr delegate rule     → rule groups per file
  │   3. git diff/show         → per-file diff text
  │   4. Select by risk + authorization + availability + full read coverage
  │      reviewer input:  diff + rule + review-comment contract
  │      reviewer output: [{path, content, start_line, end_line, category, severity, suggestion_code}, ...]
  │   5. Controller: dedup, classify, merge across workers
  │
  ├─ Layer B: structural audit (slop + 25-dimension)
  │   ├─ Mode 1: slop diagnosis (default, lightweight)
  │   └─ Mode 2: full audit (25-dimension, on explicit request)
  │
  └─ Unified output: line-level findings (Layer A) + scorecard/P0-P2 (Layer B)
```

## Activation

Default: **do not auto-run** on ordinary implementation or small refactors. Call when one of these holds:

- [ ] User asks to review code, review a PR, review changes, review a commit, compare branches, 审代码, 看看这代码有没有问题, CR, code review
- [ ] User asks to audit code quality, find redundancy, diagnose AI slop or shit mountain, 代码审计, 冗余检查, 代码臭味, slop, 重构建议
- [ ] User explicitly asks for review before merge, or an upgrade-path deploy of rewritten/restructured code
- [ ] Cross-module split/move/restructure with observed structural risk (duplicate definitions, re-export bloat, mixed-concern files) and local checks cannot cover that risk
- [ ] A single touched file exceeds ~500 lines and mixes concerns, or exceeds ~1000 lines and split is under consideration

Do **not** call for:
- [ ] Ordinary multi-file feature work or local refactors that already pass their verification target
- [ ] "About to declare done after any refactoring commit" by itself
- [ ] Pure text/docs/config edits with no structural code surface

## Input gate

Before reviewing, identify the repository root, review target (working tree,
commit, or branch range), and requested depth (diff, structural audit, or
both). If the target is not explicit, inspect status read-only and ask one
focused question rather than inventing a comparison. A finding is admissible
only with a file/line or concrete runtime/static evidence; unsupported style
preferences are not defects.

Tests passing is not structural quality; when you do review, look for defects tests miss.

## Optional OCR input preparation

Use OCR when it adds useful file selection or project-rule resolution. Otherwise
identify the target using Git, read the applicable project rules and source,
and proceed to Step 4. Steps 1–3 below describe the OCR route only.

```powershell
# Resolve the installed OCR executable and record its path.
Get-Command ocr
ocr --version

# ocr delegate mode needs no LLM endpoint — verify CLI works:
ocr delegate preview --repo <repo-path>
```

For Bash, use the equivalent explicitly labelled commands:

```bash
command -v ocr
ocr --version
ocr delegate preview --repo <repo-path>
```

On first use of an OCR installation or after its executable/package changes, verify and record the resolved executable path, the full
`ocr --version` output (including build/source details when present), and the
package/source provenance. For an npm installation, inspect both the installed
package and the registry metadata, then compare the package name, version,
registry/source, and integrity with the approved source; a version string alone
is not provenance proof:

```powershell
npm ls --global --depth=0 @alibaba-group/open-code-review
npm view @alibaba-group/open-code-review version repository.url dist.integrity
```

If `ocr` is missing or its provenance/version does not match, do not run it.
Use Git, applicable project rules, and source inspection instead; report any
coverage gap. Stop only if a required rule or independent review cannot be
satisfied by the available authorized route. A global install requires explicit user approval
for this package, its global scope, and its source/registry before running:

```powershell
npm install --global @alibaba-group/open-code-review
```

Check only the reviewer route selected for this task. For an authorized Herdr route:
```powershell
herdr integration status
herdr agent list
```
If and only if the review uses the structured batch route, verify:
```powershell
servitor inspect capabilities
```

## Layer A: Diff-Level Review (ocr delegate + isolated reviewer)

### Step 1: Preview — determine what to review

```powershell
# Workspace changes (staged + unstaged + untracked)
ocr delegate preview --repo <repo-path>

# Branch comparison
ocr delegate preview --from main --to <branch> --repo <repo-path>

# Single commit
ocr delegate preview -c <commit-hash> --repo <repo-path>
```

Output gives: mode (workspace/range/commit), from/to/merge_base refs, reviewable file list (paths, status, insertions/deletions), excluded files.

Pass business context when available:
```powershell
ocr delegate preview -b "business context here" --repo <repo-path>
```

### Step 2: Get rules for files

```powershell
ocr delegate rule <path1> <path2> ... --repo <repo-path>
# Preview which rule applies to a single file:
ocr rules check src/main/java/com/example/Foo.java
```

Output is grouped by rule content — files sharing the same rule appear under one group. Custom rules resolve in priority:
1. `--rule <path>` flag (highest)
2. `<repo>/.opencodereview/rule.json`
3. `~/.opencodereview/rule.json`
4. Built-in system defaults (lowest)

First matching user rule replaces built-in; set `merge_system_rule: true` to include both. Rule file format:

```json
{
  "rules": [
    {
      "path": "**/*.java",
      "rule": "All new methods must validate required parameters for null",
      "merge_system_rule": true
    },
    {
      "path": "**/*mapper*.xml",
      "rule": "Check SQL for injection risks and missing closing tags"
    }
  ]
}
```

### Step 3: Get diffs

Use git directly based on mode/ref from Step 1:

**Range mode** (merge_base from preview):
```powershell
git diff <merge_base>..<to> -- <path>
```

**Commit mode**:
```powershell
git show <commit> -- <path>
```

**Workspace mode**:
```powershell
# Tracked files
git diff HEAD -- <path>
# New untracked files — read directly (entire file is new code)
Get-Content <path>
```

### Step 4: Select and run the reviewer route

Record `independence_required`, authorization basis, changed surfaces, readable
coverage, exclusions, selected mechanism, and expected evidence before invoking
a reviewer. Use the smallest route that satisfies the contract:

| Condition | Route |
| --- | --- |
| A verified Codex-with-ChatGPT workspace binding can read every changed surface | Use that independent workspace review; keep local execution ownership. |
| The user explicitly requested/authorized a session-bearing reviewer, or a higher-priority active policy requires it | Create a fresh read-only Herdr reviewer session; record caller/return identity and wait for its terminal event. |
| 3+ independent homogeneous files/rule groups require schema-validated aggregation and that execution is authorized | Use the Servitor structured batch exception below. |
| Low-risk change and maker/checker separation is not required | Use relevant project checks plus controller inspection, with optional OCR; label it deterministic/controller review, not independent review. |
| Independent review is required but no authorized mechanism can read every changed surface | Stop with `needs_authorization_or_coverage`; do not silently self-certify or dispatch an unauthorized agent. |

Use one reviewer for files that need the same mental model. Do not fan out per
file merely because several paths changed. Pass file paths and precise diff/rule
excerpts rather than session history, and never expose secrets or credentials.

**Structured batch exception:** when there are 3+ independent homogeneous files
or rule groups and the controller needs schema-validated machine aggregation,
use Servitor workflow `parallel()` with one `agent({schema})` per independent
unit. This is a non-session batch engine, not the owner of reviewer identity or
callbacks. See [references/servitor-batch-config.md](references/servitor-batch-config.md).

Both routes use this reviewer contract:

```text
Review the supplied diff under the supplied rule. Return only a JSON array.
Each finding: {path, content, start_line, end_line, category, severity,
suggestion_code?}. Return [] when no supported finding exists.
```

The controller verifies every finding against current source before reporting.

When authorized reviewers cover interacting components, apply
[collaborative synthesis](references/code-reviewer.md#collaborative-synthesis)
before consolidating their findings. Reconstruct the affected behavior from
component contracts and evidence; inspect consequential disagreements at their
source. This does not require additional reviewers or change the JSON contract.

### Step 5: Controller synthesis

After all workers return:

1. Collect all findings from all worker results
2. Dedup overlapping findings (same path + overlapping line range + similar content)
3. Classify by severity:
   - **Critical/High**: bugs, security issues, data loss risks — always report
   - **Medium**: performance concerns, error handling gaps, maintainability — report with context
   - **Low**: style nits, minor suggestions — report only if clearly valuable
4. Discard likely false positives silently (insufficient context, meaningless suggestions)
5. For mispositioned comments (start_line=0, end_line=0): read file, locate relevant section, fix line numbers

### Step 6: Fix (optional)

If user requested "review and fix":
- Apply Critical/High fixes directly when safe and well-defined
- Describe Medium fixes that require manual intervention
- Skip Low-priority items unless trivial
- Always verify fixes before committing

**Evidence-based remediation:** prioritize behavioral defects by risk and use a reproducer or regression test when it can meaningfully detect the defect. Prefer demonstrating the failure before the fix when practical. Independent fixes may be batched and verified with the affected tests together. For findings better verified by static, structural, or visual inspection, use that evidence rather than inventing a test. Reuse still-valid failure evidence; rerun affected checks after changes, not merely to obtain a new red→green pair in the current turn.

## Layer B: structural audit (slop + 25-dimension)

Run Layer B when the user asks for a thorough/comprehensive audit, or when Layer A reveals structural patterns (repeated slop, architecture drift) that need whole-module diagnosis.

- **Mode 1: Slop Diagnosis** (default, lightweight) — diagnose AI slop taste: code that feels generated, over-expanded, fallback-heavy, state-foggy.
- **Mode 2: Full Audit** (when user asks for thorough/comprehensive audit) — pick relevant dimensions based on project type; do not run all mechanically.

For both modes read [references/audit-dimensions.md](references/audit-dimensions.md): slop trait checklist, audit workflow, scoring rubric, 25-dimension checklist, and the Audit Verdict output template.

**HARD gate:** any category scored 5 blocks clean status.

## Review Workflow (requesting / receiving)

### Requesting Review

Choose a review route that can catch issues before they cascade. The reviewer gets precisely crafted context for evaluation, never unrelated session history.

When to request:
- After completing a major feature or task
- Before merge to main
- When stuck (fresh perspective)
- After fixing a complex bug

How to request:
1. Get git SHAs. In PowerShell:
   ```powershell
   $baseSha = git rev-parse HEAD~1
   $headSha = git rev-parse HEAD
   ```
   In Bash:
   ```bash
   BASE_SHA=$(git rev-parse HEAD~1)
   HEAD_SHA=$(git rev-parse HEAD)
   ```
2. Apply the Step 4 decision table. When Herdr is the authorized route, use [references/code-reviewer.md](references/code-reviewer.md); use Servitor only for a qualifying structured batch
3. Act on feedback: fix Critical immediately, fix Important before proceeding, note Minor for later, push back if reviewer is wrong

### Receiving Review

Verify before implementing; technical correctness over social comfort. Never respond with performative agreement ("You are absolutely right!", "Great point!"). Full response pattern and pushback etiquette: [references/code-reviewer.md](references/code-reviewer.md).

## Unified Output Format

### Layer A: Line-Level Findings

```markdown
## Code Review Results

**Files reviewed**: N
**Issues found**: X critical/high / Y medium

### Critical / High

- **`path/to/file.java:42`** — Brief description
  > Recommendation: How to fix

### Medium

- **`path/to/file.ts:88`** — Brief description
  > Recommendation: How to fix (if applicable)
```

If no issues after filtering: "Review complete — no issues found in N files."

### Layer B: Structural Audit (when run)

Use the Audit Verdict template (scorecard, P0-P2 findings, refactoring priority, dead-code summary) in [references/audit-dimensions.md](references/audit-dimensions.md).

## Gotchas

- **ocr delegate needs no LLM endpoint** — review intelligence comes from the isolated reviewer route. Never configure `OCR_LLM_URL`/`OCR_LLM_TOKEN` for delegate mode.
- **Working directory matters** — `ocr delegate` operates on the Git repo at current directory. Use `--repo /path/to/repo` to override.
- **Untracked files in workspace mode** — `preview` includes untracked files. For these, read the file directly instead of `git diff`.
- **Large diffs may hit token limits** — for very large diffs, split per-file or truncate with a note. Consider `--exclude` for generated/vendored files.
- **Batch dispatch discipline (karma #513)**: only enter the Servitor batch route for 3+ independent homogeneous units requiring schema aggregation. Use one backend consistently rather than mixing pi/codex/codebuddy in the same batch. Keep per-worker prompts under 10KB; split large diffs into hunks. Mixing backends in one batch causes inconsistent review quality and partial failures.
- **Herdr session discipline**: when Herdr is explicitly selected and authorized, use a fresh isolated reviewer session and return to the recorded caller. Do not reuse an unrelated reviewer or infer the caller from recent panes.
- **Coverage is semantic, not path-counting**: a reviewer that cannot read a global skill, generated artifact, live UI, or another repository does not cover that surface. Record the exclusion and use another authorized proof or stop when independence is required.
- **Workers must output ONLY raw JSON** — no prose, no code fence. schema validation in `agent({ schema })` will flag wraps as a schema error; tighten the prompt, don't retry blindly.
- **Comment language follows config** — set `language` to `English` or `Chinese` (default: Chinese). State the language explicitly in either reviewer route.
- **Controller owns final truth** — verify worker findings against codebase before reporting; reject unsupported claims.

## Rules

- [ ] Evidence first: every finding needs file path + line number or function name
- [ ] Delete before refactor before new abstraction
- [ ] Do not suggest new abstractions for code that should just be deleted
- [ ] Do not audit what you cannot read; mark excluded items explicitly
- [ ] One finding per line; do not write paragraphs
- [ ] Slop is a taste diagnosis, not an authorship claim
- [ ] Controller verifies completion; delegated workers do not self-grade

## References

- [audit-dimensions.md](references/audit-dimensions.md) — Layer B structural audit: slop traits, workflow, scoring rubric, 25-dimension checklist, verdict template
- [code-reviewer.md](references/code-reviewer.md) — subagent review prompt template + receiving-review response pattern
- [servitor-batch-config.md](references/servitor-batch-config.md) — optional structured batch route for 3+ homogeneous review units
- OCR installation is approval-gated; verify package/source provenance before use. Official source: https://github.com/alibaba/open-code-review
