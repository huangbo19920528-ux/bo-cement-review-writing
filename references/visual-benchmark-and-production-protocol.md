# Visual benchmark and production protocol

## Contents

- Build a precedent bank
- Approve the visual programme
- Select the correct visual form
- Compose panels
- Caption pattern
- Visual quality gate
- Scientific image integrity

## Build a precedent bank

Inspect figures from directly relevant high-quality reviews and primary studies. Record each
candidate in `assets/visual-benchmark-matrix.csv`.

Extract:

- the scientific question answered;
- figure role and evidence type;
- whether the evidence is a real photograph, micrograph, quantitative plot, adapted concept,
  or original synthesis;
- panel count, reading order, balance, and whitespace;
- typography, label placement, colour logic, caption structure, and final-size legibility;
- why the figure works;
- what should not be copied;
- licence or permission implications.

Use precedent to learn visual grammar. Do not copy panel composition or redraw another
author's mechanism with superficial cosmetic changes.

## Approve the visual programme

Create one row per proposed figure in `assets/figure-brief.csv`. Approve a figure only when
all are clear:

1. the question it answers;
2. the evidence or synthesis it contributes;
3. why prose or a table is insufficient;
4. the intended source class for each panel;
5. the final journal width and minimum readable type;
6. the caption logic;
7. the permission route;
8. the criteria for retain, revise, replace, or delete.

One figure should carry one thesis. A multi-panel figure may combine evidence types only
when their relationship is explicit.

Before viewing a final composition, freeze the final-width acceptance criteria in
`assets/visual-acceptance-gate.csv`. Include the manuscript claim, source-register rows,
target width, minimum type, permitted panel density, hard blockers, and prior author
decisions. Do not reintroduce an author-rejected figure merely because a new layout is
available.

## Select the correct visual form

### Real observational evidence

Use a source micrograph, test photograph, failure image, or field photograph when the visual
observation itself matters. Preserve scale bars, orientation, scientifically necessary
labels, and the relation between the image and reported experiment.

Do not:

- regenerate or reconstruct the observation;
- remove defects to make it attractive;
- crop away evidence or make a partial image appear complete;
- combine panels from unrelated programmes as if they formed one experiment;
- repeat the same image or crop elsewhere in the manuscript.

### Quantitative comparison

Replot data only from traceable values with the comparison basis preserved. Show uncertainty,
sample size, dosage basis, age, control, and test method when relevant. Cite every source and
separate digitized values from directly reported values.

### Mechanism synthesis

Build an editable vector figure from the review's evidence synthesis.

- map every arrow and mechanism claim to supporting evidence;
- distinguish measured pathways from hypotheses visually and in the caption;
- use material-specific particles, hydrates, pores, fibres, interfaces, and scale cues;
- keep a clear causal direction and temporal or spatial hierarchy;
- use restrained colour and consistent symbols;
- avoid generic stock icons, childish geometry, ornamental gradients, excessive text, and
  unexplained arrows;
- do not trace a published mechanism and call it original.

### Scope or workflow

Keep only decision-relevant stages. Use unique verbs and remove repeated labels such as
generic `report`, `test`, or `retain` when they do not convey distinct decisions. Do not add
decorative checkpoints.

## Compose panels

- Use `(a)`, `(b)`, and later labels at the upper left.
- Prefer plain high-contrast text; avoid a black badge unless the image requires it.
- Use one label size and offset across all figures.
- Put panel descriptions in the caption.
- Remove inherited panel letters when lawful and scientifically safe.
- Do not place titles or long explanatory prose on the image.
- Use equal optical margins, aligned baselines, coherent borders, and balanced panel areas.
- Give detailed evidence enough area; do not shrink a dense plot or legend until unreadable.
- Use one source image per panel unless the panel is explicitly a labelled montage.
- Allow up to four simple observational panels when they form one readable comparison.
- Prefer no more than two detailed panels when axes, legends, scale bars, or source
  annotations must remain legible.
- Split protocol, response, mechanism, microstructure, and field evidence into separate
  figures when they do not answer one causal question.
- Use a restrained, coherent palette and visually consistent flat/vector assets for original
  synthesis figures. Do not force published observations into a cosmetic common style.

## Caption pattern

Write a concise lead stating the figure's scientific purpose, followed by panel mappings:

`Fig. X. [Scientific purpose]: (a) ...; (b) ...; and (c) ....`

Then state `adapted from` or `reproduced from`, include citations, identify modifications
when required, and use the publisher-mandated attribution. Do not write workflow notes such
as “under CC BY” in the body when formal caption attribution is sufficient.

## Visual quality gate

Inspect the figure only after embedding and rendering it at final page width. Reject any
figure with:

- incomplete or clipped source content;
- illegible labels, legends, or scale bars;
- mixed font families or visibly inconsistent label sizes;
- duplicated or near-duplicated images;
- unresolved legacy panel marks;
- generic diagram elements that do not encode the material system;
- text overlapping evidence;
- panels with mismatched visual grammar and no scientific reason;
- a caption that cannot explain why every panel is present;
- missing or unresolved permission;
- a prior author decision that has been silently reversed.

Compare the complete figure set against the precedent bank. Match scientific density,
clarity, and finish—not another article's appearance.

Use at most two critique-and-revision rounds. If a hard blocker remains, split, replace, or
delete the figure rather than continuing cosmetic iteration. Prefer hard blockers over one
aggregate attractiveness score.

## Scientific image integrity

Keep original source files and an edit log. Allow only disclosed operations that do not alter
scientific meaning, such as uniform cropping, sizing, or global tonal adjustment when
permitted. Never use generative fill, object removal, synthetic texture, or image generation
to represent experimental evidence. Follow the target journal's current image-integrity and
AI-disclosure policies.
