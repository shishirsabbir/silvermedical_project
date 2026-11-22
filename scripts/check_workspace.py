"""Check organization integrity without dependencies, network access or writes."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'.local', '.git', 'node_modules', '__pycache__', '.venv', 'venv', '.next', '.open-next', '.wrangler', 'dist', 'build'}
LINKS = re.compile(r'\]\(([^\s)]+)\)|(?:href|src)=["\x27]([^"\x27]+)["\x27]')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-migration', action='store_true', help='Also compare original artifact hashes; intended for the initial migration check before intentional rebuilds.')
    args = parser.parse_args()
    errors = []
    counts = dict(local_links=0, json_files=0, python_files=0, preserved_artifacts=0)
    for path in ROOT.rglob('*'):
        if not path.is_file() or any(part in EXCLUDED for part in path.relative_to(ROOT).parts):
            continue
        suffix = path.suffix.lower()
        if suffix not in {'.md', '.html', '.json', '.py'}:
            continue
        relative = path.relative_to(ROOT).as_posix()
        try:
            text = path.read_text(encoding='utf-8-sig')
            if suffix == '.json':
                json.loads(text)
                counts['json_files'] += 1
            elif suffix == '.py':
                compile(text, relative, 'exec')
                counts['python_files'] += 1
            else:
                if suffix == '.md':
                    # Code examples can contain runtime URLs that have no local file.
                    text = re.sub(r'^ {0,3}```[^\n]*\n[\s\S]*?^ {0,3}```[ \t]*$', '', text, flags=re.MULTILINE)
                for match in LINKS.finditer(text):
                    target = match[1] or match[2]
                    parsed = urlsplit(target)
                    if parsed.scheme or parsed.netloc or not parsed.path:
                        continue
                    counts['local_links'] += 1
                    resolved = (path.parent / unquote(parsed.path)).resolve()
                    if not resolved.exists():
                        errors.append(f'{relative}: missing link {target}')
        except (ValueError, SyntaxError, UnicodeError) as exc:
            errors.append(f'{relative}: {exc}')

    manifest = json.loads((ROOT/'docs/development/FILE_MOVES.json').read_text(encoding='utf-8'))
    for item in manifest['files']:
        if item['new'].startswith('.local/') and not args.verify_migration:
            continue
        path = ROOT/item['new']
        if not path.is_file():
            errors.append(f'Migration destination missing: {item["new"]}')
            continue
        if args.verify_migration and (path.suffix.lower() in {'.pdf', '.png', '.pyc', '.exe', '.dll', '.zip'} or item['new'].startswith('.local/')):
            with path.open('rb') as source:
                actual = hashlib.file_digest(source, 'sha256').hexdigest()
            if actual != item['sha256_before']:
                errors.append(f'Migrated artifact changed: {item["new"]}')
            counts['preserved_artifacts'] += 1
    print(json.dumps(dict(checks=counts, errors=errors), indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
