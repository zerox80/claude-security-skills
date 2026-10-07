---
name: threat-model
description: "Create, review or update a source-backed threat model of a supplied repository or component. Use for explicit threat-model requests or a requested modeling phase, not as a substitute for a full security audit."
---

<!-- Modified for Claude on 2026-10-07. Derived from openai/codex-security at eb73cc0fa64f25f432bace6f8ff3f475038bfc71. Local workflows replace Codex host integration. See NOTICE and LICENSE. -->

# Security threat model

Read [references/claude-runtime.md](references/claude-runtime.md) for the actual tools, source-access limits and authorization boundaries in this Claude session.

Use [references/threat-model.md](references/threat-model.md) to map the exact supplied repository or component. Read applicable policy with [references/security-guidance.md](references/security-guidance.md). Honor the requested scope, source state, output path and authoritative context.

Preserve a supplied model unchanged unless the user requests revision. If an explicitly required input is missing, request it; do not substitute generated assumptions. A reusable model from a previous run may be used only when its source identity and scope still match. Do not silently update a shared cache.

Separate actual architecture and controls, supplied deployment facts, conditional assumptions, open questions and hypothetical attacker stories. Verify every source citation and effective resource against its actual consumer. Use a separate sequential architecture cross-check when no fresh reviewer is available and do not claim independence.

Return the requested model inline or as `threatmodel.md` through [references/artifact-storage.md](references/artifact-storage.md). A model requested within a scan stays with that scan. Threat modeling alone does not validate vulnerabilities or establish completed source-audit coverage.
