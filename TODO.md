# TODO

## Next up
Keine offenen Implementierungsaufgaben. Optionaler Abschluss: PR #1 reviewen/zusammenführen und Foto im autorisierten Browser visuell prüfen.

## In progress
Keine.

## Blocked
Keine Implementierung blockiert. Direkter main-Push durch automatische Freigabeprüfung abgelehnt; GitHub-Integration erfolgt über https://github.com/felixAramea84/test/pull/1.

## Done
- [x] T-001 | P1 | DONE | Repository gemäß Projektvorgabe konfigurieren.
  - Akzeptanz: AGENTS.md unverändert, Pflichtdateien vorhanden, lokale Prüfung erfolgreich und GitHub-Sicherung bestätigt.
  - Ergebnis: 2bab1c3afcf6dba100677b1008970c24d42121b5 auf main.
- [x] T-002 | P1 | DONE | Sites-Quellen identifizieren und dem GitHub-Projekt zuordnen.
  - Akzeptanz: Projekt und Remote bestätigt, Quellabweichung erklärt, bestehende Historie erhalten.
  - Ergebnis: Version 1 war eine eigenständige leere Sites-Seite; Quellen nun unter Erhaltung beider Historien verbunden.
- [x] T-003 | P1 | DONE | Wiederherstellbaren Live-Ausgangsstand remote sichern.
  - Akzeptanz: Deployment-Dateien aus veröffentlichter Quell-SHA rekonstruierbar, lokaler Archiv-Roundtrip bytegleich, GitHub-Backup-SHA bestätigt.
  - Ergebnis: 3c7de0c47a901482c57ff257c8ba9c3db49c2066; tatsächlicher Live-Restore nicht ausgeführt. Manifest backups/2026-10-23-pre-rathaus.json.
- [x] T-004 | P1 | DONE | Rathausfoto ergänzen und Test-Website veröffentlichen.
  - Akzeptanz: Foto, Alt-Text, Attribution/Lizenz, responsive Darstellung, GitHub-Sicherung und erfolgreiches Sites-Deployment.
  - Ergebnis: Quellcommit 914d8f89e301d0b4ef341fda682c8e42cf70e46e, Version 2 succeeded, Zugriff unverändert. Lokale HTML-/Struktur-/HTTP-Prüfung PASS; visueller Live-/Bildtest nicht verfügbar, direkte Live-HTTP-Prüfung URLError. Foto wird extern geladen.
