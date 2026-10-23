# TODO

## Next up
- [ ] T-002 | P1 | OPEN | Zuordnung von GitHub-Repository und Sites bestätigen.
  - Akzeptanz: Die beabsichtigte Site und ihr Quell-Remote sind belegt; Abweichung der Quell-SHAs ist erklärt.
  - Abhängigkeit: Kein Deployment-Auftrag in dieser Session; vor nächstem Sites-Update bearbeiten.
- [ ] T-003 | P1 | OPEN | Live-Snapshot sichern und Wiederherstellung prüfen.
  - Akzeptanz: Exportintegrität und Restore geprüft; Ausgangsstand auf GitHub gesichert und Remote-SHA sowie Sites-Version im Manifest dokumentiert.
  - Abhängigkeit: T-002; zwingendes Gate vor einem Sites-Update.

## In progress
Keine.

## Blocked
Keine Aufgaben der Repository-Konfiguration blockiert. Sites-Deployment bis T-002/T-003 gesperrt.

## Done
- [x] T-001 | P1 | DONE | Repository gemäß gelieferter Projektvorgabe konfigurieren.
  - Akzeptanz: AGENTS.md unverändert; Pflichtdokumentation, Ignore-Regeln, Umgebungsbeispiel, Bestandsmanifest und Validierung vorhanden; index.html unverändert; lokale Checks erfolgreich.
  - GitHub-Abschluss: stabiler Verweis `refs/heads/main`; finale Commit-SHA und bestätigter Remote-Stand im Abschlussbericht. Bei fehlgeschlagener Veröffentlichung T-001 wieder öffnen.
