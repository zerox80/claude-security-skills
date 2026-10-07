<!-- Modified for Claude on 2026-10-07. Derived from openai/codex-security at eb73cc0fa64f25f432bace6f8ff3f475038bfc71. Local workflows replace Codex host integration. See NOTICE and LICENSE. -->

# Artifact storage

Honor the output path selected by the user. Otherwise use a separate writable results directory in the current session. Discover the actual output location in Claude.ai; do not assume a fixed container path. In a local session, keep retained output outside the audited source tree unless the user explicitly chose a location inside it.

Use normal file tools. There is no artifact-storage MCP requirement. Keep inputs, source, previous reports, and existing user files unchanged; choose a fresh output directory to avoid overwriting another run. A chat-only request can return its requested result inline. Read-only skills such as verify-fix do not write files at all.

Use repository-relative source citations and result-relative links in distributed reports. Redact credential material. Keep source identity, assumptions, evidence and gaps attached to the result. Do not create a shared model cache or write outside the requested workspace.

Follow [scan-artifacts.md](scan-artifacts.md) for local scan output and candidate continuity. These files describe this Claude adaptation, not sealed native Codex artifacts.
