"""Charo, the Admin: a million years old, grey bun, half-moon glasses, sees everything, loves (?) cats.

python3 charo.py [basedir]  -> round-1/ (6 concepts) and round-2/ (fatter, angry and sarcastic faces x cat and props)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'scripts'))  # pixelart.py
from pixelart import mirror, put, sym, sprite, scanlines, shift_left, render, contact_sheet

# K outline, S skin, N wrinkles, W/g hair, b brows, E eyes, B glasses frame, L lens, M mouth, C cardigan.
LEFT = [
    "................", "............KKKK", "...........KWWgW", "...........KWgWW",
    ".........KKKKWWW", "........KWWWWWWW", ".......KWWWgWWWW", ".......KWWgWWWWW",
    "......KWWWWWWWWW", "......KWWWSSSSSS", "......KWSSSSSSSS", "......KWSbbbbSSS",
    "......KSSKKKKSSS", "....KSSSSwEEwSSS", "....KSSBBBBBBBBB", "....KNSBLLLLLBSS",
    ".....wSSBBBBBSSS", "......KSSSSSSSNS", "......KSSppSSSSS", ".......KSSSSSSSS",
    ".......KSSSSSSMM", "........KSSSSSSS", ".........KSSSSSS", "..........KKSSSS",
    "...........KKsss", "...........KwwKs", ".......KCCCCKwwK", ".....KCCCCCCKwww",
    "....KCCCCCCCKwww", "...KCCCCCCCCKwww", "..KCCCCCCCCCCKww", "..KCCCCCCCCCCKww",
]

PAL = {
    '.': '#3d5a73', ',': '#35506a',                                   # slate blue + scanlines
    'K': '#16141c', 'S': '#efc3a0', 's': '#c9987a', 'N': '#c9987a', 'p': '#e8a08c',
    'W': '#dcdce2', 'g': '#a9a9b4', 'b': '#3d3d46', 'E': '#16141c',
    'B': '#8a6a1f', 'L': '#bfe4f2', 'M': '#8a3a3a', 'w': '#f4f1e8',
    'C': '#7a2e3a', 'c': '#5e2230', 'Y': '#e8c04a',
    'X': '#16141c', 'x': '#2b2833', 'Q': '#7dff6a', 'q': '#ff9bb0',      # black cat
    'D': '#1a1626', 'd': '#151220',                                   # dark background
    'Z': '#e8304a', 'z': '#f07a70',                                   # anger
    'R': '#ff8fb8', 'r': '#7fc8ff', 'P': '#c9a227', 'A': '#d9b36b', 'a': '#a8823c',
}


def portrait():
    g = mirror(LEFT)
    put(g, 13, 20, "N"); put(g, 18, 20, "N")                    # pursed
    put(g, 12, 21, "N"); put(g, 19, 21, "N")                    # corners down
    sym(g, 7, 13, "N")                                          # crow's feet
    put(g, 19, 10, "bbbb"); put(g, 18, 11, "bSSSSS")            # the eyebrow: one up, judging
    for y, x in ((17, 6), (19, 6), (21, 7), (22, 8)):           # glasses chain
        sym(g, x, y, "Y")
    put(g, 10, 28, "Y"); put(g, 9, 28, "Y"); put(g, 10, 27, "Y")  # brooch
    for y in range(27, 32):                                     # cardigan knit
        for x in range(32):
            if g[y][x] == 'C' and (x + y) % 5 == 0:
                g[y][x] = 'c'
    return g


def finish(g, bg='.', odd=','):
    scanlines(g, range(32), bg, odd)
    return g


# ---------- round 1 concepts ----------
def over_the_glasses():
    return render(finish(portrait()), PAL)


def cat():
    """A black cat on her shoulder. She'll deny it."""
    g = portrait()
    sprite(g, 21, 19, ["X   X  ", "XX XX  ", "XXXXX  ", "XQXQX  ", "XXqXX  ", " XXXXXX", " XXXXXXX",
                       "XXXXXXXX", "XXXXXXXX", "XXXXXXXX", "XXXXXXX "])
    put(g, 29, 25, "X"); put(g, 30, 24, "X"); put(g, 30, 23, "X")      # tail up
    return render(finish(g), PAL)


def sees_everything():
    """The glasses catch the light and you can't see her eyes. She can see yours."""
    g = portrait()
    for x in range(32):                                         # lenses blaze
        if g[15][x] == 'L':
            g[15][x] = 'w'
    put(g, 8, 14, "BwwwwwB"); put(g, 18, 14, "BwwwwwB")         # taller lenses, eyes behind
    put(g, 8, 13, "BBBBBBB"); put(g, 18, 13, "BBBBBBB")
    return render(finish(g, '.', ','), dict(PAL, **{'.': '#1a1626', ',': '#151220'}))


