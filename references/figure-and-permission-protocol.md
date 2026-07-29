# Figure and permission protocol

Use this file for source provenance and permission decisions. Use
`references/visual-benchmark-and-production-protocol.md` for precedent selection, figure
briefs, composition, and visual quality.

## Figure roles

Assign one primary role to each figure:

- scope or taxonomy;
- material identity and morphology;
- process or dispersion evidence;
- quantitative performance comparison;
- microstructure or test evidence;
- mechanism synthesis;
- field or structure-scale demonstration;
- evidence maturity or decision framework.

Delete a figure whose role duplicates another figure.

## Source classes

### Original synthesis

Redraw the review authors’ own cross-study logic, comparisons, and decision frameworks.
Do not trace a published figure and call it original.

### Adapted published content

Document the exact source, panel or figure number, modifications, license, attribution text,
and whether additional permission is required.

### Reproduced published content

Use only when the original image itself is evidence, such as a micrograph, test photograph,
or field image. Preserve scientifically necessary information and meet the license or
permission terms.

### Institutional or government photograph

Record the institution, page URL, image title, creator if supplied, date, usage restriction,
and access date. Public availability does not automatically mean unrestricted reuse.

## Panel design

- Place `(a)`, `(b)`, and later labels at the upper left using one style.
- Prefer plain high-contrast labels without opaque badges unless image contrast requires
  one.
- Keep labels clear without obscuring the evidence.
- Remove inherited panel letters when composing a new multi-panel figure, unless permission
  or scientific integrity requires the unmodified original.
- Put panel descriptions in the figure caption.
- Do not place decorative subtitles or repeated explanatory prose inside the image.
- Use legible type at final printed size.
- Preserve scale bars, axes, units, legends, and required annotations.
- Do not stretch, crop away data, or present a partial image as complete.
- Use one source image per panel unless the panel is explicitly a labelled montage.
- Reject a panel whose source text, scale bar, legend, or boundary is visibly incomplete.

## Mechanism figures

- Build editable vector artwork from the review's synthesis.
- Link each arrow, process, or causal claim to evidence.
- Distinguish measured mechanisms from hypotheses.
- Use material-specific visual elements and meaningful scale or time hierarchy.
- Avoid stock icons, generic boxes, childish geometry, decorative gradients, dense prose,
  and unexplained arrows.
- Do not trace a published mechanism or use generative imagery to simulate experimental
  evidence.

## Quality checks

- compare each panel against the registered source;
- check for duplicate source IDs and duplicate image hashes;
- inspect legends and text at final page scale;
- confirm each panel passes completeness, legacy-label, scientific-annotation, resolution,
  and final-size-legibility checks;
- confirm colour meaning is consistent and remains interpretable in grayscale;
- state when panels document different programmes rather than one paired experiment;
- avoid implying validation beyond the scale actually shown.

## Permission register fields

Complete `assets/figure-source-register.csv` before submission. `permission_status` should be
one of:

- `original`;
- `public-domain`;
- `open-license`;
- `permission-obtained`;
- `permission-required`;
- `not-used`.

Do not submit a figure with `permission-required`.
Do not mark `final_visual_check` as `pass` until the figure has been rendered at its intended
page width and inspected with its caption.

