# Architektur

Eine statische `index.html` im Repository-Root, mit eingebettetem CSS. Keine Runtime-Abhängigkeiten, APIs, Persistenz oder Migrationen im GitHub-Stand. Der Browser rendert direkt das HTML.

Es werden keine ungenutzten `src/`, `tests/`, `public/` oder Framework-Dateien angelegt. Bei wachsendem Funktionsumfang Struktur, Prüfungen und Dokumentation gemeinsam erweitern.

GitHub ist die Versionsquelle. Sites verwaltet eigene Quellstände und gespeicherte Versionen; die Verknüpfung dieses Repositories mit einer Site ist noch nicht bestätigt. Siehe [Deployment](DEPLOYMENT.md).
