# Optional Structured Review Batch — Servitor v0.2.0

Select this Servitor workflow route only when review is authorized, 3+ independent homogeneous files/rule groups require schema-validated aggregation, and no session continuation or interactive takeover is needed. Ordinary review follows the authorization/capability/coverage decision table in `../SKILL.md`; Servitor is never a default merely because several files changed.

The historical `servitor batch --config` command from v1 no longer exists. The retained structured batch route uses `servitor workflow` with `parallel()` and `agent()` calls.

## What changed

- `servitor batch --agents a,b,c --config <path>` -> gone; use `servitor workflow run review.workflow.js`.
- `servitor run --expect-json --schema <path>` -> gone; use `agent(prompt, { schema })` inside a workflow.
- `--max-concurrent` -> replaced by `servitor workflow --max-parallel <N>` (default 12).
- Python SDK (`import servitor`) -> gone.

## Migration: batch config to workflow

The legacy batch config JSON mapped tasks to prompts with schema validation. In v0.2.0, the same structure becomes a workflow:

```javascript
export const meta = { name: "multi-file-review" };

// Build review prompt per file (same content as legacy prompt_file)
function reviewPrompt(path, diffText, ruleText, language = "Chinese") {
  return `You are a Senior Code Reviewer. Review the following diff and return ONLY raw JSON (no prose, no code fence).

## Review Rule
${ruleText}

## File
${path}

## Diff
${"```"}
${diffText}
${"```"}

Return a JSON array of findings. Each finding object:
{"path": "${path}", "content": "<issue description in ${language}>", "start_line": <int>, "end_line": <int>, "category": "bug|security|performance|maintainability|test|style|documentation|other", "severity": "critical|high|medium|low", "suggestion_code": "<optional fix code>"}

Rules:
- Every finding needs a concrete line number or range.
- If no issues found, return: []
- Do not include findings you cannot locate to a line.
- Do not praise or summarize; only output findings.`;
}

const findingSchema = {
  type: "array",
  items: {
    type: "object",
    required: ["path", "content", "start_line", "end_line", "category", "severity"],
    properties: {
      path: { type: "string" },
      content: { type: "string" },
      start_line: { type: "integer" },
      end_line: { type: "integer" },
      category: { type: "string" },
      severity: { type: "string" },
      suggestion_code: { type: "string" },
    },
  },
};

// Files discovered at runtime or passed via --args
const files = args.files; // [{path, diffText, ruleText}, ...]

phase("review");
const reviews = await parallel(
  files.map(f => agent(reviewPrompt(f.path, f.diffText, f.ruleText), {
    label: f.path,
    schema: findingSchema,
  }))
);

phase("synthesize");
// reviews is an array of parsed finding arrays; controller (workflow body) owns dedup and merge
return { findings: reviews.flat() };
```

## Controller post-processing

After the workflow returns, the controller (main session or another workflow) owns:

- Dedup: same path + overlapping lines + similar content.
- Classify: critical/high always report; medium report with context; low discard if weak.
- Reject unsupported claims; verify findings against codebase.

## Notes

- `servitor workflow --max-parallel 12` (default) caps concurrent agents; lower if hitting 429s.
- For very large diffs, split one file into hunks and review per-hunk; merge results after.
- Schema validation in `agent({ schema })` rejects malformed worker output — treat schema errors as signal to tighten the prompt, not retry blindly.
- Workers do not see each other; controller (workflow body) is the only place results meet.
