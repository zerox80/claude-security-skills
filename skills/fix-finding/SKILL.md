---
name: fix-finding
description: "Use only when the user explicitly asks to fix and verify a validated or plausible security vulnerability. Do not use for ordinary bug fixes, correctness or design review findings, general validation, or full PR, commit, branch, patch, or repository scans."
---

<!-- Modified for Claude on 2026-10-07. Derived from openai/codex-security at eb73cc0fa64f25f432bace6f8ff3f475038bfc71. Local workflows replace Codex host integration. See NOTICE and LICENSE. -->

# Fix Finding

Read [references/claude-runtime.md](references/claude-runtime.md) for the actual tools, source-access limits and authorization boundaries in this Claude session.

Before choosing paths or saving retained output, read `references/artifact-storage.md` and follow its storage policy.

## Objective

Turn a current security finding into a minimal, validated code change. If the code is already safe, prove that and report that no change was needed.

Judge the result in this order:

1. the current state is correctly classified as vulnerable, already safe, or unproven
2. any fix completely closes the broken security boundary
3. legitimate behavior and compatibility are preserved
4. relevant repository checks pass
5. the implementation follows repository conventions
6. the patch contains only the scope necessary for the earlier properties

Never trade an earlier property for a later one. Minimal means the smallest repository-native change that satisfies all earlier properties, not the fewest lines.

## Patch Contract

Before editing, inspect the affected implementation, its direct callers, nearby helpers, and relevant existing tests. Establish from repository evidence:

- the attacker-controlled input and concrete source-to-sink path or broken control
- the security invariant and narrowest shared enforcement boundary
- legitimate behavior, APIs, error semantics, and compatibility constraints that must remain
- the closest existing implementation, validation, and error-handling precedents

Treat the finding as a data-flow and boundary problem, not merely the named input example. Check equivalent encodings, parser forms, aliases, callers, sinks, and every representation or copy of security-sensitive state that could bypass the proposed change. Handle unsafe state explicitly; do not silently accept, truncate, or reinterpret it into another reachable form.

## Pre-Patch Investigation

The parent agent owns the patch and independently traces the reported path. Before editing, use one fresh read-only reviewer when real delegation is available and authorized. If delegation is unavailable, perform the same perspective as a separate pass:

- **Security-boundary and compatibility investigator:** Independently trace the source-to-sink path and identify the shared enforcement boundary, affected entry points, alternate representations or lifecycle states, parser and validation-to-use transitions, concrete sibling paths, and source-backed bypass risks. Establish the legitimate workflows and public behavior that must remain, then inspect callers, implementations, optional modes, errors, side effects, repository conventions, existing helpers, and focused validation commands for integration constraints.

The investigation requires repository-relative evidence and a clear separation between facts, inferences, and unresolved questions. When it completes, reconcile its findings with the parent's investigation and choose the patch boundary.

## Implementation Workflow

1. Trace the reported path and inspect only the context needed to identify the real shared boundary. Return `no_change` when repository evidence shows that the reported path is already safe; do not make a speculative change.
2. When feasible, run the smallest high-signal reproduction through that boundary and one legitimate control through the same path.
3. Implement the smallest repository-native fix at the shared boundary. Prefer nearby helpers and established APIs. Do not broaden into unrelated redesign, cleanup, or sibling findings.
4. Before verification, challenge the patch rather than defending it: inspect every direct caller of each changed helper and both outcomes of each changed condition. Look for one sibling path, representation, or copy that still reaches the vulnerable sink and one ordinary or default input that the patch newly rejects or reinterprets; revise the implementation if either exists.
5. Verify in order:
   - inspect the final diff and run the narrowest syntax, import, build, or type check relevant to it
   - rerun the security trigger or strongest focused substitute and review one alternate malicious input class
   - rerun the legitimate control, nearest existing tests, and the owning package's applicable required checks

Return `blocked` if the vulnerability may be real, but essential evidence, tooling, access, or a product or compatibility decision is missing, so a safe fix cannot be responsibly completed or verified.

## Patch Candidate Review

After implementing and running focused checks, use one fresh read-only reviewer when real delegation is available and authorized. Give it only the finding, repository root, authorized scope, repository policy, and current candidate diff; do not provide the patch rationale, investigator report, or claims that tests passed. If delegation is unavailable, perform the same review perspective as a separate pass before final verification. In either case, use the following assignment:

- **Bypass and regression reviewer:** Reconstruct the invariant and look for a concrete surviving route through affected entry points, equivalent representations, parser boundaries, aliases, backend or platform variants, and validation-to-use gaps. Trace changed conditions and direct callers for concrete breakage of legitimate inputs, public contracts, errors, side effects, state transitions, optional modes, compatibility, resource behavior, and repository conventions.

The reviewer must not edit or delegate. Report only concrete, source-backed bypasses or regressions and explain how each can be verified. Treat reviewer findings as hypotheses: confirm them against the source or focused execution before revising the implementation. Address only confirmed issues within the finding and compatibility boundary; do not broaden into speculative concerns or redesign. Then rerun relevant verification and ensure no temporary or unrelated changes remain. Perform only one review cycle.

## Explicit remediation stages

If the user requests a particular stage, honor it: generate a patch in an isolated copy without changing the target; apply only an approved exact patch after checking its source identity and digest; or verify the current patch without source edits. Do not claim tracker state, native remediation receipts or finding closure. If the current Claude surface cannot edit or test the source, produce only the supported patch or assessment and report the exact remaining validation gap.

## Outcome and Output Contract

In the final response, include:

- outcome: `fixed`, `no_change`, or `blocked`
- the concrete vulnerable path, security invariant, and legitimate behavior that had to remain
- the selected patch strategy and why it was the narrowest complete repository-native option, or the unresolved product decision when blocked
- files changed
- tests or validation artifacts added
- commands run and their pass, fail, or unknown results, grouped by the ordered verification gates
- explicit statement of how the original issue was shown not to reproduce
- explicit statement of how legitimate behavior was shown to remain intact
- remaining uncertainty or skipped validation, if any

If using a scan artifact directory, resolve it using `references/scan-artifacts.md`, then write a visible report to the fix report path. If there is no existing scan directory, a final chat summary is sufficient unless the user asks for a file.

## Hard Rules

- Do not report `fixed` until every ordered verification gate has passed. Omit a check only when repository evidence shows it is irrelevant; an unavailable relevant check makes verification `blocked` and must be reported.
- Do not rely only on code inspection when a focused test or reproducer is feasible.
- Do not broaden the patch into unrelated cleanup, sibling findings, or architectural redesign without evidence that the broader change is required for complete closure.
- Do not remove user changes or unrelated local modifications.
- Do not weaken authentication, authorization, tenant isolation, input validation, sandboxing, or logging to make tests pass.
- Do not hide proof gaps. If the environment blocks validation, say exactly which command or setup failed and what evidence is still missing.
