# Architektur

Eine statische `index.html` im Repository-Root, mit eingebettetem CSS. Keine Runtime-Abhängigkeiten, APIs, Persistenz oder Migrationen im GitHub-Stand. Der Browser rendert direkt das HTML.

Es werden keine ungenutzten `src/`, `tests/`, `public/` oder Framework-Dateien angelegt. Bei wachsendem Funktionsumfang Struktur, Prüfungen und Dokumentation gemeinsam erweitern.

GitHub ist die Versionsquelle. Sites verwendet ein separates Quell-Remote für dasselbe Projekt, gebunden über `.openai/hosting.json`. `scripts/prepare-static.py` kopiert die kanonische index.html nach dist/index.html. Das Rathausfoto wird extern von Wikimedia Commons geladen; kein JavaScript erforderlich. Siehe [Deployment](DEPLOYMENT.md).
