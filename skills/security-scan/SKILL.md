---
name: security-scan
description: "Perform a source-backed static security audit of a supplied repository or scoped paths. Use for a full security scan or audit; use security-diff-scan for a PR, commit or patch review."
---

<!-- Modified for Claude on 2026-10-07. Derived from openai/codex-security at eb73cc0fa64f25f432bace6f8ff3f475038bfc71. Local workflows replace Codex host integration. See NOTICE and LICENSE. -->

# Security scan

Read [references/claude-runtime.md](references/claude-runtime.md) for the actual tools, source-access limits and authorization boundaries in this Claude session.

Read [references/core-scan.md](references/core-scan.md) for the complete source-backed audit. Apply it to the exact supplied repository or selected paths, preserving the supplied threat model and security context. Inspect all requested source before claiming complete coverage; preserve generated and implementation-owning code as review data where relevant.

Use [references/scan-artifacts.md](references/scan-artifacts.md) to checkpoint and deliver a local report, model, findings and coverage. If source access or session limits prevent full review, deliver the retained findings and exact remaining work as partial. An empty findings array means no validated finding in the reviewed material.

Keep the source read-only and the scan offline. Do not execute application code, start a server, install tools, change configuration, or make tracker writes as part of the static audit. Detailed vulnerability reports, hardening proposals and remediation are additional workflows only when requested. Report token usage only when the environment actually measures it.
