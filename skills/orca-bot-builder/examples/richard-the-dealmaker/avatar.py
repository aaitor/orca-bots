"""Richard, the Dealmaker: charming silver fox in a navy suit, gold cufflinks, an instinct for money.

python3 richard.py [basedir]  -> round-1/ (6 concepts) and round-2/ (faces, looks, props), each with a contact-sheet.png
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'scripts'))  # pixelart.py
from pixelart import mirror, put, sym, sprite, scanlines, shift_left, render, contact_sheet

# K outline, S skin, N/s shadow, H/h hair+shine, G grey temples, b brows, w white, E eye,
# M mouth, J suit, j lapel, C shirt, T tie, t tie shine.
LEFT = [
    "................", "................", "................", "..........KKKKKK",
    "........KKHHHHHH", ".......KHHHHHHHH", "......KHHHHHHHHH", "......KHHHHHHHHH",
    ".....KGHHHHHHHHH", ".....KGHHSSSSSSS", ".....KGSSSSSSSSS", ".....KGSbbbbbSSS",
    "....KSSSSSSSSSSS", "....KSSSSwEEwSSS", "....KNSSSSSSSSSS", ".....KSSSSSSSSSS",
    ".....KSSSSSSSSNS", "......KSSSSSSSSS", "......KSSSSSSSSS", ".......KSSSSSSSS",
    ".......KSSSSSSMM", "........KSSSSSSS", ".........KSSSSSS", "..........KKSSSS",
    "...........KKCCC", "........KJJKCCCC", "......KJJJjKCCCT", "....KJJJJJJjKCCT",
    "...KJJJJJJJJjKCT", "..KJJJJJJJJJJjKC", "..KJJJJJJJJJJJjK", ".KJJJJJJJJJJJJJj",
]

PAL = {
    '.': '#2f6b52', ',': '#295f49',                                   # money green + scanlines
    'K': '#13161a', 'S': '#e8b08a', 's': '#c08766', 'N': '#c08766',
    'H': '#2a2320', 'h': '#5a4a40', 'G': '#b9b9bf', 'b': '#2a2320',
    'w': '#ffffff', 'E': '#2a1d14', 'M': '#7a3a32',
    'J': '#1f2a44', 'j': '#2e3d60', 'C': '#f2f2f2', 'T': '#8e1f2e', 't': '#b8344a',
    'Y': '#f2c94c', 'O': '#b8892a',                                   # gold
    'P': '#c8a2d8', 'R': '#8e1f2e',
    'D': '#141018', 'd': '#100c14',                                   # dark gallery / stage
    'F': '#c9a227', 'f': '#8a6a14',                                   # gilt frame
    '1': '#d94a3a', '2': '#2f6fb8', '3': '#f2c94c', '4': '#f2f2f2',   # the painting
    'V': '#6a1a28', 'v': '#9a2a3a',                                   # red wine
    'g': '#cfe8f0',                                                   # glass
    'X': '#e8e8ee',                                                   # music notes
    'Z': '#5d5650', 'z': '#9a948e',                                   # salt-and-pepper beard
    'L': '#1d2a3a', 'p': '#6a6e78', 'k': '#1a1a1e',                   # shades, pinstripe, turtleneck
}

SILVER = {'H': '#a9a9b0', 'h': '#e2e2e8', 'b': '#6a6a72', 'G': '#d8d8de'}
VELVET = {'J': '#5a1828', 'j': '#7a2a3a', 'T': '#13161a', 't': '#3a3a44'}
PINSTRIPE = {'J': '#34373f', 'j': '#50545e', 'C': '#cfe0f2', 'T': '#c9a227', 't': '#f2c94c'}
LINEN = {'J': '#cdb68c', 'j': '#b39b6e', '.': '#2a7f9e', ',': '#257390'}


def portrait():
    g = mirror(LEFT)
    put(g, 18, 5, "hhh"); put(g, 16, 6, "hh")                    # shine, combed to one side
    put(g, 11, 4, "KK"); put(g, 12, 5, "K")                      # side parting
    put(g, 19, 11, "bSSSb"); put(g, 20, 10, "bbb")               # one brow arched: the charming bit
    put(g, 13, 20, "SS"); put(g, 18, 20, "MM"); put(g, 19, 19, "M")  # half smile, one side up
    put(g, 15, 20, "MMM")
    for y in range(26, 32):                                      # tie runs down the middle
        put(g, 15, y, "TT")
    put(g, 15, 24, "TT"); put(g, 15, 25, "Tt")
    put(g, 7, 28, "C")                                           # pocket square
    put(g, 6, 28, "C"); put(g, 6, 29, "jC")
    return g


def finish(g, bg='.', odd=','):
    scanlines(g, range(32), bg, odd)
    return g


def behind(g, x0, y0, rows):
    """sprite() that only paints the background, so it sits behind him."""
    for dy, row in enumerate(rows):
        for dx, ch in enumerate(row):
            if ch != ' ' and g[y0 + dy][x0 + dx] == '.':
                g[y0 + dy][x0 + dx] = ch


def arm(g, x=24, top=22):
    """A hand coming up from the bottom edge: skin, white cuff with a gold cufflink, navy sleeve."""
    put(g, x, top, "KSSSK"); put(g, x, top + 1, "KSSSK")
    put(g, x, top + 2, "KCYCK")
    for y in range(top + 3, 32):
        put(g, x, y, "KJJJK")


# ---------- props ----------
def coin(g, x=25, y=9):
    """A gold coin mid-flip, with a glint and sparkles."""
    sprite(g, x, y, [" KKKK ", "KYwYYK", "KYYYOK", "KYYYOK", "KYOOOK", " KKKK "])
    behind(g, x - 1, y - 2, ["w"]); behind(g, x + 5, y - 3, ["w"]); behind(g, x + 6, y + 2, ["w"])


def wink(g):
    put(g, 19, 13, "KKKK")                                       # his left eye closed
    put(g, 18, 12, " ")
    put(g, 9, 13, "wEEw")


def moustache(g):
    put(g, 12, 18, "KHHHHHHK"); put(g, 11, 19, "KH"); put(g, 19, 19, "HK")


def bow_tie(g):
    for y in range(25, 32):
        put(g, 15, y, "CC")
    sprite(g, 12, 24, ["KK    KK", "KTKKKKTK", "KTTttTTK", "KTKKKKTK", "KK    KK"])


def frame(g):
    """Gilt frame around the whole picture: he is the painting."""
    for i in range(32):
        for x, y in ((i, 0), (i, 31), (0, i), (31, i)):
            g[y][x] = 'F'
        for x, y in ((i, 1), (i, 30), (1, i), (30, i)):
            if 1 <= i <= 30:
                g[y][x] = 'f'


# ---------- round 1 concepts ----------
def silver_fox():
    return render(finish(portrait()), PAL)


def coin_flip():
    g = portrait()
    shift_left(g, 2)
    coin(g)
    put(g, 25, 16, "KK"); put(g, 25, 17, "KSK")                 # thumb that flicked it
    put(g, 25, 18, "KSSSSK"); put(g, 25, 19, "KSSSSK"); put(g, 25, 20, "KCYCCK")
    for y in range(21, 32):
        put(g, 25, y, "KJJJJK")
    return render(finish(g), PAL)


def dollar_eyes():
    """Sees the deal before anyone else does."""
    g = portrait()
    for y in (10, 11):
        for x in range(32):
            if g[y][x] == 'b':
                g[y][x] = 'S'
    sym(g, 8, 10, "bbbbb")
    put(g, 9, 13, "SSSS"); put(g, 19, 13, "SSSS")
    for x in (9, 20):
        sprite(g, x, 11, [" O ", "YYY", "Y  ", "YYY", "  Y", "YYY", " O "])
    return render(finish(g), PAL)


def maestro():
    """Tuxedo, bow tie, baton up: conducting the deal."""
    g = portrait()
    for y in range(25, 32):
        for x in range(32):
            if g[y][x] in 'Jj':
                g[y][x] = 'D' if g[y][x] == 'J' else 'K'
    bow_tie(g)
    put(g, 6, 28, "DD"); put(g, 6, 29, "DD"); put(g, 7, 28, "D")
    shift_left(g, 2)
    for x, y in ((27, 21), (27, 20), (28, 19), (28, 18), (28, 17), (29, 16), (29, 15), (29, 14), (30, 13), (30, 12)):
        g[y][x] = 'X'
    put(g, 25, 22, "KSSSK"); put(g, 25, 23, "KCYCK")
    for y in range(24, 32):
        put(g, 25, y, "KDDDK")
    note = [" XX", " X ", " X ", "XX ", "XX "]
    behind(g, 1, 1, note); behind(g, 26, 2, note); behind(g, 1, 16, note)
    pal = dict(PAL, **{'.': '#6e1f2c', ',': '#601a26'})
    return render(finish(g), pal)


def gallery():
    """In a gilt frame, with an abstract over his shoulder: the collector."""
    g = portrait()
    shift_left(g, 2)
    behind(g, 24, 3, ["ffffff", "f11K2f", "f11K2f", "fKKKKf", "f3K44f", "ffffff"])
    frame(g)
    pal = dict(PAL, **{'.': '#3a2a3a', ',': '#33253a'})
    return render(finish(g), pal)


def red_wine():
    """A glass of red and a wink. Dinner is where deals close."""
    g = portrait()
    wink(g)
    shift_left(g, 2)
    sprite(g, 24, 12, ["KgggggK", "KvVVVvK", "KVVVVVK", " KVVVK ", "  KgK  ", "  KgK  ", "  KgK  "])
    arm(g, 25, 19)
    return render(finish(g), PAL)


CONCEPTS = [("1-silver-fox", silver_fox), ("2-coin-flip", coin_flip), ("3-dollar-eyes", dollar_eyes),
            ("4-maestro", maestro), ("5-gallery", gallery), ("6-red-wine", red_wine)]


# ---------- round 2: faces, looks, props ----------
def clear_mouth(g):
    for y in (19, 20, 21):
        for x in range(11, 21):
            if g[y][x] == 'M':
                g[y][x] = 'S'


def grin(g):
    clear_mouth(g)
    sym(g, 12, 20, "Mwww"); sym(g, 13, 21, "MMM"); sym(g, 11, 19, "M")


def side_eye(g):
    put(g, 9, 13, "wwEE"); put(g, 19, 13, "wwEE")
    put(g, 9, 12, "KKKK"); put(g, 19, 12, "KKKK")              # heavy lids: sly


def pencil_moustache(g):
    sym(g, 13, 19, "HHH")


def beard(g):
    for y in range(17, 24):
        for x in range(32):
            if g[y][x] == 'S' and (y >= 21 or x <= 11 or x >= 20):
                g[y][x] = 'z' if (x * 5 + y * 3) % 7 == 0 else 'Z'
    sym(g, 12, 19, "ZZZZ")


def glasses(g, c='O'):
    for x in (8, 18):
        put(g, x, 12, c * 6); put(g, x, 14, c * 6); put(g, x, 13, c); put(g, x + 5, 13, c)
    put(g, 14, 12, c * 4); put(g, 5, 12, c * 3); put(g, 24, 12, c * 3)


def aviators(g):
    lens = ["OOOOOO", "OLLLLO", "OLwLLO", " OLLO "]
    sprite(g, 8, 12, lens); sprite(g, 18, 12, [r[::-1] for r in lens])
    put(g, 14, 12, "OOOO"); put(g, 5, 12, "OOO"); put(g, 24, 12, "OOO")


def open_collar(g):
    for y in range(24, 32):
        put(g, 15, y, "CC")
    put(g, 15, 24, "SS"); put(g, 15, 25, "SS"); put(g, 15, 26, "ss")


def pinstripes(g):
    for y in range(25, 32):
        for x in range(32):
            if g[y][x] == 'J' and x % 3 == 0:
                g[y][x] = 'p'


def turtleneck(g):
    for y in range(24, 32):
        for x in range(32):
            if g[y][x] in 'CTt':
                g[y][x] = 'k'
    put(g, 13, 24, "KKKKKK")


def flute(g, x=25, y=9):
    sprite(g, x, y, ["KgggK", "KYwYK", "KYYYK", "KYYwK", "KwYYK", " KYK ", "  g  ", "  g  ", " ggg "])


def pen(g, x=27, y=8):
    sprite(g, x, y, [" Y ", "KYK", "KOK", "KDK", "KDK", "KYK", "KDK", "KDK", "KDK", "KDK", "KDK"])


def vinyl(g, cx=27, cy=11, r=4.3):
    import math
    for y in range(32):
        for x in range(32):
            d = math.hypot(x - cx, y - cy)
            if d < 0.8:
                g[y][x] = 'K'
            elif d < 1.9:
                g[y][x] = '1'
            elif d < r - 0.4:
                g[y][x] = 'd' if int(d * 2) % 2 else 'D'
            elif d < r + 0.5:
                g[y][x] = 'K'
    put(g, 25, 9, "w")


def look(face=None, pal=None, extra=None, prop=None, bg=None):
    g = portrait()
    for f in (face if isinstance(face, (list, tuple)) else [face] if face else []):
        f(g)
    for f in (extra or []):
        f(g)
    if prop:
        prop(g)
    p = dict(PAL, **(pal or {}))
    if bg:
        p.update({'.': bg[0], ',': bg[1]})
    return render(finish(g), p)


def holding(item, top=19, **kw):
    def draw(g):
        shift_left(g, 2)
        item(g, **kw)
        arm(g, 25, top)
    return draw


def record(g):
    shift_left(g, 2)
    vinyl(g)
    arm(g, 25, 18)
    note = [" XX", " X ", " X ", "XX ", "XX "]
    behind(g, 1, 1, note); behind(g, 1, 16, note)


ROUND2 = [
    ("2a-grin", lambda: look(grin)),
    ("2b-wink", lambda: look(wink)),
    ("2c-side-eye", lambda: look(side_eye)),
    ("2d-pencil-moustache", lambda: look(pencil_moustache)),
    ("2e-salt-pepper-beard", lambda: look(beard)),
    ("2f-full-silver", lambda: look(pal=SILVER)),
    ("2g-gold-glasses", lambda: look(glasses)),
    ("2h-velvet-jacket", lambda: look(extra=[bow_tie], pal=VELVET)),
    ("2i-pinstripe-gold-tie", lambda: look(extra=[pinstripes], pal=PINSTRIPE)),
    ("2j-turtleneck-glasses", lambda: look([glasses], extra=[turtleneck], bg=('#3a2a3a', '#33253a'))),
    ("2k-linen-aviators", lambda: look(aviators, extra=[open_collar], pal=LINEN)),
    ("2l-champagne-wink", lambda: look(wink, prop=holding(flute, 19), bg=('#22304f', '#1e2a46'))),
    ("2m-fountain-pen", lambda: look(prop=holding(pen, 19, x=26, y=8))),
    ("2n-vinyl", lambda: look(prop=record, bg=('#6e1f2c', '#601a26'))),
    ("2o-silver-beard-wine", lambda: look([beard, wink], pal=SILVER, prop=lambda g: (shift_left(g, 2), sprite(g, 24, 12, ["KgggggK", "KvVVVvK", "KVVVVVK", " KVVVK ", "  KgK  ", "  KgK  ", "  KgK  "]), arm(g, 25, 19)))),
]


def save(items, out):
    os.makedirs(out, exist_ok=True)
    for name, img in items:
        img.save(os.path.join(out, f"{name}.png"))
    contact_sheet(items, os.path.join(out, "contact-sheet.png"), cols=5 if len(items) > 6 else 3)
    print("ok", out)


if __name__ == '__main__':
    base_dir = sys.argv[1] if len(sys.argv) > 1 else HERE
    save([(name, draw()) for name, draw in CONCEPTS], os.path.join(base_dir, 'round-1'))
    save([(name, draw()) for name, draw in ROUND2], os.path.join(base_dir, 'round-2'))
