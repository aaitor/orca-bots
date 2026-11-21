"""Repository checks: local doc links, SVGs, manifests, and pixel-exact redraws of the example avatars.

python3 scripts/check.py   (needs Pillow)
"""
import html
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/orca-bot-builder'
EXCLUDED = {'.git', '.venv', 'node_modules', '__pycache__'}
# The PNG each example's avatar.py must reproduce exactly: the avatar its owner picked.
CHOSEN = {
    'paco-the-releaser': 'round-2/2-skeptic-flannel.png',
    'sami-the-architect': 'round-2/4i-purple.png',
    'chani-the-marketer': 'round-1/2-bubblegum.png',
    'charo-the-admin': 'round-2/2f-angry-cat.png',
    'richard-the-dealmaker': 'round-2/2a-grin.png',
    'margo-the-doc-keeper': 'round-1/1-shush.png',  # built by the skill; its first recommendation
}


def check_files():
    errors = []
    for path in ROOT.rglob('*'):
        if any(part in EXCLUDED for part in path.relative_to(ROOT).parts) or not path.is_file():
            continue
        if path.suffix == '.svg':
            try:
                ET.parse(path)
            except ET.ParseError as exc:
                errors.append(f'{path.relative_to(ROOT)}: invalid SVG: {exc}')
        if path.suffix != '.md':
            continue
        text = re.sub(r'^(`{3,}|~{3,}).*?^\1[^\n]*$', '', path.read_text(), flags=re.M | re.S)
        links = re.findall(r'!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text)
        links += re.findall(r'(?:href|src)=["\x27]([^"\x27]+)', text)
        for link in links:
            parsed = urlsplit(html.unescape(link))
            if parsed.scheme or parsed.netloc or not parsed.path or '<' in link:
                continue
            target = (ROOT if parsed.path.startswith('/') else path.parent) / unquote(parsed.path).lstrip('/')
            if not target.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing target {link}')
    return errors


def check_manifests():
    errors = []
    plugin = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
    market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
    entry = next((p for p in market['plugins'] if p['name'] == plugin['name']), None)
    if not entry:
        errors.append('marketplace.json does not list the plugin in plugin.json')
    elif entry.get('version') != plugin.get('version'):
        errors.append('plugin.json and marketplace.json versions differ')
    for skill_md in ROOT.glob('skills/*/SKILL.md'):
        front = skill_md.read_text().split('---')[1]
        name = re.search(r'^name:\s*(\S+)', front, re.M)
        if not name or name.group(1) != skill_md.parent.name:
            errors.append(f'{skill_md.relative_to(ROOT)}: frontmatter name must be {skill_md.parent.name}')
        if 'description:' not in front:
            errors.append(f'{skill_md.relative_to(ROOT)}: missing description')
    return errors


def run(script, out):
    result = subprocess.run([sys.executable, str(script), str(out)], capture_output=True, text=True)
    return [] if result.returncode == 0 else [f'{script.relative_to(ROOT)} failed:\n{result.stderr}']


def same_pixels(a, b):
    return Image.open(a).convert('RGB').tobytes() == Image.open(b).convert('RGB').tobytes()


def check_avatars():
    errors = []
    examples = sorted(p.name for p in (SKILL / 'examples').iterdir() if (p / 'avatar.py').exists())
    if examples != sorted(CHOSEN):
        errors.append(f'examples with avatar.py {examples} do not match CHOSEN {sorted(CHOSEN)}')
    with tempfile.TemporaryDirectory(prefix='orca-bots-check-') as tmp:
        tmp = Path(tmp)
        for name, rel in CHOSEN.items():
            ex = SKILL / 'examples' / name
            failed = run(ex / 'avatar.py', tmp / name)
            errors += failed
            if not failed and not same_pixels(tmp / name / rel, ex / 'avatar.png'):
                errors.append(f'{name}: avatar.py no longer redraws avatar.png ({rel})')
        errors += run(SKILL / 'examples/paco-the-releaser/concepts.py', tmp / 'concepts')
        errors += run(SKILL / 'templates/avatar.py', tmp / 'template')
        out = tmp / 'template/round-1'
        if len(list(out.glob('*.png'))) < 5 or not (out / 'contact-sheet.png').exists():
            errors.append('templates/avatar.py: expected at least four concepts and a contact sheet')
    return errors


def main():
    errors = check_files() + check_manifests() + check_avatars()
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'ok: docs, manifests and {len(CHOSEN)} example avatars redraw pixel for pixel')
    return 0


if __name__ == '__main__':
    sys.exit(main())
