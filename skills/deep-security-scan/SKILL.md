---
name: deep-security-scan
description: "Perform several source-backed audit passes over the same supplied repository or scoped paths to challenge findings and improve coverage. Use for a deep or multi-pass audit, not a PR or patch review."
---

<!-- Modified for Claude on 2026-10-07. Derived from openai/codex-security at eb73cc0fa64f25f432bace6f8ff3f475038bfc71. Local workflows replace Codex host integration. See NOTICE and LICENSE. -->

# Deep security scan

Read [references/claude-runtime.md](references/claude-runtime.md) for the actual tools, source-access limits and authorization boundaries in this Claude session.

This is a local multi-pass audit. It does not reproduce the native Codex coordinator, parallel scan isolation, restart recovery, long-running background execution or usage accounting.

Bind one supplied source state and scope for every pass. Read [references/core-scan.md](references/core-scan.md) and [references/scan-artifacts.md](references/scan-artifacts.md). Honor the user's pass count or budget. If neither is specified, plan three bounded passes and state that assumption. Do not invent a fixed runtime or guaranteed coverage.

1. First pass: perform the complete baseline audit, map architecture, inspect requested source and retain source-backed candidates and counterevidence.
2. Second pass: reopen the source with alternate forward/backward and authorization perspectives. Challenge prior assumptions and examine sibling entrypoints, concrete sink variants and missing coverage. Do not simply reread the prior report and call it another audit.
3. Third pass: revisit remaining source and material proof gaps, test the strongest benign explanations statically, validate unique surviving candidates and reconcile coverage. Additional requested passes repeat substantive source inspection from another useful perspective.

Use sequential passes unless real delegation is available and authorized. State whether passes shared a context and avoid claiming statistical independence or quantified variance reduction. Keep each completed pass's findings, covered paths, exclusions and unresolved candidates available for reconciliation.

Merge by the same broken control and effective remediation, preserving every independently affected instance. Do not add overlapping file counts. Save the aggregate local artifacts and record passes planned and completed. Report partial deep coverage if the requested passes or source review were unfinished, along with the retained findings and exact outstanding work. Never silently replace a different source state with the original target.
