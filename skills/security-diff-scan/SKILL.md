---
name: security-diff-scan
description: "Review a supplied pull request, commit range, branch diff or working-tree patch for security vulnerabilities, with complete changed-file coverage and source-backed evidence."
---

<!-- Modified for Claude on 2026-10-07. Derived from openai/codex-security at eb73cc0fa64f25f432bace6f8ff3f475038bfc71. Local workflows replace Codex host integration. See NOTICE and LICENSE. -->

# Security diff scan

Read [references/claude-runtime.md](references/claude-runtime.md) for the actual tools, source-access limits and authorization boundaries in this Claude session.

Bind the exact supplied patch or establish base and head for a Git comparison. For a working-tree review, capture the relevant staged and unstaged changes and document whether untracked files were included. Keep the assessed patch bytes and source state stable; record actual revision identity or an actually computed patch digest.

Read [references/security-guidance.md](references/security-guidance.md), [references/threat-model.md](references/threat-model.md), [references/static-finding-assessment.md](references/static-finding-assessment.md) and [references/scan-artifacts.md](references/scan-artifacts.md). Preserve a supplied model. Generate only the model context needed to interpret changed security behavior when none was supplied.

Inventory every changed file, including deletions, renames and changed text regardless of filename extension. Inspect deleted source at the baseline and changed behavior at the assessed head or snapshot. Do not count uninspected binary or generated implementation as reviewed; record a concrete gap when it cannot be inspected. Follow supporting code only as needed to explain changed controls and affected callers.

Review every changed file and every plausible candidate. Use [references/discovery-checklist.md](references/discovery-checklist.md) to preserve concrete instances, source/control/sink paths, seed anchors and affected operations. Validate candidates with source evidence and strongest counterevidence; calibrate using [references/severity-policy.md](references/severity-policy.md). A finding must arise from changed behavior or a directly affected shared control; unrelated preexisting bugs are separate observations.

Keep the checkout unchanged and the review offline. Record one explicit outcome for every candidate, retaining deferred proof gaps and rejected evidence. Deliver the local report, findings and actual changed-file coverage. Use baseline citations for deleted lines and assessed-head citations for current lines. Never fabricate inline review comments or claim native scan completion, SARIF export or measured usage.
