# Test-Website

Statische deutsche Testseite „Nur der HSV“. Einstiegspunkt ist `index.html`; CSS ist darin eingebettet. Keine JavaScript-Abhängigkeiten, Datenbank oder Build-Pipeline.

## Lokal starten

Python 3 bereitstellen, dann im Repository ausführen:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Im Browser `http://127.0.0.1:8000` öffnen. Vor Änderungen `AGENTS.md`, `HANDOFF.md`, `TODO.md`, `CHANGELOG.md` und aktuelle Session-Logs lesen.

## Validierung

```sh
python3 scripts/validate.py
git diff --check
```

Die Strukturprüfung kontrolliert Pflichtdateien, relative Markdown-Verweise und das Backup-Manifest. Sie ersetzt keine Browser-, Security- oder Live-Tests. Formatter, Linter, Typprüfung, Unit-/E2E-Tests und Build sind bisher nicht eingerichtet. Keine Build-Schritte für diese reine HTML-Seite nötig.

## Projektstruktur

- `index.html`: bestehende Anwendung.
- `AGENTS.md`: unverändert übernommene Projektregeln aus der gelieferten Vorgabe.
- `HANDOFF.md`, `TODO.md`, `CHANGELOG.md`: Übergabe, Aufgaben und Änderungshistorie.
- `docs/`: [Architektur](docs/ARCHITECTURE.md), [Deployment](docs/DEPLOYMENT.md), [Rollback](docs/ROLLBACK.md), [Entscheidungen](docs/DECISIONS.md).
- `scripts/validate.py`: lokale Prüfung ohne externe Pakete.
- `logs/`: Session-Protokolle gemäß [Logregeln](logs/README.md).
- `backups/`: Referenzen und Manifeste; keine geheimen oder großen Backup-Dateien.

## Versionsquelle und Veröffentlichung

GitHub: https://github.com/felixAramea84/test, Hauptbranch `main`.
Änderungen bevorzugt über Feature-Branch, Review und kontrollierte Zusammenführung. Vor Push Diff, Secrets, Prüfungen und Zielbranch kontrollieren; danach Remote-SHA prüfen.

Sites und GitHub sind derzeit nicht nachweislich synchronisiert. Die Kandidatin „Test-Website“ ist in den Deployment-Dokumenten inventarisiert; die Repo-Zuordnung bleibt offen. Kein automatisches Deployment eingerichtet. `.openai/hosting.json` erst nach bestätigter Zuordnung anlegen. Vor jeder Sites-Änderung gelten die Backup-Gates aus `AGENTS.md`.