def clipboard():
    """Pencil behind the ear, clipboard with everything ticked. Except yours."""
    g = portrait()
    for i in range(6):                                          # pencil behind the ear
        put(g, 2 + i, 9 + i, "P")
    put(g, 1, 8, "q"); put(g, 8, 15, "K")
    sprite(g, 20, 20, ["  KKKK  ", "KKKYYKKK", "KAAAAAAK", "KAKAaaAK", "KAAAAAAK", "KAKAaaAK",
                       "KAAAAAAK", "KAqAaaAK", "KAAAAAAK", "KAAAAAAK", "KKKKKKKK"])
    return render(finish(g), PAL)


def rulos():
    """Sunday morning: curlers in, opinions out."""
    g = portrait()
    for y in range(0, 5):                                       # no bun today
        for x in range(32):
            if g[y][x] in 'WgK' and y < 4:
                g[y][x] = '.'
    for x0, y0, c in ((8, 4, 'R'), (12, 3, 'r'), (16, 3, 'R'), (20, 4, 'r'), (6, 7, 'r'), (22, 7, 'R')):
        sprite(g, x0, y0, [" KK ", "K" + c * 2 + "K", "K" + c * 2 + "K", " KK "])
    return render(finish(g), PAL)


def mug():
    """Coffee. The mug says it all."""
    g = portrait()
    sprite(g, 19, 21, ["KKKKKKKKKKK  ", "KwwwwwwwwwK  ", "KwMwwMwMMMKKK", "KwMMwMwMwMK K",
                       "KwMwMMwMwMK K", "KwMwwMwMMMKKK", "KwwwwwwwwwK  ", "KwwwwwwwwwK  ", " KKKKKKKKK   "])
    return render(finish(g), PAL)


# ---------- round 2: fatter, angrier, more sarcastic ----------
FAT = [
    "................", "............KKKK", "...........KWWgW", "...........KWgWW",
    ".........KKKKWWW", "........KWWWWWWW", ".......KWWWWWWWW", "......KWWWWgWWWW",
    "......KWWWgWWWWW", ".....KWWWWWSSSSS", ".....KWWSSSSSSSS", ".....KWSSbbbbSSS",
    ".....KSSSKKKKSSS", "...KSSSSSwEEwSSS", "...KSSSBBBBBBBBB", "...KNSSBLLLLLBSS",
    "...KwSSSBBBBBSSS", "....KSSSSSSSSSNS", "....KSppSSSSSSSS", "....KSppSSSSSSSS",
    "....KSSSSSSSSSMM", "....KSSSSSSSSSSS", ".....KSSSSSSSSSS", "......KSSSNNNNNN",
    ".......KSSSSSSSS", "........KKKKKKKK", "....KCCCCCCKwwww", "...KCCCCCCCKwwww",
    "..KCCCCCCCCKwwww", ".KCCCCCCCCCKwwww", ".KCCCCCCCCCCKwww", "KCCCCCCCCCCCKwww",
]
CAT = ["X   X  ", "XX XX  ", "XXXXX  ", "XQXQX  ", "XXqXX  ", " XXXXXX", " XXXXXXX",
       "XXXXXXXX", "XXXXXXXX", "XXXXXXXX", "XXXXXXX "]


def fat_portrait():
    g = mirror(FAT)
    sym(g, 7, 13, "N")                                          # crow's feet
    sym(g, 5, 20, "s"); sym(g, 5, 21, "s"); sym(g, 6, 22, "s"); sym(g, 7, 23, "s")  # jowls
    for y, x in ((18, 3), (20, 3), (22, 4), (24, 6)):           # glasses chain
        sym(g, x, y, "Y")
    put(g, 10, 28, "Y"); put(g, 9, 28, "Y"); put(g, 10, 27, "Y")  # brooch
    for y in range(26, 32):
        for x in range(32):
            if g[y][x] == 'C' and (x + y) % 5 == 0:
                g[y][x] = 'c'
    return g


def clear(g, rows, cols, chars, to='S'):
    for y in rows:
        for x in cols:
            if g[y][x] in chars:
                g[y][x] = to


def angry(g):                                                   # V brows, tight frown
    clear(g, (10, 11), range(32), 'b')
    sym(g, 8, 10, "bb"); sym(g, 10, 11, "bbb")
    sym(g, 14, 11, "N"); sym(g, 14, 12, "N")                    # furrow
    clear(g, range(19, 23), range(10, 22), 'MN')
    put(g, 14, 20, "MMMM"); put(g, 13, 21, "M"); put(g, 18, 21, "M")


