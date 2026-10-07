<!-- Modified for Claude on 2026-10-07. Derived from openai/codex-security at eb73cc0fa64f25f432bace6f8ff3f475038bfc71. Local workflows replace Codex host integration. See NOTICE and LICENSE. -->

# GitHub draft security advisories

Create only a maintainer-owned private draft for one selected validated finding when the user explicitly requests that external write. Use available authenticated advisory-capable tools or a selected gh account for the exact repository. A missing integration means draft the payload locally and report that it was not posted.

Verify repository identity, audience, canonical source, actual permissions, precise affected package and release evidence. A scanned commit alone does not prove an affected version range. Include summary, description and supported vulnerability/package fields; add patched versions or CWE/CVSS data only when actually established. Leave unrequested CVE assignment, publication, forks, credits and collaborator actions alone.

Search all relevant advisory states and read plausible exact-binding or same-package matches. Reuse an exact supported match read-only; block ambiguity rather than creating a duplicate. Preview the full exact payload, account, destination and disclosure consequences. Honor approval for an unchanged payload and obtain any missing authorization before writing.

Submit once through the supported API, keeping finding text out of shell source. Follow that connected tool's or current official API's accepted schema and version rather than assuming an old fixed API header. Read back the returned advisory and confirm draft state and payload fields. Record the real identifier, URL and any verification gap. Reconcile an uncertain create before retrying. Do not publish or close an advisory as part of tracking.
