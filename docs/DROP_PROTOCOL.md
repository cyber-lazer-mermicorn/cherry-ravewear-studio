# Drop Protocol

## Naming

| Element | Pattern | Example |
|---------|---------|---------|
| Collection id | `DROP###` | `DROP001` |
| Package id | `RW-DROP###-###` | `RW-DROP001-001` |
| Folder | `collections/DROP001/` | |

## Minimum Drop contents

```text
collections/DROP001/
  COLLECTION.md
  packages/
    RW-DROP001-001.json
    RW-DROP001-001.md
  prompts/
    RW-DROP001-001-front.txt
    RW-DROP001-001-side.txt
    RW-DROP001-001-back.txt
    RW-DROP001-001-detail.txt
  assets/          # public-safe previews only
  private/         # gitignored or empty public stub
```

## Rules

1. Every package validates against `schemas/design-package.schema.json`.
2. Three colorways minimum.
3. Four views minimum (front, side, back, detail).
4. Open questions to manufacturers are required.
5. No claim that Cherry sews the garment.
6. Public assets are sanitized; masters stay private.
7. Rights point to mermicorn-grove/LICENSE.
