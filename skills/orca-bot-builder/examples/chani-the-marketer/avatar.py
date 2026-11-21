"""La Chani, the Marketer: 21, disco queen, high ponytail, gold hoops, winged liner, zero filter.

python3 chani.py [basedir]  -> round-1/ (8 concepts) with a contact-sheet.png
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'scripts'))  # pixelart.py
from pixelart import mirror, put, sym, sprite, scanlines, shift_left, render, contact_sheet

# K outline, S skin, N/s shadow, H/h hair+shine, b brows, w white, E iris, R/P lips, p blush, T top.
LEFT = [
    "................", "................", "................", "...........KKKKK",
    ".........KKHHHHH", "........KHHHHHHH", ".......KHHHHHHHH", ".......KHHHHHHHH",
    "......KHHHHHHHHH", "......KHHHHSSSSS", "......KHHbbbbSSS", "......KHSSSSSSSS",
    "......KHKSSSSSSS", "....KSSSSKKKKKSS", "....KSSSSwEEwSSS", "....KNSSSSSSSSSS",
    ".....KSSppSSSSSS", "......KSSSSSSSNS", "......KSSSSSSSSS", ".......KSSSSSRRR",
    ".......KSSSSSPPP", "........KSSSSSSS", ".........KSSSSSS", "..........KKSSSS",
    "...........KKsss", "............Ksss", ".......KTTTTTKss", ".....KTTTTTTTTKs",
    "....KTTTTTTTTTTK", "...KTTTTTTTTTTTT", "..KTTTTTTTTTTTTT", "..KTTTTTTTTTTTTT",
]

PAL = {
    '.': '#8e3a8e', ',': '#7d3280',                                   # magenta background + scanlines
    'K': '#1a0f1e', 'S': '#e3a273', 's': '#b97852', 'N': '#b97852',
    'H': '#2b1810', 'h': '#6a4430', 'b': '#2b1810',
    'w': '#ffffff', 'E': '#3a2012', 'R': '#c2185b', 'P': '#ff4f9a', 'p': '#f0907a',
    'X': '#ff69b4', 'x': '#d63f8c', 'Y': '#ffd23f', 'O': '#c9961a',
    'T': '#b8b8cc', 't': '#ffffff',                                   # silver sequins
    'G': '#ffb3dc', 'M': '#5c1030', 'r': '#e8304a', 'I': '#9aa0ad', 'c': '#e4e8f0', 'L': '#7fe0ff',
    'D': '#2a1240', 'd': '#24103a',                                   # dark disco background
    '1': '#ff4fd8', '2': '#4fd8ff', '3': '#ffe14f', '4': '#7dff6a',   # disco light spots
    'A': '#d9a650', 'k': '#3b2414',                                   # leopard
}

HOOP = ["  YY  ", " Y  Y ", "Y    Y", "Y    Y", "O    O", " O  O ", "  OO  "]


def portrait():
    g = mirror(LEFT)
    put(g, 11, 5, "hhh"); put(g, 9, 6, "hh"); put(g, 8, 7, "h")   # slicked-back shine, one side
    for y in range(26, 32):                                     # sequins
        for x in range(32):
            if g[y][x] == 'T' and (x + 2 * y) % 4 == 0:
                g[y][x] = 't'
    return g


def pony(g):
    """High ponytail with a pink scrunchie, bouncing off to her left."""
    tail = {0: (17, "KKKKKK"), 1: (13, "KXXXXKHHhHHK"), 2: (13, "KXxXxK"), 3: (24, "KHhHK"),
            4: (25, "KHhHK"), 5: (25, "KHhHK"), 6: (25, "KHhHK"), 7: (25, "KHhHK"), 8: (25, "KHhHK"),
            9: (25, "KHhHK"), 10: (25, "KHhHK"), 11: (26, "KHhK"), 12: (27, "KHK"), 13: (28, "K")}
    for y, (x, s) in tail.items():
        put(g, x, y, s)
    put(g, 23, 2, "KHhHK")


def hoops(g, y=16):
    sprite(g, 1, y, HOOP)
    sprite(g, 25, y, HOOP)


def finish(g, bg='.', odd=','):
    scanlines(g, range(32), bg, odd)
    return g


def base():
    g = portrait()
    pony(g)
    hoops(g)
    return g


# ---------- round 1 concepts ----------
def hoops_pony():
    return render(finish(base()), PAL)


def bubblegum():
    """Pink gum bubble, mid-sentence."""
    g = base()
    cx, cy, r = 16, 21, 3.6
    for y in range(32):
        for x in range(32):
            d = math.hypot(x - cx, y - cy)
            if d < r - 0.6:
                g[y][x] = 'G'
            elif d < r + 0.4:
                g[y][x] = 'x'
    put(g, 14, 19, "w"); put(g, 13, 20, "w")
    return render(finish(g), PAL)


def disco_ball():
    """Under the mirror ball: dark club, coloured light spots."""
    g = base()
    put(g, 4, 0, "K")
    cx, cy, r = 4, 4.5, 3.6
    for y in range(9):
        for x in range(9):
            d = math.hypot(x - cx, y - cy)
            if d < r - 0.5:
                g[y][x] = 'w' if (x + y) % 3 == 0 else ('c' if (x * y) % 2 else 'I')
            elif d < r + 0.5:
                g[y][x] = 'K'
    for x, y, c in ((10, 1, '1'), (29, 17, '2'), (1, 12, '3'), (30, 2, '4'), (22, 0, '2'),
                    (0, 25, '1'), (31, 24, '3'), (8, 24, '4'), (24, 23, '1')):
        if g[y][x] in '.,':
            g[y][x] = c
    return render(finish(g, '.', ','), dict(PAL, **{'.': '#2a1240', ',': '#24103a'}))


def selfie():
    """Phone up, nails out, going live."""
    g = base()
    shift_left(g, 2)
    sprite(g, 24, 10, ["KKKKKKK", "KLLLLrK", "KLLLLLK", "KLwLLLK", "KLLLLLK", "KLLLLLK",
                       "KLLLLLK", "KLLLLLK", "KLLLLLK", "KKKKKKK"])
    for y in (13, 15, 17):                                      # fingers, pink nails
        put(g, 22, y, "KSX")
    put(g, 30, 14, "X")                                         # thumb
    for y in range(20, 32):                                     # forearm
        put(g, 25, y, "KSSSK")
    return render(finish(g), PAL)


def megaphone():
    """Announcing something. Loudly."""
    g = base()
    put(g, 12, 19, "KMMMMMMK"); put(g, 12, 20, "PMMMMMMP"); put(g, 13, 21, "PPPPPP")
    for x in range(18, 31):
        h = 1 + (x - 18) * 0.42
        for y in range(32):
            if abs(y - 20) <= h:
                edge = abs(y - 20) > h - 1 or x in (18, 30)
                g[y][x] = 'K' if edge else ('w' if x >= 28 else 'r')
    for y in (23, 24, 25):
        put(g, 21, y, "KIK")
    return render(finish(g), PAL)


def afro_disco():
    """Seventies volume: a curl cloud and a gold headband."""
    g = portrait()
    cx, cy, r = 15.5, 10, 14.2
    for y in range(26):
        for x in range(32):
            d = math.hypot(x - cx, (y - cy) * 1.1)
            if d < r and g[y][x] in '.,':
                g[y][x] = 'h' if (x * 3 + y * 5) % 7 == 0 else 'H'
            elif d < r + 0.8 and g[y][x] in '.,':
                g[y][x] = 'K'
    for x in range(8, 24):
        if g[8][x] in 'Hh':
            g[8][x] = 'Y'
    put(g, 7, 8, "Y"); put(g, 24, 8, "Y")
    hoops(g)
    return render(finish(g), PAL)


def bun_leopard():
    """Tight top bun and a leopard top: the full Chani."""
    g = portrait()
    cx, cy, r = 15.5, 1.6, 2.9
    for y in range(5):
        for x in range(32):
            d = math.hypot(x - cx, y - cy)
            if d < r - 0.4:
                g[y][x] = 'h' if (x, y) in ((14, 1), (15, 0)) else 'H'
            elif d < r + 0.5 and g[y][x] in '.,':
                g[y][x] = 'K'
    put(g, 13, 3, "XXXXXX")
    hoops(g)
    for y in range(26, 32):
        for x in range(32):
            if g[y][x] in 'Tt':
                g[y][x] = 'A'
    for x, y in ((5, 29), (9, 27), (12, 30), (19, 30), (22, 27), (26, 29), (8, 31), (24, 31), (16, 31)):
        if g[y][x] == 'A':
            g[y][x] = 'k'
            for dx, dy in ((1, 0), (0, 1)):
                if y + dy < 32 and g[y + dy][x + dx] == 'A':
                    g[y + dy][x + dx] = 'k'
    return render(finish(g), PAL)


def heart_shades():
    """Pink heart sunglasses, zero regrets."""
    g = base()
    heart = [" XX XX ", "XXXXXXX", "XXwXXXX", " XXXXX ", "  XXX  ", "   X   "]
    sprite(g, 7, 11, heart); sprite(g, 18, 11, heart)
    put(g, 14, 12, "KKKK")
    return render(finish(g), PAL)


CONCEPTS = [("1-hoops-pony", hoops_pony), ("2-bubblegum", bubblegum), ("3-disco-ball", disco_ball),
            ("4-selfie", selfie), ("5-megaphone", megaphone), ("6-afro-disco", afro_disco),
            ("7-bun-leopard", bun_leopard), ("8-heart-shades", heart_shades)]


def save(items, out):
    os.makedirs(out, exist_ok=True)
    for name, img in items:
        img.save(os.path.join(out, f"{name}.png"))
    contact_sheet(items, os.path.join(out, "contact-sheet.png"), cols=4)
    print("ok", out)


if __name__ == '__main__':
    base_dir = sys.argv[1] if len(sys.argv) > 1 else HERE
    save([(name, draw()) for name, draw in CONCEPTS], os.path.join(base_dir, 'round-1'))
