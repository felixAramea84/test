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

Sites-Projekt „Test-Website“ ist über `.openai/hosting.json` zugeordnet. `index.html` bleibt die kanonische Quelle. `python3 scripts/prepare-static.py` erzeugt die identische Deployment-Datei `dist/index.html`. GitHub und das separate Sites-Quell-Remote erhalten vor Veröffentlichung denselben identifizierten Stand. Keine Veröffentlichung bei gewöhnlichen GitHub-Pushes. Details und Backup-Gates in `docs/DEPLOYMENT.md` und `AGENTS.md`.

Das Rathausfoto wird unverändert von Wikimedia Commons geladen; es benötigt Internetzugang zu `upload.wikimedia.org`. Urheber: Arnoldius, Lizenz CC BY-SA 4.0; Bildquelle und Lizenz sind auf der Seite verlinkt. Die Ausführungsumgebung erlaubt keinen Bilddownload von Wikimedia; die Website bindet das verifizierte Original direkt ein.
