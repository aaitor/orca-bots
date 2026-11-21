"""Sami, the Architect: nerdy senior architect, ponytail, thick glasses, sci-fi everything.

python3 sami.py [basedir]  -> round-1/ (5 concepts) and round-2/ (faces on 1 and 4, sabers, robe), each with a contact-sheet.png
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'scripts'))  # pixelart.py
from PIL import Image
from pixelart import mirror, put, sym, sprite, scanlines, shift_left, render, contact_sheet

# K outline, S skin, N/s shadow, A/a hair+beard, b brows, B glasses, L lens, E eye, M mouth, T shirt.
LEFT = [
    "................", "................", "..........KKKKKK", "........KKAAAAAA",
    ".......KAAAAAaAA", "......KAAAAaAAAA", "......KAAAaAAAAA", ".....KAAAaAAAAAA",
    ".....KAAASSSSSSS", ".....KAASSSSSSSS", "....KAASbbbbbbSS", "....KASBBBBBBBSS",
    "...KSASBLLEELBBB", "...KNASBLLEELBSS", "...KSASBLLLLLBSS", "....KASBBBBBBBSS",
    "....KASSSSSSSSNS", "....KAASSSSSSSSS", "....KAAASSSSSAAA", "....KAAAASSSAAAA",
    "....KAAAASSSSMMM", ".....KAAAASSSAAA", ".....KAAAAAAAAAA", "......KAAAAAAAAA",
    "......KsKAAAAAAA", ".......KsKKAAAAA", "...KTTTKsssKKKKK", "..KTTTTTKssssssK",
    ".KTTTTTTTKKsssss", ".KTTTTTTTTTKKKKK", "KTTTTTTTTTTTTTTT", "KTTTTTTTTTTTTTTT",
]

PAL = {
    '.': '#1f5560', ',': '#1a4952',                                   # teal background + scanlines
    'K': '#141220', 'S': '#eaa97e', 's': '#c27f5c', 'N': '#c27f5c',
    'A': '#3b2a20', 'a': '#6a4a35', 'b': '#241a14', 'g': '#8a8a8a',
    'B': '#141220', 'L': '#8fd6ff', 'w': '#ffffff', 'E': '#141220', 'M': '#5c2232',
    'T': '#1c1c24', 't': '#34343f', 'Y': '#ffd23f', 'X': '#ff4d4d',
    'Q': '#45ff6e', 'I': '#9aa0ad', 'i': '#5a606d', 'c': '#d8e4f0', 'D': '#7a4a24', 'O': '#d9a441',
    '*': '#c8c8ff',
    'h': '#26262e', 'j': '#4a4a58', 'G': '#a3a3a8',                    # headphones, grey hair
    'R': '#6b4a2b', 'r': '#4e3520', 'U': '#d9c8a0', 'u': '#b3a27c',    # robe, tunic
}
SABERS = {'green': '#45ff6e', 'red': '#ff3b3b', 'blue': '#4da6ff', 'purple': '#b34dff'}

FOUR = ["Y Y", "Y Y", "YYY", "  Y", "  Y"]
TWO = ["YYY", "  Y", "YYY", "Y  ", "YYY"]


def portrait():
    g = mirror(LEFT)
    put(g, 8, 12, "w"); put(g, 19, 12, "w")                     # lens glints
    tail = {9: (4, "K"), 10: (3, "KA"), 11: (2, "KAA"), 12: (1, "KAaA"), 13: (1, "KXXX"),
            14: (1, "KAaA"), 15: (1, "KAaA"), 16: (1, "KAaA"), 17: (1, "KAaA"), 18: (1, "KAaA"),
            19: (1, "KAaA"), 20: (1, "KAaAK"), 21: (2, "KAaAK"), 22: (2, "KAaAK"), 23: (2, "KAaAK"),
            24: (3, "KAaAK"), 25: (3, "KAaAK"), 26: (4, "KAaAK"), 27: (4, "KAaAK"), 28: (5, "KAaK"),
            29: (5, "KAaK"), 30: (6, "KK")}
    for y, (x, s) in tail.items():                              # ponytail: behind the head, over the shoulder
        put(g, x, y, s)
    sprite(g, 20, 27, FOUR); sprite(g, 24, 27, TWO)             # "42" on the tee
    return g


def finish(g, bg='.', odd=','):
    scanlines(g, range(32), bg, odd)
    return g


# ---------- round 1 concepts ----------
def ponytail():
    return render(finish(portrait()), PAL)


def hologram():
    """A blue holo-transmission: same portrait, luminance mapped to a cyan ramp, flickering rows."""
    g = portrait()
    img = render(g, PAL, scale=1)
    px = img.load()
    bg = tuple(int(PAL['.'][i:i + 2], 16) for i in (1, 3, 5))
    for y in range(32):
        for x in range(32):
            r, gg, b = px[x, y]
            if (r, gg, b) == bg:
                px[x, y] = (8, 16, 40) if y % 2 else (10, 22, 52)
                continue
            lum = (0.3 * r + 0.59 * gg + 0.11 * b) / 255
            lum = min(1.0, 0.45 + 0.8 * lum)
            if y % 2:
                lum *= 0.75
            px[x, y] = (int(90 * lum), int(225 * lum), int(255 * lum))
    for y, dx in ((9, 1), (21, -1), (22, -1)):                  # glitch rows
        row = [px[x, y] for x in range(32)]
        for x in range(32):
            px[x, y] = row[(x - dx) % 32]
    return img.resize((512, 512), Image.NEAREST)


def magnifier():
    """Inspecting your code: a big lens over his right eye."""
    g = portrait()
    cx, cy, r = 21, 13, 6
    for y in range(32):
        for x in range(32):
            d = math.hypot(x - cx, y - cy)
            if d < r - 0.5:
                g[y][x] = 'S'
            elif d < r + 0.8:
                g[y][x] = 'O' if d < r + 0.3 else 'K'
    sprite(g, 18, 9, ["bbbbbb"])                                # big brow, magnified
    sprite(g, 18, 11, [" wwww ", "wwEEww", "wwEEww", " wwww "])  # magnified eye
    put(g, 18, 11, "w"); put(g, 23, 15, " ")
    put(g, 17, 10, "ww")                                        # lens glare
    for i in range(7):                                          # handle
        put(g, 25 + i // 2 * 1 + i // 3, 18 + i, "DD")
    return render(finish(g), PAL)


def draw_saber(g):
    shift_left(g, 3)                                            # room for the blade
    for y in range(1, 22):                                      # blade, white core
        put(g, 27, y, "QwQ")
    put(g, 28, 0, "Q")
    for y in range(22, 30):                                     # hilt
        put(g, 27, y, "KIK" if y % 3 else "KiK")
    sprite(g, 25, 24, [" KKKK", "KSSSSK", "KSSSSK", " KKKK"])    # fist


def saber():
    """Ruthless on a major problem: lightsaber out."""
    g = portrait()
    draw_saber(g)
    return render(finish(g), PAL)


def space_helmet():
    """Fishbowl helmet, starfield behind."""
    g = portrait()
    cx, cy, r = 15.5, 14, 14.5
    for y in range(32):
        for x in range(32):
            d = math.hypot(x - cx, y - cy)
            if r - 0.6 < d < r + 0.6 and y < 25:
                g[y][x] = 'c'
    put(g, 6, 5, "ww"); put(g, 5, 6, "w"); put(g, 4, 8, "w")    # glass glare
    for y in (25, 26):                                          # collar ring
        put(g, 3, y, "I" * 26)
    put(g, 3, 27, "i" * 26)
    for x, y in ((1, 2), (29, 1), (2, 20), (30, 12), (27, 22), (24, 3), (0, 9)):
        if g[y][x] in '.,':
            g[y][x] = '*'
    pal = dict(PAL, **{'.': '#0d0b1e', ',': '#0a0918'})
    return render(finish(g), pal)


CONCEPTS = [("1-ponytail", ponytail), ("2-hologram", hologram), ("3-magnifier", magnifier),
            ("4-saber", saber), ("5-space-helmet", space_helmet)]

# ---------- round 2: faces on 1 (ponytail) and 4 (saber) ----------
def classic(g):
    pass


def skeptic(g):                                                 # right brow up, left eye squinting
    put(g, 18, 10, "SSSSSS")
    put(g, 19, 8, "bbbb"); put(g, 18, 9, "b"); put(g, 23, 9, "b")
    put(g, 20, 14, "EE")                                         # wide open
    put(g, 10, 12, "LL"); put(g, 9, 13, "EEE")                  # squint


def grin(g):                                                    # the teacher who just found your bug
    put(g, 13, 20, "MwwwwM"); put(g, 14, 21, "MMMM")
    put(g, 12, 19, "M"); put(g, 19, 19, "M")


def round_glasses(g):
    for x in (7, 13, 18, 24):
        g[11][x] = g[15][x] = 'S'


def headphones(g):                                              # coding with music on
    put(g, 10, 2, "hhhhhhhhhhhh")
    sym(g, 8, 3, "hh"); sym(g, 7, 4, "h")
    for y in (5, 6): sym(g, 6, y, "h")
    for y in (7, 8, 9): sym(g, 5, y, "h")
    for y in (10, 11): sym(g, 4, y, "h")
    for y in range(11, 18): sym(g, 1, y, "Khjjh")
    sym(g, 2, 10, "KKK"); sym(g, 2, 18, "KKK")
    sym(g, 2, 14, " Q")                                          # LED


def salt_pepper(g):                                             # greying at the temples and chin
    sym(g, 6, 8, "G"); sym(g, 6, 9, "GG"); sym(g, 5, 10, "GG"); sym(g, 5, 11, "G")
    sym(g, 6, 18, "G"); sym(g, 6, 19, "G")                       # sideburns
    for y in (22, 23, 24):                                      # chin streak
        sym(g, 15, y, "G")
    for y in (14, 16, 18):
        g[y][3] = 'G'


def robe(g):                                                    # brown robe over a cream tunic, no print
    for y in range(24, 32):
        for x in range(32):
            if g[y][x] in 'TY':
                if 11 <= x <= 20:
                    g[y][x] = 'u' if abs(x - 15.5) < (y - 25) * 0.6 + 1 else 'U'
                else:
                    g[y][x] = 'r' if x % 5 == 0 else 'R'


FACES = [("classic", classic), ("skeptic", skeptic), ("grin", grin), ("round-glasses", round_glasses),
         ("headphones", headphones), ("salt-pepper", salt_pepper)]


def build(face=classic, saber_color=None, robed=False):
    g, pal = portrait(), dict(PAL)
    if robed:
        robe(g)
    face(g)
    if saber_color:
        pal['Q'] = SABERS[saber_color]
        draw_saber(g)
    return render(finish(g), pal)


def round2():
    items = []
    for i, (fname, face) in enumerate(FACES):
        items.append((f"1{'abcdef'[i]}-{fname}", build(face)))
    for i, (fname, face) in enumerate(FACES):
        items.append((f"4{'abcdef'[i]}-{fname}", build(face, 'green')))
    for name, kw in (("4g-red", dict(saber_color='red')), ("4h-blue", dict(saber_color='blue')),
                     ("4i-purple", dict(saber_color='purple')), ("4j-robe", dict(saber_color='green', robed=True)),
                     ("4k-robe-red", dict(saber_color='red', robed=True)), ("1g-robe", dict(robed=True))):
        items.append((name, build(**kw)))
    return items


def save(items, out):
    os.makedirs(out, exist_ok=True)
    for name, img in items:
        img.save(os.path.join(out, f"{name}.png"))
    contact_sheet(items, os.path.join(out, "contact-sheet.png"))
    print("ok", out)


if __name__ == '__main__':
    base = sys.argv[1] if len(sys.argv) > 1 else HERE
    save([(name, draw()) for name, draw in CONCEPTS], os.path.join(base, 'round-1'))
    save(round2(), os.path.join(base, 'round-2'))
