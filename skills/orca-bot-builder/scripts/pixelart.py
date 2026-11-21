"""Arcade pixel-art avatars: 32x32 character grids rendered to crisp PNGs. Method: references/avatars.md.

A grid is a list of 32 lists of 32 single-char cells; a palette maps each char to a hex colour.
"""
import os

from PIL import Image, ImageDraw


def mirror(left):
    """32 rows of the LEFT 16 columns -> a symmetric 32x32 grid."""
    assert len(left) == 32, len(left)
    for r in left:
        assert len(r) == 16, (len(r), r)
    return [list(r + r[::-1]) for r in left]


def put(g, x, y, s):
    """Write s into row y from column x. ' ' is transparent."""
    for i, ch in enumerate(s):
        if ch != ' ':
            g[y][x + i] = ch


def sym(g, x, y, s):
    """put() s at x and its mirror image on the other side."""
    put(g, x, y, s)
    put(g, 32 - x - len(s), y, s[::-1])


def sprite(g, x0, y0, rows):
    """put() several rows, top-left at (x0, y0)."""
    for dy, row in enumerate(rows):
        put(g, x0, y0 + dy, row)


def scanlines(g, rows, src, dst):
    """Swap src for dst on odd rows: the CRT scanline look."""
    for y in rows:
        if y % 2:
            g[y] = [dst if c == src else c for c in g[y]]


def behind(g, x0, y0, rows, bg='.', odd=','):
    """sprite() that paints only background cells (plain or scanline), so the prop sits behind the head."""
    for dy, row in enumerate(rows):
        for dx, ch in enumerate(row):
            if ch != ' ' and g[y0 + dy][x0 + dx] in (bg, odd):
                g[y0 + dy][x0 + dx] = ch


def finish(g, bg='.', odd=','):
    """Scanlines over the whole background; call last, after props."""
    scanlines(g, range(32), bg, odd)
    return g


def shift_left(g, n=2, bg='.', bg_odd=','):
    """Move the picture left to free columns on the right (room for smoke, props)."""
    for y, row in enumerate(g):
        g[y] = row[n:] + [bg_odd if y % 2 else bg] * n


def render(g, pal, scale=16):
    """Grid -> RGB image, scaled with NEAREST so pixels stay crisp (32 * 16 = 512px)."""
    img = Image.new('RGB', (32, 32))
    px = img.load()
    for y in range(32):
        for x in range(32):
            h = pal[g[y][x]].lstrip('#')
            px[x, y] = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    return img.resize((32 * scale, 32 * scale), Image.NEAREST)


def contact_sheet(items, path, cols=6):
    """items: [(name, img)]. Each at 256px plus a round 40px preview, which is how Orca shows avatars."""
    W, H = 290, 330
    rows = (len(items) + cols - 1) // cols
    sheet = Image.new('RGB', (W * min(cols, len(items)), H * rows), (245, 245, 245))
    d = ImageDraw.Draw(sheet)
    for i, (name, img) in enumerate(items):
        x, y = (i % cols) * W + 17, (i // cols) * H + 15
        sheet.paste(img.resize((256, 256), Image.NEAREST), (x, y))
        small = img.resize((40, 40), Image.LANCZOS)
        mask = Image.new('L', (40, 40), 0)
        ImageDraw.Draw(mask).ellipse((0, 0, 39, 39), fill=255)
        sheet.paste(small, (x, y + 266), mask)
        d.text((x + 50, y + 280), name, fill=(20, 20, 20))
    sheet.save(path)


def save(items, out, cols=None):
    """Write each (name, img) as <out>/<name>.png plus <out>/contact-sheet.png."""
    os.makedirs(out, exist_ok=True)
    for name, img in items:
        img.save(os.path.join(out, f"{name}.png"))
    contact_sheet(items, os.path.join(out, "contact-sheet.png"), cols=cols or (5 if len(items) > 6 else 3))
    print("ok", out)


def html_page(sheets, path, title):
    """sheets: [(caption, png_path)] -> one self-contained HTML page (images inlined), e.g. for an Orca inline visual."""
    import base64
    import html
    parts = [f"<!doctype html><meta charset='utf-8'><title>{html.escape(title)}</title>"
             "<body style='margin:0;padding:16px;font-family:var(--font-sans,sans-serif);"
             "background:var(--background,#fff);color:var(--foreground,#171717)'>"]
    for caption, png in sheets:
        with open(png, 'rb') as f:
            data = base64.b64encode(f.read()).decode()
        parts.append(f"<h3>{html.escape(caption)}</h3>"
                     f"<img alt='{html.escape(caption)}' style='max-width:100%;image-rendering:pixelated' "
                     f"src='data:image/png;base64,{data}'>")
    with open(path, 'w') as f:
        f.write(''.join(parts))
