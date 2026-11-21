# Arcade avatars

Pixel-art portraits drawn as 32 x 32 character grids in Python, rendered to 512 x 512 PNGs with
crisp pixels. Every bot keeps its own `avatar.py`, so its picture can be redrawn and varied later.
Needs Python 3.9+ and Pillow (`pip install pillow`).

## How a picture is built

1. **The left half.** 32 strings of 16 characters, one character per pixel. `mirror()` copies it
   to the right, so the face is symmetric.
2. **Overlays.** `put`, `sym` and `sprite` add what is not symmetric: a raised brow, a wink, a
   glint, a prop, a shirt print. A space in an overlay is transparent.
3. **The palette.** A dict from character to hex colour. Swap the palette to change hair, skin,
   clothes or background without touching the grid.
4. **Finish.** `finish(g)` darkens the background on odd rows: the CRT scanline look. Call it last.
5. **Render.** `render(g, pal)` scales x16 with nearest-neighbour: 512 px, no blur.

### Palette conventions

Keep these so scripts stay readable to the next agent:

| Char | Meaning | Char | Meaning |
|---|---|---|---|
| `.` `,` | background, scanline | `K` | outline (near black) |
| `S` `N` | skin, skin shadow | `H` `h` | hair, hair shine |
| `b` | brows | `w` `E` | eye white, iris |
| `M` | mouth | `B` `L` | glasses frame, lens |
| `T` `U` | shirt | `O` `Y` | gold, dark and light |

Anything else is free: pick a letter and comment it in the palette.

### Helpers (`scripts/pixelart.py`)

| Helper | Does |
|---|---|
| `mirror(left)` | 32 x 16 left half to a symmetric 32 x 32 grid |
| `put(g, x, y, s)` | write a string into row `y` from column `x`; spaces are transparent |
| `sym(g, x, y, s)` | `put` plus its mirror image on the other side |
| `sprite(g, x, y, rows)` | `put` several rows, top-left at `(x, y)` |
| `behind(g, x, y, rows)` | like `sprite`, but paints only background cells: props sit behind the head |
| `shift_left(g, n=2)` | move the whole picture left to free columns on the right for a prop |
| `scanlines(g, rows, src, dst)` / `finish(g)` | the CRT lines |
| `render(g, pal, scale=16)` | grid to a PIL image |
| `contact_sheet(items, path)` | each image at 256 px plus a **round 40 px preview**, which is how Orca shows avatars |
| `save(items, out)` | every PNG plus `contact-sheet.png` into `out` |
| `html_page(sheets, path, title)` | one self-contained HTML page with the sheets inlined |

## The process

1. **Read the SOUL.** Pull three or four visual cues: age, job, mood, era, clothes, habits.
   Paco: forty years a sysadmin, grumpy, old Unix, smokes. Charo: ancient, strict, sees
   everything, cats. Richard: elegant, money, art and music.
2. **Round 1: four to eight different concepts**, not variations of one. Mix a plain portrait, a
   portrait with the persona's signature prop, and one or two ideas that break the frame (a CRT
   face, a space invader, peeking over a server rack, a gilt painting frame).
3. **Look before you show.** Read the contact sheet and at least one full-size PNG. Fix what reads
   wrong, then show it.
4. **The owner picks.** Recommend two or three and say why in a few words.
5. **Round 2 and later: vary the pick, one axis at a time.** Group them so the owner can compare:
   *faces* (grin, wink, side-eye, a raised brow, glasses, a moustache, a beard), *looks* (hair
   colour, clothes, palette), *props* (what they hold), *background*. When two axes both matter,
   draw a grid: six faces x two shirts.
6. **Name files by round and idea**: `round-1/3-dollar-eyes.png`, `round-2/2h-velvet-jacket.png`, so
   "2h" is enough for the owner to answer.
7. **Upload.** The owner clicks the bot's picture in Orca and uploads the PNG.

### Showing pictures

- In an Orca chat (`ORCA_CHAT_SCRATCH_DIR` is set): build a page with
  `html_page([("Round 1", "<dir>/round-1/contact-sheet.png")], "$ORCA_CHAT_SCRATCH_DIR/<bot>-r1-<4 random chars>.html", "<Bot>: round 1")`
  and put `::orca-visual{file="<that file name>" title="<Bot>: round 1"}` on its own line in the reply.
