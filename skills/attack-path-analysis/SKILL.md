---
name: attack-path-analysis
description: "Trace supplied security findings from attacker-controlled source through controls to sensitive sinks, assess counterevidence, and calibrate severity and reportability. Use for explicit attack-path or severity analysis."
---

<!-- Modified for Claude on 2026-10-07. Derived from openai/codex-security at eb73cc0fa64f25f432bace6f8ff3f475038bfc71. Local workflows replace Codex host integration. See NOTICE and LICENSE. -->

# Security attack-path analysis

Read [references/claude-runtime.md](references/claude-runtime.md) for the actual tools, source-access limits and authorization boundaries in this Claude session.

Start from supplied findings or plausible candidates and the repository's threat model. If essential model context is missing, request it or clearly state the assumptions the user permits; do not invent exposure or privilege. Read [references/security-guidance.md](references/security-guidance.md), [references/static-finding-assessment.md](references/static-finding-assessment.md), [references/attack-path-facts.md](references/attack-path-facts.md), and [references/severity-policy.md](references/severity-policy.md).

For every candidate, map the real service or workflow, entrypoint, attacker identity and starting privilege, trust boundaries, controlled data, transformations, actual controls, sensitive sink, capability gain, prerequisites and concrete impact. Preserve every exact affected instance, source anchor and root-control location. Use supplied context and source evidence; no deployment inference becomes a fact simply because a sink is dangerous.

Challenge each reportability-driving fact with the strongest counterevidence: out-of-scope code, internal-only exposure, admin-only callers, same-privilege behavior, lack of a boundary crossing, effective controls, or a genuinely unreachable path. Missing public ingress alone does not defeat a caller-controlled library or parser boundary. Retain unknowns where evidence is incomplete.

Keep factual attack-path assessment, impact/likelihood severity calibration and policy adjustment as separate stages. Apply the provided severity matrix mechanically after facts are established. Record `ignore` or `deferred` explicitly rather than silently dropping candidates, and explain the source-backed reason.

Return one decision per candidate with its ID, title, role-labeled file/line locations, attack steps, rendered facts, counterevidence, severity and confidence rationale, final policy decision and remaining proof gaps. Retain continuity through [references/scan-artifacts.md](references/scan-artifacts.md). Keep source read-only and inspection offline. Never invent a reachable attack chain or claim runtime exploitation from static evidence.
