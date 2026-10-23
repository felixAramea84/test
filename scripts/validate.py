"""Check required documents and their relative links without dependencies."""
from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
required = ('AGENTS.md', 'README.md', 'HANDOFF.md', 'TODO.md', 'CHANGELOG.md',
            '.gitignore', '.env.example', 'index.html', 'docs/ARCHITECTURE.md',
            'docs/DEPLOYMENT.md', 'docs/ROLLBACK.md', 'docs/DECISIONS.md', 'logs/README.md')
errors = []
for name in required:
    path = root / name
    if not path.is_file() or not path.read_text(encoding='utf-8').strip():
        errors.append(f'Missing or empty required file: {name}')
for path in root.rglob('*.md'):
    if '.git' in path.relative_to(root).parts:
        continue
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        target = link.split('#', 1)[0]
        if not target or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
            continue
        if not (path.parent / target).is_file():
            errors.append(f'Broken link in {path.relative_to(root)}: {link}')
logs = list((root / 'logs/sessions').glob('*.md'))
if not logs:
    errors.append('No session log found')
manifests = list((root / 'backups').glob('*.json'))
if not manifests:
    errors.append('No backup manifest found')
for path in manifests:
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
        if not re.fullmatch(r'[0-9a-f]{40}', data.get('baseline_commit', '')):
            errors.append(f'Invalid baseline SHA: {path.name}')
    except (ValueError, TypeError) as exc:
        errors.append(f'Invalid manifest {path.name}: {exc}')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'PASS: {len(required)} required files, Markdown links, {len(logs)} session log(s), {len(manifests)} manifest(s)')