def sarcastic(g):                                               # one brow flat, one arched, smirk
    clear(g, (10, 11), range(16, 32), 'b')
    put(g, 19, 10, "bbbb"); put(g, 23, 11, "b"); put(g, 18, 11, "b")
    clear(g, range(19, 23), range(10, 22), 'MN')
    put(g, 13, 20, "MMMM"); put(g, 17, 19, "MM"); put(g, 19, 18, "N")


def eye_roll(g):                                                # "oh, really"
    clear(g, (10, 11), range(32), 'b')
    sym(g, 9, 10, "bbbb")
    clear(g, (13,), range(32), 'E', 'w')
    clear(g, range(19, 23), range(10, 22), 'MN')
    put(g, 13, 20, "MMMMMM")


def side_eye(g):                                                # looking at you sideways
    put(g, 9, 13, "wwEE"); put(g, 19, 13, "wwEE")
    sym(g, 9, 11, "b"); sym(g, 12, 11, "b")
    sym(g, 8, 11, "b")
    clear(g, range(19, 23), range(10, 22), 'MN')
    put(g, 15, 20, "MMMM"); put(g, 19, 19, "M")


def fuming(g):                                                  # steam from the ears
    angry(g)
    sprite(g, 22, 4, [" Z Z ", "ZZ ZZ", "     ", "ZZ ZZ", " Z Z "])
    for y in range(32):
        for x in range(32):
            if g[y][x] == 'p':
                g[y][x] = 'z'
    for x, y in ((1, 12), (0, 11), (1, 10), (30, 12), (31, 11), (30, 10)):
        if g[y][x] in '.,':
            g[y][x] = 'w'


FACES2 = [("angry", angry), ("sarcastic", sarcastic), ("eye-roll", eye_roll),
          ("side-eye", side_eye), ("fuming", fuming)]


def with_cat(g):
    shift_left(g, 2)
    sprite(g, 23, 21, CAT)


def blazing(g):
    put(g, 8, 13, "BBBBBBB"); put(g, 18, 13, "BBBBBBB")
    put(g, 8, 14, "BwwwwwB"); put(g, 18, 14, "BwwwwwB")
    clear(g, (15,), range(32), 'L', 'w')


def with_mug(g):
    sprite(g, 19, 21, ["KKKKKKKKKKK  ", "KwwwwwwwwwK  ", "KwMwwMwMMMKKK", "KwMMwMwMwMK K",
                       "KwMwMMwMwMK K", "KwMwwMwMMMKKK", "KwwwwwwwwwK  ", "KwwwwwwwwwK  ", " KKKKKKKKK   "])


def with_rulos(g):
    clear(g, range(0, 4), range(32), 'WgK', '.')
    for x0, y0, c in ((8, 4, 'R'), (12, 3, 'r'), (16, 3, 'R'), (20, 4, 'r'), (6, 7, 'r'), (22, 7, 'R')):
        sprite(g, x0, y0, [" KK ", "K" + c * 2 + "K", "K" + c * 2 + "K", " KK "])


DARK = {'.': '#1a1626', ',': '#151220'}
GINGER = {'X': '#d9822b', 'Q': '#3fae4a'}


def build2(face, prop=None, pal=None):
    g = fat_portrait()
    face(g)
    if prop:
        prop(g)
    return render(finish(g), dict(PAL, **(pal or {})))


def round2():
    items = [(f"2{'abcde'[i]}-{n}", build2(f)) for i, (n, f) in enumerate(FACES2)]
    items += [(f"2{'fghij'[i]}-{n}-cat", build2(f, with_cat)) for i, (n, f) in enumerate(FACES2)]
    items += [("2k-angry-blazing", build2(angry, blazing, DARK)),
              ("2l-sarcastic-mug", build2(sarcastic, with_mug)),
              ("2m-angry-rulos", build2(angry, with_rulos)),
              ("2n-sarcastic-ginger-cat", build2(sarcastic, with_cat, GINGER)),
              ("2o-side-eye-ginger-cat", build2(side_eye, with_cat, GINGER))]
    return items


CONCEPTS = [("1-over-the-glasses", over_the_glasses), ("2-cat", cat), ("3-sees-everything", sees_everything),
            ("4-clipboard", clipboard), ("5-rulos", rulos), ("6-mug-no", mug)]


def save(items, out):
    os.makedirs(out, exist_ok=True)
    for name, img in items:
        img.save(os.path.join(out, f"{name}.png"))
    contact_sheet(items, os.path.join(out, "contact-sheet.png"), cols=5 if len(items) > 6 else 3)
    print("ok", out)


if __name__ == '__main__':
    base_dir = sys.argv[1] if len(sys.argv) > 1 else HERE
    save([(name, draw()) for name, draw in CONCEPTS], os.path.join(base_dir, 'round-1'))
    save(round2(), os.path.join(base_dir, 'round-2'))
