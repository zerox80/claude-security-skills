---
name: track-findings
description: "Prepare reviewed tracking items or private advisory drafts for validated security findings in a selected Linear, Jira or GitHub destination. Use available connected tools or an authorized CLI for explicitly requested writes and duplicate checks."
---

<!-- Modified for Claude on 2026-10-07. Derived from openai/codex-security at eb73cc0fa64f25f432bace6f8ff3f475038bfc71. Local workflows replace Codex host integration. See NOTICE and LICENSE. -->

# Track security findings

Read [references/claude-runtime.md](references/claude-runtime.md) for the actual tools, source-access limits and authorization boundaries in this Claude session.

Prepare tracking for the supplied validated findings in one selected provider and destination. Native Codex scan IDs, database receipts and artifact seals are not required. Preserve the source collection and identify exactly which source state and findings the request covers. An unverified candidate cannot become a validated finding merely by being copied into a ticket.

Use available connected Linear, Jira or GitHub tools, or an explicitly selected authenticated CLI. A ZIP import does not install these integrations. If the required connection is missing, produce reviewed ticket drafts with their metadata and duplicate-check limitations; do not claim they were created. Read [references/jira.md](references/jira.md) for Jira work and [references/github-security-advisories.md](references/github-security-advisories.md) for advisory drafts.

1. Read the actual evidence and local manifest/findings when present. Validate any existing integrity metadata with the corresponding available tools; otherwise record source integrity as unverified instead of fabricating a seal. Preserve canonical source IDs/fingerprints when supplied. For local findings, use their actual stable local IDs and clearly labeled locally generated bindings. Resolve any missing source identity or validity that matters before writing.
2. Resolve the exact destination, live account and audience from the request and connected source. Verify actual access and visibility. Honor private-disclosure policy; never silently switch accounts, transports, repositories or audiences. Source repository and tracking destination can be different choices.
3. Search the selected destination across relevant statuses for finding IDs, fingerprints and narrow semantic matches, then read plausible duplicates. Similar text alone is insufficient. Choose create, read-only reuse, reviewed update, or blocked. Record incomplete searches as a limitation; do not claim a complete duplicate check without doing it.
4. Preview the concrete payload: selected findings, source identity, destination, audience, account, duplicate decision, exact title/body/metadata, uncertainty and omitted sensitive details. An advisory requires verified affected release/package information. No credential material, signed URL or private exploit detail belongs in a public issue. Honor existing explicit approval for the unchanged payload; request missing disclosure or write authorization before any new external mutation.
5. After a pause, recheck evidence identity, account, visibility and selected existing items. Execute approved writes serially with exact supported fields and preserve other issue content. Capture the returned item identity and read back actual changed fields when possible. If a write fails or times out ambiguously, reconcile by exact reads or bindings before any retry; never duplicate an uncertain create.

Use commit-pinned links only for verified source at that immutable revision and checked paths. A dirty checkout or unverified source gets plain role-labeled path/line references, with the limitation stated. Keep draft files and tracking receipts separate from the evidence collection. For CLI text bodies, use a safely created file with restricted permissions and a body-file argument rather than interpolating finding text into shell source.

Report each item as drafted, created, updated, reused, blocked, failed, uncertain or unprocessed, with actual returned links or IDs. Do not merge code, publish advisories, request CVEs, manage users/settings or change issue status unless those additional actions were explicitly requested.
