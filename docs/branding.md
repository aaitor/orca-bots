# Banner and social preview

The README header follows the shared repository format: the **diagonal-drift (1a)** banner, seed
`7`, generated with the banner kit from [aaitor/oss-repo-template](https://github.com/aaitor/oss-repo-template)
and kept locally as `assets/hero.svg`. `shared-assets.json` records the template revision.

## Regenerate the banner

From a checkout of the template (Node.js 18+, no npm packages needed):

```bash
node banner-kit/make-banner.mjs --style diagonal-drift --seed 7 \
  --repo "Orca Bots" \
  --tagline "Teammate bots for Orca, with a soul and a pixel-art face." \
  --handle "@aaitor" --out /path/to/orca-bots/assets/hero.svg
```

## Regenerate the social card

The social card shows the five real bots' avatars. It is drawn with Pillow from the committed
`avatar.png` files:

```bash
python3 scripts/social_preview.py   # -> assets/social-preview.png, 1280 x 640
```

Committing the PNG does not set it. Upload it in **GitHub Settings → General → Social preview**.
