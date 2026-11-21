"""Margo, the Doc Keeper: a retired 1970s librarian gone punk. Spiky dyed hair, cat-eye glasses on a
bead chain, studded leather jacket, plum lipstick, one eyebrow up. Props: the shush, an index card,
a card-catalogue drawer, a record.

python3 avatar.py [basedir]   -> <basedir>/round-1/: one PNG per concept + contact-sheet.png
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(HERE, '..', '..', 'scripts')]  # pixelart.py
from pixelart import mirror, put, sym, sprite, shift_left, finish, render, save

# Left halves, 16 columns. No head outline here: outline() adds it, so shapes stay easy to edit.
# H/h hair + shine, G shaved stubble, S skin, N shadow/wrinkle, b brows, w/E eye white + iris,
# M lips, J/j leather jacket + highlight, w (centre) white tee.
HAIR = {
    'spikes': [
        "...............H", "..........H...HH", "..........H...HH", ".........HHH.HHH",
        "......H..HHH.HHH", "......HH.HHHHHHH", "......HHHHHHHHHH", ".....HHHHHHHHHHH",
        ".....HHHHHHHHHHH", ".....HHHHSSSSSSS", ".....HHSSSSSSSSS",
    ],
    'mohawk': [
        "...............H", ".............H.H", ".............HHH", "............HHHH",
        "............HHHH", "........GGG.HHHH", ".......GGGG.HHHH", "......GGGGG.HHHH",
        ".....GGGGGG.HHHH", ".....GGGGSSSSSSS", ".....GGSSSSSSSSS",
    ],
    'bun': [
        "............HHHH", "...........HHHHH", "...........HHHHH", "...........HHHHH",
        "............HHHH", "........HHHHHHHH", ".......HHHHHHHHH", "......HHHHHHHHHH",
        ".....HHHHHHHHHHH", ".....HHHHSSSSSSS", ".....HHSSSSSSSSS",
    ],
}
FACE = [  # rows 11-31
    ".....HSSSbbbbSSS", "....SSSSSSSSSSSS", "....SSSSSwEEwSSS", "....NSSSSSSSSSSS",
    ".....SSSSSSSSSSS", ".....SSSSSSSSSNS", "......SSSSSSSSSS", "......SSSSSSSSSS",
    ".......SSSSSSSSS", ".......SSSSSSSMM", "........SSSSSSSS", ".........SSSSSSS",
    "............SSSS", ".........JJJ.SSS", "......JJJJJj.www", ".....JJJJJJj.www",
    "....JJJJJJJj.www", "...JJJJJJJJj.www", "...JJJJJJJJj.www", "..JJJJJJJJJj.www",
    "..JJJJJJJJJj.www",
]


def palette(hair=('#ff4fa3', '#ff9bd0'), frame='#1fb5a8', bg=('#4b2f6b', '#422a5e')):
    return {
        '.': bg[0], ',': bg[1],                                   # background + scanline
        'K': '#15131a', 'S': '#f0c8a8', 'N': '#c99878', 'p': '#ec9f96', 'G': '#c8ab98',
        'H': hair[0], 'h': hair[1], 'b': '#5a4c55',
        'w': '#ffffff', 'E': '#2a1d14', 'M': '#8e2a4a',
        'B': frame, 'L': '#cfe9f2', 'Y': '#e8c04a', 'O': '#b8892a',
        'J': '#26262c', 'j': '#4e4e5c', 'c': '#d8d8e0',
        'R': '#d62f3f', 'r': '#6f9fd8',                            # index-card lines, badge
        'A': '#a8743f', 'a': '#8a5a2e',                            # oak
        'P': '#f2c230', 'q': '#f08aa0', 'k': '#44444f', 'g': '#9c8f8c',  # pencil, eraser, groove, stubble
    }


PINK = palette()
GREY = ('#b9b9c2', '#e6e6ee')       # hair: (colour, shine)
BLEACH = ('#efe6c8', '#ffffff')


def outline(g, bg='.'):
    """Every background cell touching the figure becomes K."""
    src = [r[:] for r in g]
    for y in range(32):
        for x in range(32):
            if src[y][x] == bg and any(0 <= y + dy < 32 and 0 <= x + dx < 32 and src[y + dy][x + dx] != bg
                                       for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0))):
                g[y][x] = 'K'


def cat_eye(g):
    sym(g, 5, 11, "BB")                                          # the flick
    sym(g, 6, 12, "BBBBBBBB")                                    # heavy top rim
    sym(g, 7, 13, "BL"); sym(g, 13, 13, "BBB")                   # rims + bridge
    sym(g, 8, 14, "BLLLLB")
    sym(g, 9, 15, "BBBB")
    for x, y in ((4, 16), (4, 18), (5, 20), (6, 22), (7, 24)):   # bead chain
        sym(g, x, y, "Y")


def portrait(hair='spikes'):
    g = mirror(HAIR[hair] + FACE)
    outline(g)
    put(g, 19, 11, "bSSSb"); put(g, 20, 10, "bbb")               # one brow up: "that date is wrong"
    sym(g, 6, 14, "N"); sym(g, 6, 13, "N")                       # crow's feet
    sym(g, 9, 16, "N")                                           # under the lenses
    sym(g, 9, 21, "N")                                           # softer jaw
    sym(g, 12, 18, "N"); sym(g, 12, 19, "N")                     # smile lines
    sym(g, 7, 17, "pp")                                          # rouge
    put(g, 18, 20, "M"); put(g, 18, 19, "M")                     # knowing half smile
    cat_eye(g)
    for x, y in ((5, 27), (7, 26), (3, 29)):                     # shoulder studs
        sym(g, x, y, "c")
    sprite(g, 8, 28, ["RR", "RR"])                               # lapel badge
    for y, x in ((1, 15), (3, 10), (5, 7), (7, 12)):             # shine on the spikes
        if g[y][x] == 'H':
            g[y][x] = 'h'
    return g


# ---------- props ----------
def shush(g):
    """Finger to the lips, right hand, off-centre so it never reads as a nose. Shh."""
    for y in (19, 20, 21):
        g[y] = ['S' if c == 'M' else c for c in g[y]]
    put(g, 12, 20, "MMM"); put(g, 13, 21, "M"); put(g, 20, 20, "M")   # pursed, both sides of the finger
    sprite(g, 15, 17, [" KKK ", "KwppK", "KSSSK", "KSSSK", "KSSSK"])   # starts below the nose
    sprite(g, 14, 22, ["KKSSSKKKK", "KSSSSSSNK", "KSNSNSNNK", "KSSSSSSNK", " KKKKKKKK"])   # fist, outlined on top
    for i, y in enumerate(range(27, 32)):                        # forearm runs off to the bottom right
        put(g, 16 + i, y, "KJJjJJK")


def arm(g, x, top):
    put(g, x, top, "KSSSK"); put(g, x, top + 1, "KSSSK"); put(g, x, top + 2, "KKKKK")
    for y in range(top + 3, 32):
        put(g, x, y, "KJjJK")


def index_card(g):
    shift_left(g, 2)
    arm(g, 24, 21)
    sprite(g, 21, 12, ["KKKKKKKKKKK", "KwwwwwwwwwK", "KRRRRRRRRRK", "KwwwwwwwwwK", "KrrrrrrrwwK",
                       "KwwwwwwwwwK", "KrrrrrwwwwK", "KwwwwwwwwwK", "KKKKKKKKKKK"])


def catalogue(g):
    """Peeking over an open card-catalogue drawer."""
    put(g, 0, 21, "K" * 32)
    put(g, 0, 22, "".join('c' if x % 3 == 0 else 'w' for x in range(32)))   # the cards
    put(g, 0, 23, "K" * 32)
    for y in range(24, 32):
        put(g, 0, y, "".join('a' if (x * 3 + y * 7) % 11 == 0 else 'A' for x in range(32)))
    sprite(g, 13, 25, ["OOOOOO", "OwrrwO", "OOOOOO"])              # label holder
    sprite(g, 11, 29, ["KYYYYYYYYK", " KKKKKKKK "])                # brass pull
    for x0 in (3, 22):                                           # fingers over the edge
        sprite(g, x0, 20, [" KKKKK ", "KSKSKSK", "KSKSKSK", "KSKSKSK"])


def vinyl(g):
    shift_left(g, 2)
    cx, cy, r = 25, 22, 6.6
    for y in range(32):
        for x in range(18, 32):
            d = math.hypot(x - cx, y - cy)
            if d <= r:
                g[y][x] = ('K' if d > r - 0.9 else 'w' if d < 0.8 else 'R' if d < 2.4
                           else 'j' if abs((x - cx) - (y - cy)) < 0.8 and x < cx else 'k' if int(d) % 2 else 'K')
    arm(g, 23, 28)


def grin(g):
    for y in (19, 20, 21):
        for x in range(11, 21):
            if g[y][x] == 'M':
                g[y][x] = 'S'
    sym(g, 12, 20, "Mwww"); sym(g, 13, 21, "MMM"); sym(g, 11, 19, "M")


def shaved(g):
    for y in range(32):
        for x in range(32):
            if g[y][x] == 'G' and (x * 5 + y * 3) % 4 == 0:
                g[y][x] = 'g'


def punk_hardware(g):
    """Spiked collar, safety-pin earring."""
    put(g, 11, 23, "KKKKKKKKKK"); put(g, 11, 24, "KcKcKcKcKK")
    put(g, 3, 15, "c"); put(g, 3, 16, "c"); put(g, 3, 17, "cc")


def pencil_in_bun(g):
    for y in (1, 4):                                             # outline only where there's no bun
        for x in range(6, 26):
            if g[y][x] == '.':
                g[y][x] = 'K'
    put(g, 6, 2, "KqqcPPPPPPPPPPPPPAAKK")                        # eraser, ferrule, body, wood, point
    put(g, 6, 3, "KqqcOOOOOOOOOOOOOAAK ")
    put(g, 13, 0, "hh"); put(g, 12, 1, "h"); put(g, 18, 4, "hh")  # bun shine
    sym(g, 3, 15, "c"); sym(g, 3, 16, "c"); sym(g, 3, 17, "cc")  # safety-pin earrings


# ---------- round 1: different concepts ----------
def look(hair='spikes', *steps, pal=PINK, **over):
    g = portrait(hair)
    for s in steps:
        s(g)
    return render(finish(g), dict(pal, **over))


CONCEPTS = [
    ("1-shush", lambda: look('spikes', shush)),
    ("2-mohawk", lambda: look('mohawk', shaved, punk_hardware, pal=palette(frame='#d62f3f', bg=('#2f5f6b', '#29535e')))),
    ("3-index-card", lambda: look('spikes', index_card,
                                  pal=palette(BLEACH, '#d62f3f', ('#3d5a73', '#35506a')))),
    ("4-card-catalogue", lambda: look('spikes', catalogue, pal=palette(frame='#1fb5a8', bg=('#2f5d46', '#29523d')))),
    ("5-vinyl", lambda: look('spikes', grin, vinyl, pal=palette(GREY, '#7a4a22', ('#7a2230', '#6b1d2a')))),
    ("6-bun-pencils", lambda: look('bun', pencil_in_bun, pal=palette(GREY, '#d62f3f', ('#22284a', '#1d2240')))),
]

if __name__ == '__main__':
    base = sys.argv[1] if len(sys.argv) > 1 else HERE
    save([(name, draw()) for name, draw in CONCEPTS], os.path.join(base, 'round-1'))
