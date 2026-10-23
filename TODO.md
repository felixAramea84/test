# TODO

## Next up
- [ ] T-004 | P1 | IN_PROGRESS | Rathausfoto ergänzen und Test-Website veröffentlichen.
  - Akzeptanz: Foto mit Alt-Text, Bildquelle/Lizenz und responsiver Darstellung; Quellstand auf GitHub gesichert; Sites-Deployment erfolgreich.
  - Abhängigkeit: Pre-Backup 3c7de0c47a901482c57ff257c8ba9c3db49c2066 verifiziert.

- [x] T-002 | P1 | DONE | Zuordnung von GitHub-Repository und Sites bestätigen.
  - Akzeptanz: Die beabsichtigte Site und ihr Quell-Remote sind belegt; Abweichung der Quell-SHAs ist erklärt.
  - Ergebnis 2026-10-23: Site-Quell-Remote bestätigt, bisher eigene Sites-Historie mit leerer Seite; nun bewusst mit dem GitHub-Projekt verknüpft.
- [x] T-003 | P1 | DONE | Live-Snapshot sichern und Wiederherstellung prüfen.
  - Akzeptanz: Exportintegrität und lokale Rekonstruktion geprüft; Ausgangsstand auf GitHub gesichert und Remote-SHA sowie Sites-Version im Manifest dokumentiert.
  - Ergebnis 2026-10-23: Quell-SHA entspricht Version 1; Deployment-Dateien im Backup-Commit 3c7de0c47a901482c57ff257c8ba9c3db49c2066, tar-Inhalte bytegleich rekonstruiert. Live-Restore nicht ausgeführt.

## In progress
Keine.

## Blocked
Keine. Sites-Version 1 anhand Quell-SHA identifiziert und als rekonstruierbarer statischer Stand auf GitHub gesichert; siehe backups/2026-10-23-pre-rathaus.json. Tatsächlicher Live-Restore nicht ausgeführt.

## Done
- [x] T-001 | P1 | DONE | Repository gemäß gelieferter Projektvorgabe konfigurieren.
  - Akzeptanz: AGENTS.md unverändert; Pflichtdokumentation, Ignore-Regeln, Umgebungsbeispiel, Bestandsmanifest und Validierung vorhanden; index.html unverändert; lokale Checks erfolgreich.
  - GitHub-Abschluss: stabiler Verweis `refs/heads/main`; finale Commit-SHA und bestätigter Remote-Stand im Abschlussbericht. Bei fehlgeschlagener Veröffentlichung T-001 wieder öffnen.
