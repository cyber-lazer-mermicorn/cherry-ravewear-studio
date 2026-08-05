# Ravewear Prompt Library

Reusable prompt structure for AI media generation. Keep brand direction; vary silhouette and materials per package.

## Base camera / lighting block

```text
Full-body fashion product photography, clean studio, soft key light + subtle rim,
neutral dark backdrop, sharp fabric detail, no watermark, no logo text,
editorial ravewear catalog style, accurate garment construction visible
```

## Movement / floor block (optional)

```text
Subject mid-motion as if on a dancefloor, fabric catching directional LED color
bleed (magenta / cyan), reflective or holographic surfaces reading correctly,
still catalog-usable not chaotic
```

## View suffixes

- **Front:** facing camera, arms relaxed, full silhouette readable
- **Side:** true profile, depth of garment and cutouts clear
- **Back:** rear construction, straps, closures, panel lines visible
- **Detail:** tight crop on hardware, seam, mesh, or reflective panel

## Negative / avoid block

```text
blurry, low-res, extra limbs, deformed hands, random logos, brand names,
watermark, heavy NSFW, gore, celebrity lookalike, readable third-party trademarks
```

## Usage

1. Compose: concept + silhouette + materials + colorway + base block + view suffix + avoid block
2. Store exact prompt text under `collections/DROP###/prompts/`
3. Record `prompt_ref` inside the package JSON
