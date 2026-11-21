"""Three other arcade concepts drawn for Paco's first round. Starting points for new bots, not finished avatars.

python3 concepts.py [basedir]  -> concepts/: green-screen, rack-peek, invader + contact-sheet.png
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'scripts'))  # pixelart.py
from pixelart import mirror, put, scanlines, render, contact_sheet

# ---------- grumpy CRT terminal: line-art face on a phosphor screen ----------
CRT = [
    "................", "................", "................", "...KKKKKKKKKKKKK",
    "...KCCCCCCCCCCCC", "...KCKKKKKKKKKKK", "...KCKDDDDDDDDDD", "...KCKDDDDDppppp",
    "...KCKDDDppDDDDD", "...KCKDDpDDDDDDD", "...KCKDpDPPPDDDD", "...KCKDpDDDDPPPD",
    "...KCKDpDPPPPPDD", "...KCKDpDPDPDPPP", "...KCKDpDPPPPPDD", "...KCKDpDDDDDDDD",
    "...KCKDpDDDDPPPP", "...KCKDDpDDDDDDD", "...KCKDDpDDDDPPP", "...KCKDDDpDDPDDD",
    "...KCKDDDDppDDDD", "...KCKDDDDDDpppp", "...KCKKKKKKKKKKK", "...KCCCCCCCCCCCC",
    "...Kcccccccccccc", "...KKKKKKKKKKKKK", "..........KcCCCC", "........KcccCCCC",
    ".......KKKKKKKKK", "................", "................", "................",
]
CRT_PAL = {'.': '#1b1530', ',': '#161126', 'K': '#0d0b14', 'C': '#d8cdaa', 'c': '#a89c7c',
           'D': '#0a2a17', 'd': '#06190d', 'P': '#4dff88', 'p': '#2fbf62', 'X': '#ff4d4d'}


def green_screen():
    g = mirror(CRT)
    put(g, 23, 21, "PP")                                        # cursor
    put(g, 6, 23, "cccc"); put(g, 23, 23, "P X")                # vents, power LEDs
    scanlines(g, range(6, 22), 'D', 'd')                        # phosphor lines
    scanlines(g, range(32), '.', ',')
    return g


# ---------- peeking over a server rack ----------
RACK = [
    "................", "................", "...........KKKKK", ".........KKSSSSS",
    "........KSSSSSSS", ".......KSSSSSSSS", ".......KWSSSSSSS", ".......KWbbbSSSS",
    "......KWWSbbbbbS", "......KWSBBBBBBS", "......KWBBssssBB", "......KWSBLEELBS",
    "..KKK.KWSBBBBBBS", ".KSSSKKGSSSSSSNS", ".KKKKKKKKKKKKKKK", ".KRRRRRRRRRRRRRR",
    ".KRUUUUUUUUUUUUU", ".KRUUUUUUUUUUUUU", ".KRUUUUUUUUUUUUU", ".KRRRRRRRRRRRRRR",
    ".KRUUUUUUUUUUUUU", ".KRUUUUUUUUUUUUU", ".KRUUUUUUUUUUUUU", ".KRRRRRRRRRRRRRR",
    ".KRUUUUUUUUUUUUU", ".KRUUUUUUUUUUUUU", ".KRUUUUUUUUUUUUU", ".KRRRRRRRRRRRRRR",
    ".KRUUUUUUUUUUUUU", ".KRUUUUUUUUUUUUU", ".KRUUUUUUUUUUUUU", ".KRRRRRRRRRRRRRR",
]
RACK_PAL = {'.': '#10303d', ',': '#0c2833', 'K': '#0b0d12', 'S': '#f1b38c', 's': '#c98262',
            'N': '#c98262', 'H': '#ffe0c8', 'W': '#f2f2f2', 'G': '#b9bdc7', 'g': '#5e6470', 'b': '#4a4f5c',
            'B': '#0b0d12', 'L': '#8fd6ff', 'w': '#ffffff', 'E': '#0b0d12',
            'R': '#3b4252', 'U': '#5b6680', 'u': '#2b3140', 'P': '#4dff88', 'A': '#ffb347', 'X': '#ff4d4d'}


def rack_peek():
    g = mirror(RACK)
    put(g, 12, 3, "HH"); put(g, 11, 4, "H")
    put(g, 10, 11, "w"); put(g, 18, 11, "w")
    for y, leds in ((17, "P P"), (21, "P A"), (25, "X A"), (29, "P P")):
        for x in range(9, 28, 2):
            g[y][x] = 'u'                                       # drive bays
        put(g, 4, y, leds)                                      # status LEDs, one unit red
    scanlines(g, range(32), '.', ',')
    return g


# ---------- space invader with glasses and a beard ----------
INV = ["..X.....X..", "...X...X...", "..XXXXXXX..", ".XX.XXX.XX.",
       "XXXXXXXXXXX", "X.XXXXXXX.X", "X.X.....X.X", "...XX.XX..."]
INV_PAL = {'.': '#0b0b18', '*': '#8a8fb0', 'K': '#0b0b18', 'X': '#d65cff', 'W': '#f2f2f2',
           'G': '#c4c8d2', 'g': '#8a90a0', 'B': '#0b0b18', 'L': '#8fd6ff', 'w': '#ffffff',
           'E': '#0b0b18', 'M': '#5c2232'}


def invader():
    g = [['.'] * 32 for _ in range(32)]
    for by, row in enumerate(INV):                              # 11x8 invader at 2x
        for bx, ch in enumerate(row):
            if ch == 'X':
                for dy in (0, 1):
                    for dx in (0, 1):
                        g[4 + 2 * by + dy][5 + 2 * bx + dx] = 'W' if by < 2 else 'X'
    for x0 in (10, 18):                                         # glasses
        put(g, x0, 9, "BBBB"); put(g, x0, 10, "BwLB"); put(g, x0, 11, "BEEB"); put(g, x0, 12, "BBBB")
    put(g, 14, 10, "BBBB")
    put(g, 9, 7, "WW"); put(g, 11, 8, "WWW"); put(g, 21, 7, "WW"); put(g, 18, 8, "WWW")  # angry brows
    beard = {14: (11, 20), 15: (10, 21), 16: (10, 21), 17: (10, 21), 18: (10, 21), 19: (11, 20),
             20: (11, 20), 21: (12, 19), 22: (12, 19), 23: (13, 18), 24: (13, 18), 25: (14, 17), 26: (15, 16)}
    for y, (a, b) in beard.items():
        g[y][a - 1] = g[y][b + 1] = 'K'
        for x in range(a, b + 1):
            g[y][x] = 'g' if x == a else 'G'
    put(g, 14, 27, "KK"); put(g, 13, 26, "KK  KK")
    put(g, 11, 14, "WWWWWWWWWW")
    put(g, 13, 15, "MMMMMM"); put(g, 12, 16, "M"); put(g, 19, 16, "M")
    for x, y in ((2, 2), (28, 3), (3, 24), (27, 22), (24, 29), (6, 30), (29, 13), (1, 15)):
        g[y][x] = '*'                                           # stars
    return g


CONCEPTS = [("green-screen", green_screen, CRT_PAL), ("rack-peek", rack_peek, RACK_PAL), ("invader", invader, INV_PAL)]

if __name__ == '__main__':
    out = os.path.join(sys.argv[1] if len(sys.argv) > 1 else HERE, 'concepts')
    os.makedirs(out, exist_ok=True)
    items = [(name, render(draw(), pal)) for name, draw, pal in CONCEPTS]
    for name, img in items:
        img.save(os.path.join(out, f"{name}.png"))
    contact_sheet(items, os.path.join(out, "contact-sheet.png"))
    print("ok", out)
