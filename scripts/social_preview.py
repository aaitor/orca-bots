"""Render assets/social-preview.png (1280 x 640): title, tagline and the five example avatars.

python3 scripts/social_preview.py   (needs Pillow; uses DejaVu fonts when installed)
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / 'skills/orca-bot-builder/examples'
BOTS = [('paco-the-releaser', 'Paco', 'the Releaser'), ('sami-the-architect', 'Sami', 'the Architect'),
        ('chani-the-marketer', 'La Chani', 'the Marketer'), ('charo-the-admin', 'Charo', 'the Admin'),
        ('richard-the-dealmaker', 'Richard', 'the Dealmaker')]


def font(size, bold=False):
    name = 'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'
    try:
        return ImageFont.truetype(name, size)
    except OSError:  # ponytail: no DejaVu, Pillow's default font; fine for a local asset
        return ImageFont.load_default(size)


def main():
    img = Image.new('RGB', (1280, 640), '#101827')
    d = ImageDraw.Draw(img)
    d.text((60, 48), 'Orca Bots', font=font(76, True), fill='#F4F7FB')
    d.text((64, 148), 'Teammate bots for Orca, with a soul and a pixel-art face.', font=font(30), fill='#89E5CC')
    for i, (slug, name, role) in enumerate(BOTS):
        x = 60 + i * 240
        img.paste(Image.open(EXAMPLES / slug / 'avatar.png').convert('RGB').resize((200, 200), Image.NEAREST), (x, 240))
        d.text((x + 100, 460), name, font=font(28, True), fill='#F4F7FB', anchor='mt')
        d.text((x + 100, 500), role, font=font(22), fill='#9CAEC4', anchor='mt')
    d.text((1220, 592), 'github.com/aaitor/orca-bots', font=font(20), fill='#9CAEC4', anchor='rs')
    img.save(ROOT / 'assets/social-preview.png')


if __name__ == '__main__':
    main()
