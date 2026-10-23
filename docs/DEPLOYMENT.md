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
