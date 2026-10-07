# Claude Security Skills

15 Skills für Sicherheitsanalysen mit Claude Code und Claude.ai, angepasst aus
[OpenAI codex-security](https://github.com/openai/codex-security/tree/main/plugins/codex-security/skills).
Alle benötigten Referenzen liegen im jeweiligen Skill-Ordner. Die Skills sind lokale
Arbeitsabläufe; ein Codex-Security-Server ist nicht erforderlich.

## Download und Installation in Claude Code

1. Lade [claude-security-skills-gesamt.zip](claude-security-skills-gesamt.zip) herunter und entpacke es.
2. Kopiere die 15 Ordner unter `claude-security-skills/claude-skills/` in den persönlichen Skills-Ordner `~/.claude/skills/`.
3. Öffne eine neue Claude-Code-Sitzung. `/skills` zeigt die verfügbaren Skills.

Beispiel unter Linux/macOS, im entpackten Paket:

```sh
mkdir -p ~/.claude/skills
cp -R claude-skills/. ~/.claude/skills/
```

Prüfe vor dem Kopieren, ob gleichnamige Skills schon vorhanden sind. Für eine
Installation nur in einem Projekt verwende `.claude/skills/` im Projektordner.
Unter Windows liegt der persönliche Ordner unter `%USERPROFILE%\.claude\skills`.

Du kannst auch dieses Repository klonen und die lesbaren Skill-Ordner direkt kopieren:

```sh
git clone https://github.com/zerox80/claude-security-skills.git
cd claude-security-skills
mkdir -p ~/.claude/skills
cp -R skills/. ~/.claude/skills/
```

Die Quellen aller angepassten Skills sind unter [`skills/`](skills/) einsehbar.

Beispielaufrufe:

```text
/security-scan Prüfe dieses Repository auf Sicherheitslücken.
/security-diff-scan Prüfe die aktuellen Änderungen auf Sicherheitslücken.
/threat-model Erstelle ein Threat Model für dieses Projekt.
```

## Import in Claude.ai

Lade eine der einzelnen Skill-ZIPs in diesem Repository hoch, oder verwende
die ZIPs unter `import-zips/` im Gesamtpaket. In Claude:
`Customize > Skills > + > Create skill > Upload a skill`.
Das Gesamtpaket selbst ist kein einzelner importierbarer Skill.
Für Web-Skills muss Code execution and file creation aktiviert sein.
Ein Skill-Import gewährt keinen automatischen Zugriff auf lokale Repositories.

## Enthaltene Skills

| Skill / Aufruf | Aufgabe | Import-ZIP |
| --- | --- | --- |
| `/assess-patch-risk` | Auswirkungen und Regressionsrisiken einer Änderung beurteilen | [assess-patch-risk.zip](assess-patch-risk.zip) |
| `/attack-path-analysis` | Angriffspfade, Gegenbelege und Schweregrad prüfen | [attack-path-analysis.zip](attack-path-analysis.zip) |
| `/deep-security-scan` | Mehrere lokale Prüfdurchgänge über denselben Quellstand durchführen | [deep-security-scan.zip](deep-security-scan.zip) |
| `/define-security-policy` | SECURITY.md und Sicherheitsgrenzen definieren oder prüfen | [define-security-policy.zip](define-security-policy.zip) |
| `/finding-discovery` | Plausible Kandidaten für Sicherheitslücken finden | [finding-discovery.zip](finding-discovery.zip) |
| `/fix-finding` | Eine konkrete Sicherheitslücke gezielt beheben und prüfen | [fix-finding.zip](fix-finding.zip) |
| `/propose-security-hardening` | Strukturelle Sicherheitsverbesserungen mit Alternativen vorschlagen | [propose-security-hardening.zip](propose-security-hardening.zip) |
| `/security-diff-scan` | PRs, Commits und lokale Änderungen auf Sicherheitslücken prüfen | [security-diff-scan.zip](security-diff-scan.zip) |
| `/security-scan` | Ein Repository oder ausgewählte Pfade statisch prüfen | [security-scan.zip](security-scan.zip) |
| `/threat-model` | Ein quellenbasiertes Threat Model erstellen | [threat-model.zip](threat-model.zip) |
| `/track-findings` | Befunde als Tracker-Einträge oder private Advisory-Entwürfe vorbereiten | [track-findings.zip](track-findings.zip) |
| `/triage-finding` | Vorhandene Meldungen anhand von Policy und Quellcode einstufen | [triage-finding.zip](triage-finding.zip) |
| `/validation` | Kandidaten durch Quellcode und erlaubte lokale Reproduktion bewerten | [validation.zip](validation.zip) |
| `/verify-fix` | Prüfen, ob eine gemeldete Sicherheitslücke tatsächlich behoben ist | [verify-fix.zip](verify-fix.zip) |
| `/vulnerability-writeup` | Nachvollziehbare Vulnerability-Berichte aus belegten Erkenntnissen schreiben | [vulnerability-writeup.zip](vulnerability-writeup.zip) |

## Anpassungen und Grenzen

Gemeinsame Referenzen wurden in die einzelnen Skill-Pakete aufgenommen.
Codex-spezifische Datei- und Toolverweise wurden durch lokale Claude-Abläufe ersetzt.
Die fachlichen Regeln für Evidenz, Gegenbelege, Validierung, Schweregrad und Berichte
wurden übernommen oder angepasst.

Native Scan-Datenbank, Artefaktversiegelung, Hintergrundkoordination, automatischer
SARIF-Export und Tokenmessung sind nicht enthalten. Deep Scan verwendet lokale
Prüfdurchgänge; mehrere Durchgänge im selben Kontext sind keine unabhängigen Audits.
GitHub, Jira und Linear benötigen passende verbundene Tools oder ein ausgewähltes
CLI-Konto. Ohne Verbindung können lokale Entwürfe erstellt werden.
Der optionale Patch-Risk-Validator benötigt das bereits installierte Python-Paket
`jsonschema`; die Skills installieren es nicht automatisch.

## Prüfung

Für alle 15 Skills wurden Namen, Metadaten, lokale Referenzziele und ZIP-Struktur
geprüft. Die installierten Dateien wurden mit den geprüften Paketen verglichen.
Der hinzugefügte Validator wurde mit gültigen, ungültigen und stdin-Daten geprüft.
Es wurde kein echter Sicherheitsscan in Claude ausgeführt; diese Prüfungen belegen
die Paketstruktur und keine garantierte Erkennungsleistung.

Prüfsummen und Herkunft: [Quelle-und-Pruefung.json](Quelle-und-Pruefung.json).
Weitere Hinweise: [Anleitung-Claude.txt](Anleitung-Claude.txt).

## Quelle und Lizenz

Originalquelle: [openai/codex-security](https://github.com/openai/codex-security).
Quellstand: `eb73cc0fa64f25f432bace6f8ff3f475038bfc71`, abgerufen am 07.10.2026.
[codex-security-originale.zip](codex-security-originale.zip) enthält unveränderte
Plugin-Quellen zum Vergleich und ist kein Claude-Importpaket oder kompilierter Server.

Apache-2.0; siehe [LICENSE](LICENSE) und [NOTICE](NOTICE).
Jedes Skill-Paket enthält ebenfalls Lizenz und Herkunftsangabe.
Diese Anpassung ist keine offizielle Integration von OpenAI oder Anthropic.

Offizielle Dokumentation:
[Claude Code Skills](https://code.claude.com/docs/en/skills) ·
[Claude.ai Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
