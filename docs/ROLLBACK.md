# Rollback

## Repository

Gesicherter Zustand vor der Konfiguration: Commit `d0b6ec1d45667ff5e6d73851cf3d4163962e69a9` auf https://github.com/felixAramea84/test.

Zur Untersuchung sicher separat auschecken:

```sh
git fetch origin
git worktree add --detach ../test-restore d0b6ec1d45667ff5e6d73851cf3d4163962e69a9
```

Das ist eine lokale Wiederherstellung zur Prüfung, keine Veröffentlichung. Bei beabsichtigter Rücknahme der Konfiguration auf neuem Branch `git revert <konfigurations-commit>` verwenden, Diff/Checks prüfen und kontrolliert integrieren. Die SHA dieses Commits aus dem GitHub-Verlauf bzw. finalen Session-Bericht beziehen. Kein `reset --hard`, Force-Push oder History-Rewrite als Standard.

## Sites

Für die Kandidatin „Test-Website“ existiert die gespeicherte Version 1 (`appgprj_6adb5adde3a0819186797112638e6c1d~appgver_2b3adb6efc1c81919846bd9a91b52a59`), mit Quell-SHA `7868b213ea3282c2699531842e0478a09195b02e`. Archiv-Referenz: [Bestandsmanifest](../backups/2026-10-23-baseline.json).

Die Sites-Werkzeuge bieten Veröffentlichung gespeicherter Versionen. Eigentümer-/Editorrechte, aktuelle Zugriffsregeln und erneut geprüfte IDs sind erforderlich. Eine frühere bekannte Version kann erneut veröffentlicht werden, sofern sie verfügbar ist und die Backup-Gates erfüllt sind. Quellarchiv, Codeabgleich und tatsächlicher Restore sind noch nicht verifiziert. Der GitHub-Ausgangscommit darf nicht als identisch mit der Sites-Live-Version angenommen werden.

Vor einer Wiederveröffentlichung: Site-Zuordnung bestätigen, aktuellen Stand sichern, richtige gespeicherte Version prüfen und Freigabe im Auftragskontext klären. Danach Deployment-Status und Live-Smoke-Test ausführen, Ergebnis dokumentieren. Kein erfolgreicher Rollback ohne diese Prüfung. Datenbank-/Content-Backups separat ergänzen, sobald solche Komponenten existieren.
