<!-- Modified for Claude on 2026-10-07. Derived from openai/codex-security at eb73cc0fa64f25f432bace6f8ff3f475038bfc71. Local workflows replace Codex host integration. See NOTICE and LICENSE. -->

# Local scan artifacts and continuity

This adaptation uses ordinary local files, with format marker `claude-security-scan/v1`. It does not reproduce the Codex database, handoff tokens, artifact seals, native IDs, SARIF export, or token metering. Do not apply the native Codex findings schema to these local outputs.

For a complete scan, write these files to one output directory:

- `scan-manifest.json`: format marker, target label, actual revision or snapshot identity when known, requested scope and exclusions, mode, source limitations, completion status, and performed checks. A HEAD revision alone does not identify a dirty worktree. Use a digest only if actually measured over the assessed input.
- `threatmodel.md`: exact supplied model, or the source-backed generated model with facts, assumptions and hypotheses separated. Preserve supplied text; put extra evidence in a separate clearly labeled section or report.
- `findings.json`: an object with the format marker and a `findings` array of validated, reportable findings. Use an empty array when none are established; an empty array never establishes full coverage.
- `coverage.json`: requested inventory, fully reviewed paths, exclusions with reasons, remaining paths, supporting paths, rejected/suppressed candidates with counterevidence, deferred candidates with evidence and exact proof gaps, open questions, and a boolean `complete`. Count only files actually fully reviewed in the requested inventory. Reading search hits or architecture snippets is not full review. Deduplicate overlapping passes.
- `report.md`: scope and source identity, executive findings summary, source-backed findings, validation basis, counterevidence, severity/confidence, actual coverage, remaining work and next actions. Distinguish no findings in reviewed material from a claim that the repository is secure.

Every finding retains a stable local ID, title, vulnerability family and CWE when established, attacker, controlled input, prerequisites, violated invariant, source-to-sink path, root cause, impact, mitigation and counterevidence. Include exact repository-relative `locations` with `path`, `startLine`, optional `endLine`, and roles such as `entrypoint`, `root_control`, `sink`, and `concrete_implementation`. Evidence entries contain actual inspected code or observed results and explain what they establish. Separate calibrated severity (`critical`, `high`, `medium`, `low`) from confidence (`high`, `medium`, `low`) and state the reason for each. Do not invent line numbers or runtime output.

When a standalone phase is requested, maintain one `candidates.json` collection or the same inline candidate collection if no files were requested. Preserve each candidate ID, original source evidence, affected instances and order. Discovery adds plausible candidates; validation adds `reportable`, `suppressed`, `not_applicable`, or `deferred` and its basis; attack-path analysis adds its facts and final decision. Every candidate receives an explicit outcome. Pending candidates never enter the validated findings array.

If detailed artifacts are requested, use `findings/<id>/discovery.md`, `validation.md`, `attack-path.md`, or `fix.md` within the output directory. Store actual PoCs, crafted inputs and logs in `findings/<id>/validation-artifacts/`. Do not create empty directories or placeholder proof. Writeups may use `findings/<slug>/<slug>.md`. Hardening output goes in `hardening/` without changing the evidence collection.

Checkpoint a longer audit as ordinary local JSON with `complete: false` and honest partial coverage. Resume only against the same input identity; record source drift rather than silently treating a different checkout as the old target. Complete the report only after every requested path and candidate has a recorded outcome, or explicitly deliver partial results. If token usage is unavailable, say unavailable and do not estimate it.

Validate JSON syntax, citations and result-relative links before delivery. JSON parsing validates syntax, not factual accuracy or full schema conformance. Specialized patch-risk and triage skills keep their own documented contracts.
