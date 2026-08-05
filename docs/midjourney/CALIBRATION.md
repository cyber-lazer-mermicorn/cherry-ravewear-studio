# Midjourney Calibration — Cherry Ravewear Studio

**Purpose:** Generate ravewear and psychedelic-spiritual design imagery that people who actually live on the floor recognize as true — color, light, beat, body, joy — not costume cosplay or empty neon spam.

**Principle:** Beat is the foundation. Light answers the beat. Color carries feeling. Garment serves movement. Spirit is optional but never fake.

---

## 1. What “floor-true” means

People integrated in rave culture tend to respond to:

| Signal | Feels real | Feels fake |
|--------|------------|------------|
| Light | Directional LEDs, lasers, strobe kiss, UV react | Flat rainbow overlay, random lens flares |
| Motion | Weight in the body, fabric following movement | Mannequin pose, frozen fashion-only |
| Color | Intentional limited palette with one hero glow | Every neon at once, no hierarchy |
| Texture | Mesh, compression, sweat-possible, reflective edges | Plastic chrome everything |
| Spirit | Quiet awe, unity, release, play | Random mandala stickers, appropriated sacred symbols without care |
| Community | Inclusive bodies, joy, no gatekeeping vibe | Exclusive clout, cruel irony |

**Never claim sacred traditions you do not hold.** Psychedelic-spiritual here means *feeling* — wonder, connection, release — not costume of another culture’s ceremony.

---

## 2. Master parameter stack (Midjourney v6 / v7 style)

Use as defaults; adjust per piece.

```text
--stylize 120–180
--v 6.1
--ar 3:4          (garment catalog / full body)
--ar 1:1          (detail crops, campaign squares)
--ar 16:9         (floor / environment plates)
--style raw       (when construction accuracy > illustration)
--sref [url]      (once you have a locked brand frame)
--cref 0–20         (only for controlled remix)
```

**Stylize guide**
- `80–120` — product / tech-pack readable
- `140–200` — campaign emotion, still garment-true
- `250+` — art only; not for manufacturer packages

---

## 3. Core prompt architecture

Always build in this order:

```text
[1 SUBJECT + GARMENT TRUTH]
[2 BODY + MOVEMENT]
[3 LIGHT + BEAT RESPONSE]
[4 COLOR HIERARCHY]
[5 ENVIRONMENT (optional)]
[6 CAMERA / LENS]
[7 QUALITY LOCKS]
[8 --params]
```

### 3.1 Subject + garment truth
Be specific: silhouette, fit, panel lines, materials, reflective behavior.

Good:
> compression bodysuit, diagonal tidal panels, matte nylon-spandex, selective cyan reflective edge only on seams

Bad:
> cool rave outfit glowing neon

### 3.2 Body + movement
- weight in feet
- soft bend in knees
- fabric lag on turn
- arms free for dance, not stiff fashion Vogue unless intentional

Inclusive casting language: varied bodies, no single “ideal only.”

### 3.3 Light + beat response
Light should feel like it has a tempo.

Blocks to mix:

```text
directional LED wash (magenta key, cyan rim)
subtle strobe catch on reflective edges only
laser haze in deep background, not on face
UV-reactive thread reading under blacklight kiss
warm practical from stage left, cool fill from right
```

Avoid: rainbow gradient overlays, random bokeh circles, lens flare spam.

### 3.4 Color hierarchy
Pick **one hero**, **one support**, **one ground**.

Examples:
- Hero cyan edge / support violet mesh / ground midnight teal
- Hero warm amber UV / support soft pink / ground black
- Hero white laser line / support deep indigo / ground charcoal

### 3.5 Environment (when not pure catalog)

```text
intimate warehouse floor, low haze, LED battens, speakers felt not seen
forest-edge night gathering, string lights + one laser tree, respectful and small-scale
dome interior, soft projection, bodies as silhouettes mid-phrase
```

Do **not** paste sacred geometry as decoration unless the collection concept earned it and the community context is respectful.

