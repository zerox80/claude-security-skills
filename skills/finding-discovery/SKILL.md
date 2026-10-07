---
name: finding-discovery
description: "Discover plausible candidate security findings in supplied source or a code change. Preserve exact instances and evidence for later validation. Use for candidate discovery, not a complete audit or final severity assessment."
---

<!-- Modified for Claude on 2026-10-07. Derived from openai/codex-security at eb73cc0fa64f25f432bace6f8ff3f475038bfc71. Local workflows replace Codex host integration. See NOTICE and LICENSE. -->

# Security finding discovery

Read [references/claude-runtime.md](references/claude-runtime.md) for the actual tools, source-access limits and authorization boundaries in this Claude session.

Resolve the supplied source, scope, current source identity, context and threat model. Read [references/security-guidance.md](references/security-guidance.md) and [references/discovery-checklist.md](references/discovery-checklist.md). Review actual source before proposing candidates. For a diff, inventory all changed files, including deletions, and follow directly supporting code without broadening into an unrelated audit.

Preserve independently reachable instances, exact seed anchors and source/control/sink evidence. Do not merge concrete operations merely because they share a wrapper, helper or CWE. For a shared-control change, inspect materially affected callers and concrete branches. Apply the checklist according to the actual technology and scope rather than manufacturing candidates for each vulnerability family.

For every plausible candidate, retain a stable ID, descriptive title, attacker-controlled input, entrypoint, closest control, sensitive sink, prerequisites, concrete possible impact, actual inspected evidence, affected file/line locations with roles, advisory/seed references when supplied, and why validation is needed. Add diff line references only when the suspected vulnerability actually overlaps changed behavior. Do not invent final severity.

Return all candidates in one collection using [references/scan-artifacts.md](references/scan-artifacts.md). Continue until the requested source is reviewed or clearly report the remaining paths. An empty collection means no plausible candidate found in reviewed material. Candidate discovery is not proof of exploitability, full validation, or a completed audit.
