"""Paco, the Releaser: grumpy old sysadmin, smoking. The worked example for SKILL.md.

python3 avatar.py [basedir]  -> round-2/: 6 faces x 2 shirts (12 PNGs) + contact-sheet.png
Chosen avatar (2026-11-20): 2-skeptic-flannel.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'scripts'))  # pixelart.py
from pixelart import mirror, put, sym, sprite, scanlines, shift_left, render, contact_sheet

# Left half of the portrait. K outline, S skin, W/G/g hair+beard, b brows, B glasses, L lens, M mouth, T shirt.
LEFT = [
    "................", "................", "..........KKKKKK", "........KKSSSSSS",
    ".......KSSSSSSSS", "......KSSSSSSSSS", "......KSSSSSSSSS", ".....KWSSSSSSSSS",
    ".....KWWSSSSSSSS", ".....KWWbbbSSSSS", "....KWWSSbbbbbSS", "....KWWSBBBBBBSS",
    "...KSWWBBssssBBB", "...KSWWSBLEELBSS", "...KSWWSBLLLLBSS", "...KSWWSBBBBBBSS",
    "...KSWWSSSSSSSNS", "....KGGGSSSSSGGG", "....KGGGGSSSGWWW", "....KGGGGGGGWWWW",
    "....KgGGGGGGGMMM", "....KgGGGGGGMGGG", ".....KgGGGGGGGGG", ".....KggGGGGGGGG",
    "......KggGGGGGGG", ".......KggGGGGGG", "...KTTTTKKggGGGG", "..KTTTTTTTKggGGG",
    ".KTTTTTTTTTKKggG", ".KTTTTTTTTTTTKKg", "KTTTTTTTTTTTTTTT", "KTTTTTTTTTTTTTTT",
]

PAL = {
    '.': '#2d2a6e', ',': '#25225e',                                   # background + scanlines
    'K': '#141220', 'S': '#f1b38c', 's': '#c98262', 'N': '#c98262', 'H': '#ffe0c8',
    'W': '#f2f2f2', 'G': '#b9bdc7', 'g': '#7f8592', 'b': '#4a4f5c',
    'B': '#141220', 'L': '#8fd6ff', 'w': '#ffffff', 'E': '#141220', 'M': '#5c2232',
    'T': '#3a4a6e', 't': '#34343f', 'P': '#45ff6e',
    'F': '#e0893c', 'C': '#f7f7f7', 'O': '#ff5a1f', 'm': '#e4e4f0', 'n': '#9d9dc0',  # cigarette + smoke
    'h': '#26262e', 'j': '#4a4a58', 'V': '#c4522a', 'v': '#9c3f20',                  # headset, beanie
    'R': '#a8323a', 'r': '#6e1f27', 'k': '#3d1015', 'l': '#d9a066', 'U': '#4d7cff', 'X': '#ff4d4d',  # flannel
}


def portrait():
    g = mirror(LEFT)
    put(g, 12, 4, "HH"); put(g, 11, 5, "H")                     # bald-head shine
    put(g, 9, 13, "w"); put(g, 19, 13, "w")                     # lens glints
    put(g, 23, 28, "P"); put(g, 24, 29, "P"); put(g, 23, 30, "P  PPP")  # >_ on the shirt
    scanlines(g, range(32), '.', ',')
    return g


def cigarette(g):
    sprite(g, 19, 20, ["KKKKKKKKKK", "FFCCCCCCOK", "KKKKKKKKKK"])


def wisp(x, y, n=17):
    """Smoke that curls up from (x, y), fading (dithered) at the top."""
    sway = [0, 0, 1, 1, 1, 2, 2, 2, 1, 1, 0, 0, 0, 1, 1, 2, 2]
    return [(x + s, y - i, 'm' if i < 8 else 'n') for i, s in enumerate(sway[:n]) if i < 12 or i % 2 == 0]


# ---------- shirts ----------
def black_tee(g, pal):
    pal['T'] = '#1c1c24'
    for y in range(26, 32):
        for x in range(32):
            if g[y][x] == 'T' and g[y - 1][x] not in 'Tt':
                g[y][x] = 't'                                   # shoulder edge highlight


def flannel(g, pal):
    for y in range(26, 32):
        for x in range(32):
            if g[y][x] in 'TP':                                 # flannel has no >_ print
                v, h = x % 6 in (0, 1), y in (28, 29)
                g[y][x] = 'k' if v and h else 'r' if v or h else 'l' if x % 6 == 3 else 'R'
    for y in range(28, 32):                                     # breast pocket with two pens
        g[y][22] = g[y][26] = 'k'
    put(g, 22, 28, "kkkkk"); put(g, 23, 27, "U X")


# ---------- faces ----------
def classic(g):
    pass


def skeptic(g):                                                 # one brow arched, that eye wide open
    for x in range(18, 24):
        g[9][x] = g[10][x] = 'S'
    put(g, 19, 8, "bbbb"); put(g, 18, 9, "b"); put(g, 23, 9, "b")
    put(g, 19, 12, "LLLL")


def round_glasses(g):
    for x in (8, 13, 18, 23):
        g[11][x] = g[15][x] = 'S'


def headset(g):                                                 # on call
    put(g, 10, 2, "hhhhhhhhhhhh")
    sym(g, 8, 3, "hh"); sym(g, 7, 4, "h")
    for y in (5, 6): sym(g, 6, y, "h")
    for y in (7, 8, 9): sym(g, 5, y, "h")
    for y in (10, 11): sym(g, 4, y, "h")
    sym(g, 3, 11, "hh"); sym(g, 3, 16, "hh")
    for y in range(12, 16): sym(g, 1, y, "Khjjh")
    for x, y in ((4, 17), (5, 18), (6, 19), (7, 19), (8, 20), (9, 20), (10, 21)):
        g[y][x] = 'h'
    put(g, 11, 21, "j"); put(g, 11, 22, "j")


def beanie(g):                                                  # server rooms are cold
    left = ["...........KKKKK", ".........KKVVVVV", "........KVVVVVVV", ".......KVVVVVVVV",
            "......KVVVVVVVVV", ".....KvVvVvVvVvV", ".....KvVvVvVvVvV", ".....KvVvVvVvVvV"]
    for y, row in enumerate(left):
        put(g, 0, y, (row + row[::-1]).replace('.', ' '))


def walrus(g):                                                  # drawn AFTER the cigarette
    put(g, 12, 17, "WWWWWWWW")
    put(g, 10, 18, "WWWWWWWWWWWW")
    put(g, 9, 19, "WWWWWWWWWWWWWW")
    put(g, 9, 20, "GWWWWWWWWWWWWG")
    put(g, 9, 21, "WWGGGGGGGGGGWW")
    put(g, 9, 22, "WWGGGGGGGGGGWW")


FACES = [("classic", classic), ("skeptic", skeptic), ("round-glasses", round_glasses),
         ("headset", headset), ("beanie", beanie), ("walrus", walrus)]
SHIRTS = [("black-tee", black_tee), ("flannel", flannel)]


def build(face, shirt):
    g, pal = portrait(), dict(PAL)
    shirt(g, pal)
    if face is walrus:
        cigarette(g); walrus(g)
    else:
        face(g); cigarette(g)
    shift_left(g)                                               # free the right column for the smoke
    for x, y, c in wisp(26, 20):
        g[y][x] = c
    return render(g, pal)


if __name__ == '__main__':
    out = os.path.join(sys.argv[1] if len(sys.argv) > 1 else HERE, 'round-2')
    os.makedirs(out, exist_ok=True)
    items = []
    for sname, shirt in SHIRTS:
        for i, (fname, face) in enumerate(FACES):
            name = f"{i + 1}-{fname}-{sname}"
            img = build(face, shirt)
            img.save(os.path.join(out, f"{name}.png"))
            items.append((name, img))
    contact_sheet(items, os.path.join(out, "contact-sheet.png"))
    print("ok", out)
