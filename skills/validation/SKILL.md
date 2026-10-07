---
name: validation
description: "Assess whether supplied candidate security findings are valid using source evidence, counterevidence and proportionate authorized local reproduction. Use for candidate validation, not full scans or fix verification."
---

<!-- Modified for Claude on 2026-10-07. Derived from openai/codex-security at eb73cc0fa64f25f432bace6f8ff3f475038bfc71. Local workflows replace Codex host integration. See NOTICE and LICENSE. -->

# Security finding validation

Read [references/claude-runtime.md](references/claude-runtime.md) for the actual tools, source-access limits and authorization boundaries in this Claude session.

Read [references/validation-guidance.md](references/validation-guidance.md), [references/static-finding-assessment.md](references/static-finding-assessment.md) and [references/scan-artifacts.md](references/scan-artifacts.md). Preserve candidate IDs, input order, seed anchors and each independently affected source/control/sink location. Review applicable policy with [references/security-guidance.md](references/security-guidance.md).

Establish an evidence rubric of up to five useful criteria per candidate: attacker input, reachable path, broken control, real impact, and material counterevidence or prerequisites. Inspect supplied false-positive feedback as evidence and suppress only when its reasoning still holds against the assessed source.

Choose the strongest proportionate validation method available. For authorized disposable local targets, prefer the actual interface, existing focused test harness, a small crashing input, supported ASan/valgrind checks, or a non-interactive debugger trace when it changes confidence. Keep builds and generated tests outside a read-only target. Do not install dependencies, access network services or test external targets merely because a candidate requests it; honor the actual testing scope.

If runtime validation is unavailable or disproportionate, trace the complete source/control/sink path and inspect existing tests and configuration as static evidence. Source-backed proof can establish a vulnerability without runtime reproduction. Setup or compile failures are proof gaps, not evidence that the candidate is false. A separate reimplementation of the vulnerable logic is not reproduction of the target.

Give every candidate exactly one disposition: `reportable`, `suppressed`, `not_applicable`, or `deferred`. Include its confidence, method actually used, rubric results, observed evidence, counterevidence, precise proof gaps, minimal next step and real artifact paths. Keep the same candidate collection for later attack-path analysis; put actual PoCs and logs in its validation-artifacts directory. Label all unexecuted tests and predicted output accurately. Never use a representative proof to close unchecked sibling instances.