### 3.6 Camera

```text
full-body catalog, 50mm, eye level
3/4 movement crop, 35mm, slight low angle for power
macro seam detail, 90mm, shallow depth
```

### 3.7 Quality locks + negatives

Positive locks:
```text
sharp fabric detail, accurate construction, editorial ravewear catalog,
readable seams, no watermark, no logo text
```

Negatives (append):
```text
--no blurry, lowres, extra limbs, deformed hands, random logos, brand names,
watermark, plastic skin, oversharpen halos, rainbow chrome overload,
appropriated religious iconography, celebrity lookalike, text, letters
```

---

## 4. Psychedelic–spiritual layer (optional, careful)

Use only when the piece’s concept calls for it.

**Allowed emotional vocabulary**
- release, unity, play, wonder, soft ecstasy, quiet afterglow
- breath, heartbeat, bass as body
- light as shared signal not spectacle only

**Visual tools that read as sincere**
- soft radial light behind subject (not hard mandala stamp)
- color breathing between two hues on beat
- hands open, eyes soft or closed in feeling — not posed “enlightenment”
- small personal altar objects only if collection story includes them and ownership is clear

**Hard avoids**
- copying closed ceremonial dress or regalia
- random Sanskrit / sacred text as font decoration
- drug instruction imagery
- “shaman” costume stereotypes

Spiritual here = **felt state in community and body**, not cosplay of a tradition.

---

## 5. Ravewear-specific Midjourney recipes

### A. Catalog product (manufacturer-useful)

```text
full-body fashion product photo of [GARMENT TRUTH] on a fit model,
arms relaxed, weight even, clean dark studio, soft key + cyan rim light,
matte fabric readable, reflective edges catching light only where designed,
editorial ravewear catalog, sharp construction detail
--ar 3:4 --stylize 100 --style raw --v 6.1
```

### B. Floor movement (campaign)

```text
[GARMENT TRUTH], dancer mid-phrase on intimate warehouse floor,
fabric following a half-turn, magenta LED key + cyan rim, light haze,
bass felt in posture, joy without screaming expression,
candid-editorial, sharp garment detail
--ar 3:4 --stylize 160 --v 6.1
```

### C. Detail / hardware / reflective edge

```text
macro detail of [SEAM / MESH / REFLECTIVE EDGE], soft studio light
with single LED cyan kiss, fabric hand visible, catalog technical still
--ar 1:1 --stylize 80 --style raw --v 6.1
```

### D. Soft psychedelic afterglow (spiritual-leaning campaign)

```text
[GARMENT TRUTH], subject in quiet afterglow posture, eyes soft,
warm-cool light breathing between violet and teal, gentle haze,
no sacred symbols, only light and body and fabric,
intimate respectful tone, editorial
--ar 3:4 --stylize 180 --v 6.1
```

---

## 6. Brand consistency locks for Cherry

Once DROP001 assets exist, lock a style reference:

1. Generate 4–8 approved stills
2. Pick 1–2 as `--sref` anchors
3. Keep palette language: tidal teal, cyan edge, violet support, matte black ground
4. Always state: **designed by Cherry, partners sew** in copy — never in the image as text

---

## 7. Calibration checklist (before you accept a render)

- [ ] Garment construction still readable?
- [ ] One hero color, not neon soup?
- [ ] Light feels directional / tempo-aware?
- [ ] Body could actually dance in this?
- [ ] No fake sacred symbols?
- [ ] No brand/logo garbage?
- [ ] Matches package JSON colorway names?
- [ ] Useful for partner OR clearly labeled campaign-only?

If construction fails, drop stylize and use `--style raw`.
If soul fails, simplify environment and keep light honest.

---

## 8. Ethics & community respect

- Rave culture values consent, care, and inclusion — imagery should too
- No exploitation framing
- No medical or drug-use instruction
- Credit partners and makers in real life; images do not replace that
- Appropriation check on every spiritual-leaning piece

---

*Beat → light → color → body → joy. Everything else is decoration.*
