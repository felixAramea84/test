# Deployment

## Inventar, Stand 2026-10-23 15:41 CEST

Repository: `felixAramea84/test`, Hauptbranch `main`.
GitHub-Ausgangscommit: `d0b6ec1d45667ff5e6d73851cf3d4163962e69a9`.

Sites-Kandidatin: „Test-Website“ (Zuordnung zum Repository nicht bestätigt).
- Projekt-ID: `appgprj_6adb5adde3a0819186797112638e6c1d`.
- URL: https://leere-testseite-fh-231026.arbeitsberei-5761.chatgpt.site
- Gespeicherte Version: 1, ID `appgprj_6adb5adde3a0819186797112638e6c1d~appgver_2b3adb6efc1c81919846bd9a91b52a59`.
- Quellcommit der Sites-Version: `7868b213ea3282c2699531842e0478a09195b02e`.
- Deployment: `appgdep_6adb5b0fba608191bb8161c735f96dd1`, Status `succeeded`, aktualisiert 2026-10-23 15:04:25 CEST (13:04:25 UTC).
- Zugriff: benutzerbeschränkt (`custom`); kein öffentliches Hosting zugesagt.

Version und erfolgreicher Veröffentlichungsstatus wurden über Sites gelesen. Der letzte Status-Zeitpunkt ist kein separat belegter Startzeitpunkt. Browser-/Live-Smoke-Test in dieser Konfigurationssession: NOT RUN. Keine Website geändert oder neu veröffentlicht. ARAMEA Market Monitor ist nicht diesem Repository zugeordnet und nicht Gegenstand der Konfiguration.

## Ablauf für ein späteres Sites-Update

1. Zuordnung bestätigen; aktuelle Site, veröffentlichte Version, gespeicherte Zwischenstände und Git-Status neu prüfen.
2. Live-Version inklusive nur in Sites vorhandener Quellen exportieren, Integrität und Wiederherstellbarkeit prüfen. Das vorhandene Archiv ist bisher nur als Referenz erfasst; Export/Restore noch nicht geprüft.
3. Wiederherstellbaren Ausgangsstand nach GitHub committen und pushen, Remote-SHA prüfen und Manifest in `backups/` ergänzen. Vorherige Version und Commit eindeutig referenzieren.
4. Zieländerung auf Feature-Branch implementieren, prüfen und remote sichern. Alten und neuen Stand remote belegen.
5. Erst nach erfüllten Gates die Integration gemäß aktuellen Sites-Werkzeugen/Skill einrichten und genau den gesicherten Quellstand veröffentlichen. Zugriffsmodus erhalten. Nötige Freigaben gemäß Auftrag und Integrationsregeln beachten.
6. Deployment-Status bis zum Endzustand prüfen; URL, Hauptfunktion, Assets, Navigation, Konsole und Mobilansicht testen. HANDOFF, TODO und Session-Log aktualisieren, committen und Remote-Verifikation durchführen.

**Sperre:** Ohne belegtes GitHub-Backup und rekonstruierbaren bisherigen Sites-Stand kein automatisches Sites-Update. Hier ist keine automatische Deploy-Pipeline eingerichtet. [Rollback](ROLLBACK.md) beachten.

## Aktualisierung 2026-10-23 – bestätigte Zuordnung und Backup

„Test-Website“ wird im aktuellen Auftrag bewusst diesem GitHub-Projekt zugeordnet. Das vorhandene Sites-Quell-Remote wurde authentifiziert geklont; HEAD entspricht exakt der veröffentlichten Version-1-SHA. Es enthält nur .openai/hosting.json und eine leere dist/index.html. Die historische Abweichung zur GitHub-Seite ist damit erklärt.

Pre-Deployment-Backup auf GitHub: `3c7de0c47a901482c57ff257c8ba9c3db49c2066`, Branch `feature/rathaus-foto`. Beide Deployment-Dateien sind dort unverändert gesichert. Aus der verifizierten Quell-SHA wurde ein tar-Archiv rekonstruiert, dessen Inhalte byteweise mit git show verglichen wurden. Manifest: [Pre-Rathaus](../backups/2026-10-23-pre-rathaus.json). Der alte Sediment-Download war nicht auflösbar; die exakten statischen Dateien sind über Git rekonstruierbar. Kein Live-Restore ausgeführt.

Lokales Packaging: `python3 scripts/prepare-static.py`, danach `python3 scripts/validate.py`; Archiv enthält ausschließlich .openai/hosting.json und dist/index.html. Vor Veröffentlichung Zielcommit auf GitHub UND das konfigurierte Sites-Quell-Remote pushen und Remote-SHAs verifizieren. Publikum bleibt ausschließlich der bisherige Eigentümer. Sites-Version und Deployment-Ergebnis werden nach Veröffentlichung in HANDOFF und Session-Log ergänzt.

Der Sites-Workflow-Helper ist in dieser Ausführungsumgebung nicht installiert und auch nicht als Skill-Ressource verfügbar. Fallback: gewöhnliches Git mit kurzlebiger Authentifizierung nur im Prozessspeicher sowie natives Sites-Speichern/Veröffentlichen mit lokalem tar-Archiv. Keine Zugangsdaten auf Platte oder in Git.

## Veröffentlichtes Rathaus-Update

Version 2: appgprj_6adb5adde3a0819186797112638e6c1d~appgver_2313f71bd6f48191bdd15c1e74f67984. Quellcommit 914d8f89e301d0b4ef341fda682c8e42cf70e46e. Deployment appgdep_6adb673811d88191b6c535b53c291497 succeeded, 2026-10-23 15:55:18 CEST. Lokaler HTTP-/Archiv-Test PASS; direkte Live-HTTP-Prüfung URLError; visuelle Bildprüfung nicht verfügbar. GitHub-Quellstand auf feature/rathaus-foto, PR #1 offen; main wegen abgelehntem Direkt-Push unverändert. Dokumentationscommit nach dem Release braucht keine erneute Sites-Veröffentlichung.
