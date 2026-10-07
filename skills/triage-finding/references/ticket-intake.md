<!-- Modified for Claude on 2026-10-07. Derived from openai/codex-security at eb73cc0fa64f25f432bace6f8ff3f475038bfc71. Local workflows replace Codex host integration. See NOTICE and LICENSE. -->

# Jira and Linear finding intake

Use only connected tools actually available in Claude and the account/source selected for the request. Exact issue links or IDs can be fetched directly. For a selected collection, resolve its project/team and query, paginate all selected results, and fetch complete finding content before normalization. Retain identifiers, URLs, query, state, reported revision and parent relationships as provenance. Do not infer inaccessible content from a title or repository code.

Use supported live metadata and schemas; no Codex app URL, deferred-operation API or particular tool name is assumed. A missing connector, authentication failure or unreadable item is a retrieval limitation. Ask for the complete claim or the appropriate connection instead of fabricating a triage result. Retry a transient identical read at most once without changing account or broadening scope.

For parent/sub-issue trees, honor the selected depth and issue set. Resolve direct children before recursively importing more; organizing summaries without independent claims are not vulnerability findings. Keep deterministic input order and one result per selected claim, including duplicates.

Normalize issue-based findings as scanner_ticket unless their actual contents are an advisory, CVE, bug bounty or native scanner finding. Preserve available fields without inventing priority, assignee or ownership. Intake is read-only: no comments, transitions, assignments, label edits or closure is implied. Finish static verdicts before considering any separately requested writeback.
