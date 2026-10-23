# Session-Logs

Je Session `sessions/YYYY-MM-DD_HHMM_<kurzthema>.md` in Europe/Berlin anlegen. Erfassen: Start/Ende, Ziel, Ausgangszustand, Änderungen, Entscheidungen, Befehle ohne Secrets, Prüfungen, Commits, Remote-Verifikation, Sites-/Backup-/Rollback-Aktionen, Fehler und offene Risiken.

Status klar als GEPLANT, VERSUCHT, VERIFIZIERT oder FEHLGESCHLAGEN markieren. Nicht ausgeführte Checks als NOT RUN mit Grund erfassen. Keine Tokens, Zugangsdaten, vollständigen personenbezogenen Datensätze oder sensiblen Payloads.

Aufbewahrung: kompakte Session-Logs mindestens 12 Monate behalten. Danach quartalsweise prüfen und ältere Logs bei Bedarf in Jahresdateien zusammenführen; Commit-, Versions- und Incident-Referenzen erhalten. Keine automatische Löschung offener Risiken. Git-Historie nicht umschreiben. Große Artefakte extern halten und hier nur Referenz plus Integritätsnachweis speichern.
