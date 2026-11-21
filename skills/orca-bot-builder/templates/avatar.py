"""<Name>, the <Role>: <three or four visual cues from SOUL.md: age, job, mood, era, habits>.

Starter for a new bot's avatars. Copy this file and ../scripts/pixelart.py into the bot's avatar
folder, then edit LEFT, PAL, the helpers and CONCEPTS. Method and lessons: ../references/avatars.md.

python3 avatar.py [basedir]   -> <basedir>/round-1/: one PNG per concept + contact-sheet.png
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(HERE, '..', 'scripts')]  # pixelart.py: a copy next to this file, or the skill's
from pixelart import mirror, put, sym, sprite, behind, shift_left, finish, render, save

# Left half of the face, 32 rows x 16 columns; mirror() builds the right half.
# K outline, S skin, N shadow, H/h hair + shine, b brows, w eye white, E iris, M mouth, U shirt, u shirt shade.
LEFT = [
    "................", "................", "................", "..........KKKKKK",
    "........KKHHHHHH", ".......KHHHHHHHH", "......KHHHHHHHHH", "......KHHHHHHHHH",
    ".....KHHHHHHHHHH", ".....KHHHSSSSSSS", ".....KHSSSSSSSSS", ".....KHSbbbbbSSS",
    "....KSSSSSSSSSSS", "....KSSSSwEEwSSS", "....KNSSSSSSSSSS", ".....KSSSSSSSSSS",
    ".....KSSSSSSSSNS", "......KSSSSSSSSS", "......KSSSSSSSSS", ".......KSSSSSSSS",
    ".......KSSSSSSMM", "........KSSSSSSS", ".........KSSSSSS", "..........KKSSSS",
    ".......KKUUUKSSS", ".....KKUUUUUUKKK", "....KUUUUUUUUUUU", "...KUUUUUUUUUUUU",
    "..KUUUUUUUUUUUUU", "..KuUUUUUUUUUUUU", ".KUuUUUUUUUUUUUU", ".KUuUUUUUUUUUUUU",
]

# Skin tones: (skin, shadow). Pick the one the persona calls for.
SKIN = {'light': ('#f1c7a5', '#cf9f7c'), 'medium': ('#e8b08a', '#c08766'), 'tan': ('#c99566', '#a2734a'),
        'brown': ('#9a6a43', '#7a5032'), 'dark': ('#6b4429', '#52331f')}
# Hair: (hair, shine).
HAIR = {'black': ('#1c1a1d', '#3e3a40'), 'brown': ('#4a3020', '#6e4a32'), 'blonde': ('#d9b45a', '#f2d78a'),
        'red': ('#a8452a', '#d0663e'), 'grey': ('#a9a9b0', '#e2e2e8'), 'white': ('#e8e8ee', '#ffffff')}


def palette(skin='medium', hair='brown', shirt=('#2f5d8a', '#264d73'), bg=('#2f3b6b', '#29345e')):
    s, n = SKIN[skin]
    h, hs = HAIR[hair]
    return {
        '.': bg[0], ',': bg[1],                                   # background + scanline
        'K': '#13161a', 'S': s, 'N': n, 'H': h, 'h': hs, 'b': h,
        'w': '#ffffff', 'E': '#2a1d14', 'M': '#7a3a32',
        'U': shirt[0], 'u': shirt[1],
        'O': '#c9a227', 'Y': '#f2c94c', 'L': '#1d2a3a',           # gold, lens
        'C': '#f2f2f2', 'c': '#b8b8c0', 'X': '#e8e8ee',           # mug, steam
        'Z': '#5d5650', 'z': '#9a948e',                           # beard
    }


PAL = palette()


def portrait():
    g = mirror(LEFT)
    put(g, 18, 5, "hhh"); put(g, 16, 6, "hh")                    # hair shine, one side
    put(g, 19, 11, "bSSSb"); put(g, 20, 10, "bbb")               # one brow up: expression carries at 40px
    put(g, 18, 20, "MM"); put(g, 19, 19, "M")                    # half smile
    return g


# ---------- faces: each changes one thing ----------
def grin(g):
    for y in (19, 20, 21):
        for x in range(11, 21):
            if g[y][x] == 'M':
                g[y][x] = 'S'
    sym(g, 12, 20, "Mwww"); sym(g, 13, 21, "MMM"); sym(g, 11, 19, "M")


def wink(g):
    put(g, 19, 13, "KKKK"); put(g, 18, 12, " ")


def glasses(g, c='K'):
    for x in (8, 18):
        put(g, x, 12, c * 6); put(g, x, 14, c * 6); put(g, x, 13, c); put(g, x + 5, 13, c)
    put(g, 14, 12, c * 4); put(g, 5, 12, c * 3); put(g, 24, 12, c * 3)


def aviators(g):
    lens = ["OOOOOO", "OLLLLO", "OLwLLO", " OLLO "]
    sprite(g, 8, 12, lens); sprite(g, 18, 12, [r[::-1] for r in lens])
    put(g, 14, 12, "OOOO"); put(g, 5, 12, "OOO"); put(g, 24, 12, "OOO")


def beard(g):
    for y in range(17, 24):
        for x in range(32):
            if g[y][x] == 'S' and (y >= 21 or x <= 11 or x >= 20):
                g[y][x] = 'z' if (x * 5 + y * 3) % 7 == 0 else 'Z'   # sparse speckles, not a checkerboard


# ---------- props: shift the face left first so the prop has its own columns ----------
def arm(g, x=25, top=19):
    put(g, x, top, "KSSSK"); put(g, x, top + 1, "KSSSK")
    for y in range(top + 2, 32):
        put(g, x, y, "KUUUK")


def mug(g):
    shift_left(g, 2)
    sprite(g, 24, 13, ["KKKKKK  ", "KEEEEKK ", "KCCCCK K", "KUUUUK K", "KCCCCKK ", " KKKK   "])
    behind(g, 25, 9, [" X", "X ", " X"]); behind(g, 28, 8, ["X ", " X", "X "])  # steam, behind the head
    arm(g, 25, 19)


# ---------- round 1: different concepts, not variations of one ----------
def look(*faces, prop=None, **pal):
    """portrait + faces + prop, rendered with palette(**pal)."""
    g = portrait()
    for f in faces:
        f(g)
    if prop:
        prop(g)
    return render(finish(g), palette(**pal))


CONCEPTS = [
    ("1-classic", lambda: look()),
    ("2-glasses-beard", lambda: look(glasses, beard, hair='black', skin='tan')),
    ("3-grin", lambda: look(grin, hair='red', skin='light', bg=('#2f6b52', '#295f49'))),
    ("4-coffee", lambda: look(wink, prop=mug, skin='brown', hair='black', shirt=('#8e1f2e', '#741826'))),
    ("5-aviators", lambda: look(aviators, grin, hair='grey', skin='dark', bg=('#6e1f2c', '#601a26'))),
]

# Round 2 varies the pick one axis at a time, e.g.:
# ROUND2 = [("2a-grin", lambda: look(grin)), ("2b-glasses", lambda: look(glasses)), ...]

if __name__ == '__main__':
    base = sys.argv[1] if len(sys.argv) > 1 else HERE
    save([(name, draw()) for name, draw in CONCEPTS], os.path.join(base, 'round-1'))
