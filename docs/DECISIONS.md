# Entscheidungen

## 2026-10-23 – Schlanke Projektbasis

Die gelieferte Vorgabe wird unverändert als `AGENTS.md` abgelegt. Dokumentation und Struktur orientieren sich am vorhandenen statischen HTML-Projekt. Keine Framework-Migration, leeren Standardordner oder neuen Paketabhängigkeiten.

Die Konfiguration wird als ein atomarer, auf dem vorhandenen Commit aufbauender GitHub-Commit auf `main` abgeschlossen. Der vorherige Commit bleibt unverändert erreichbar. Die kleine Erstkonfiguration wird vor Veröffentlichung lokal geprüft; zukünftige Funktionsänderungen bevorzugen Feature-Branches und Review.

## 2026-10-23 – Sites-Zuordnung offen

„Test-Website“ ist eine plausible Kandidatin, aber ihre Quell-SHA weicht von GitHub ab. Deshalb kein Hosting-Binding und keine automatische Veröffentlichung. Ein erreichbarer gespeicherter Stand ist noch kein getesteter Restore. Vor einem späteren Sites-Update Zuordnung, Export, GitHub-Sicherung und Wiederherstellbarkeit belegen.