- Anywhere else: give the contact sheet's path, and show it inline if the client can display images.

## Lessons

**Faces**

- A face filled with one flat colour reads as an animal (the first CRT face was a frog). Use skin
  plus an outline, or line art.
- Heavy, dark brows carry the expression at 40 px. An arched brow is two rows (`put(g, 19, 11,
  "bSSSb"); put(g, 20, 10, "bbb")`), not a block.
- Expressions that read small: one brow up, a wink (a closed eye is a row of `K`), side-eye (irises
  pushed to one side under heavy lids), a grin with a row of white teeth, V brows for angry.
- A beard drawn as a checkerboard looks like noise. Use a base colour with sparse lighter
  speckles: `'z' if (x * 5 + y * 3) % 7 == 0 else 'Z'`.
- A moustache must be continuous. Check for gaps where it meets the mouth.
- Want a persona "fatter" or "older"? Widen the jaw rows and add cheeks and wrinkle pixels in the
  left half, then re-mirror; don't stretch the image.

**Props**

- Leave the prop its own columns: `shift_left(g)` first, then draw it on the right edge.
- Anything behind the head (music notes, smoke, a painting on the wall) goes through `behind()`,
  or it will be painted over the face.
- Draw whatever covers a prop after it (the walrus moustache after the cigarette), and check for
  stray outline pixels.
- Thin details vanish at 40 px: a one-pixel white cigarette, single-pixel smoke. Make the signature
  prop at least 3 px wide, with an outline and a highlight.
- Round things need a rounder sprite than you expect: a coin is `" KKKK "` on top and bottom.
  For a disc, compute it with `math.hypot` and centre it on a pixel.
- Glyphs need room: a readable `$` is 3 x 7.
- A hand holding a prop: skin rows, then a cuff, then the sleeve down to the bottom edge.

**Colour and clothes**

- The face must contrast with the background. Game Boy greens were too close to the skin; use a
  mid-tone background behind light skin and a lighter or more saturated one behind dark skin.
- Swap palettes to try looks quickly: a palette override dict per look (`SILVER`, `VELVET`,
  `LINEN`) merged with `dict(PAL, **override)`.
- Keep clothes true to the persona. An old sysadmin wears a black tee or an old flannel, not a
  hoodie. A dealmaker wears a navy suit. Ask if unsure.

## The examples as a style library

Before drawing, open the example closest to the new bot and borrow from it.

| Example | Shows |
|---|---|
| `examples/paco-the-releaser/avatar.py` | The basic portrait: faces x shirts grid, a cigarette with smoke wisps, headset, beanie, walrus moustache |
| `examples/paco-the-releaser/concepts.py` | Frame-breaking concepts: a CRT terminal face in phosphor line art, peeking over a server rack, a space invader with glasses and beard |
| `examples/sami-the-architect/avatar.py` | Ponytail and beard, a hologram, a magnifier, a lightsaber in four colours, a space helmet, a shirt print ("42"), a robe |
| `examples/chani-the-marketer/avatar.py` | A high ponytail and hoops, a bubblegum bubble, a disco ball, a selfie phone, a megaphone, an afro, heart sunglasses |
| `examples/charo-the-admin/avatar.py` | An old face, a bun, half-moon glasses, a cat; round 2 widens the face and adds angry, sarcastic, eye-roll, side-eye and fuming (steam) faces |
| `examples/richard-the-dealmaker/avatar.py` | A suit and tie, `behind()`, a coin flip, dollar eyes, a conductor's baton with notes, a gilt frame and painting, wine, palette overrides and a `look()` composer for round 2 |
| `examples/margo-the-doc-keeper/avatar.py` | Drawn by the skill itself: hair styles as swappable top rows, an `outline()` pass, spikes, a mohawk, cat-eye glasses on a chain, a studded jacket, a shush hand, a card-catalogue drawer |
| `templates/avatar.py` | The starter: a neutral portrait, skin and hair palettes, a few faces and a held mug |
