---
name: bo-cement-review-writing
description: Plan, research, distil, draft, illustrate, revise, target, and audit evidence-grounded review manuscripts in cementitious and construction materials. Use for local PDF-library analysis, topic-novelty checks, high-ambition journal ladders, article-type and invitation eligibility checks, classic-review benchmarking, citation chasing, DOI-verified evidence matrices, quantitative or critical synthesis, mechanism figures, published photographs and micrographs, figure permissions, editorial pitches, journal-cascade planning, DOCX production, and final scientific, visual, citation, policy, and reproducibility audits. 閫傜敤浜庘€滄湰鍦癙DF鏂囩尞搴撱€佺患杩伴€夐銆侀珮瀹氫綅鏈熷垔鍒嗗眰銆侀個绋胯祫鏍兼牳楠屻€佺粡鍏哥患杩版媶瑙ｃ€佸紩鏂囪拷韪€佷簩娆¤捀棣忋€丼CI缁艰堪鍐欎綔銆佸畾閲忕患鍚堛€佹牳楠屽弬鑰冩枃鐚€佹満鐞嗗浘涓庣収鐗囥€佺増鏉冩函婧愩€侀€愰〉鑷煡銆佸鏍囬珮姘村钩缁艰堪銆侀檷妗ｈ浆鎶曗€濈瓑浠诲姟銆?---

# Bo Cement Review Writing

Build a review as an auditable scientific synthesis. Treat corpus construction, topic
novelty, evidence traceability, visual provenance, journal fit, author decisions, and
rendered-page quality as one connected workflow.

## Non-negotiable principles

1. Never invent a reference, DOI, author, result, permission statement, quotation, or
   figure source.
2. Verify bibliographic identity against a DOI registry or publisher record before
   citation.
3. Distinguish a verified publication from a valid interpretation of its evidence.
4. Do not upload confidential or unpublished files to an external service without explicit
   authorization.
5. Do not bulk-download paywalled papers or bypass access controls. Build an acquisition
   list when lawful full text is unavailable.
6. Do not reproduce or adapt a published panel without a documented reuse basis.
7. Never use generative editing to fabricate, beautify, or replace experimental evidence.
8. Do not target a reference or figure count as a substitute for coverage and synthesis.
9. Keep numerical comparisons tied to dosage basis, water balance, mixture design, age,
   control, uncertainty, and test method.
10. Preserve explicit author decisions. Do not reintroduce a deleted figure, rejected
    source, removed section, or superseded interpretation unless the author reverses the
    decision.
11. Require author judgement for disputed interpretations, novelty claims, and final
    submission approval.
12. Verify current journal scope, article-type eligibility, invitation status, author
    guide, and AI/data policies from live official sources; never rely on remembered
    rankings or an old template.
13. Aim at the highest scientifically defensible venue, but do not inflate method labels,
    evidence maturity, mechanism certainty, quantitative precision, or application
    readiness to mimic a prestigious journal.

## Workflow

### 1. Build a secure local corpus

- Inventory supplied PDFs before searching for more sources.
- For a large corpus, use a local structured parser or literature manager rather than
  placing hundreds of raw PDFs in one prompt.
- Preserve file hashes, source paths, page locations, metadata, abstracts, references,
  and extraction logs.
- Inspect the environment before installing software. Use GROBID or an equivalent local
  structured parser when authorized; use a lightweight extractor when Docker is
  unavailable.
- Manually quality-check a sample of extracted records and every source used for a
  decisive claim.

Read
[references/local-library-and-distillation-protocol.md](references/local-library-and-distillation-protocol.md)
before processing a large PDF collection.

### 2. Define the gap before fixing the title

- Record a three-level target ladder: stretch, best-fit, and floor journals. For each,
  verify scope, readership, accepted review type, invitation or proposal requirements,
  current author guide, and recent comparable reviews.
- Classify the intended synthesis profile as mechanism-to-performance,
  application-to-performance, evidence-to-design, or a justified hybrid.
- Populate [assets/journal-target-ladder.csv](assets/journal-target-ladder.csv) before
  committing to a journal-specific rewrite.
- Record the intended scientific level, material system, practical problem, date range,
  and review type.
- Search recent reviews and primary studies around the proposed concept.
- Populate [assets/benchmark-review-matrix.csv](assets/benchmark-review-matrix.csv).
- Separate material, mechanism, outcome, application, date-range, method, and synthesis-axis
  overlap.
- Retain the topic only if it adds a defensible comparison unit, evidence framework,
  dataset, mechanism reconciliation, scale-up analysis, or reproducibility standard.
- Write a one-sentence novelty claim. Redesign the topic if its novelty is only 鈥渕ore
  recent papers.鈥?
Read [references/benchmarking-protocol.md](references/benchmarking-protocol.md) when testing
topic novelty.

Read
[references/high-ambition-journal-routing.md](references/high-ambition-journal-routing.md)
before selecting a stretch journal, preparing an editorial proposal, or planning a
high-to-lower journal cascade.

Validate the target ladder:

```bash
python scripts/validate_journal_profile.py assets/journal-target-ladder.csv
```

### 3. Learn the architecture of strong reviews

- Inspect roughly 10鈥?0 classic, influential, or field-defining reviews for recurring
  rhetorical and synthesis patterns.
- Select three to six directly comparable recent reviews for close structural and visual
  benchmarking.
- Extract how introductions establish the gap, methods delimit the corpus, sections compare
  evidence, contradictions are reconciled, figures carry evidence, and discussions close.
- Infer a reusable field-specific skeleton. Do not copy sentences, figure layouts, or a
  single paper's outline.
- Record practices worth retaining and practices not worth imitating.

### 4. Separate tool roles and expand the evidence graph

- Use discovery tools for finding literature, a controlled full-text library for
  source-grounded synthesis, and an analysis model for gap finding and drafting.
- Do not ask a discovery engine to substitute for reading and evidence extraction.
- Treat retrieval-augmented answers as navigation aids, not verified evidence; open the
  cited full text and check the exact passage, table, or figure.
- Use backward reference checking and forward citation searching from the benchmark set.
- Search Crossref, OpenAlex, Semantic Scholar, publisher records, or equivalent lawful
  sources for metadata and citation links.
- Add a paper only when it closes a scope gap, provides independent replication, challenges
  an old conclusion, supplies missing negative evidence, or documents a method, field
  application, or visual source.
- Run a second distillation after new sources are added to compare old and new conclusions,
  repeated experiments, unresolved contradictions, and changed boundary conditions.
- Treat citation counts as discovery signals, never as evidence quality.

### 5. Build a traceable evidence library

- Record databases, complete queries, search dates, filters, screening decisions,
  acquisition status, and update dates.
- Use [assets/evidence-matrix.csv](assets/evidence-matrix.csv) for study-level extraction.
- Verify each DOI and normalize duplicate records.
- Classify each source as primary experiment, method/standard, review, modelling/LCA, field
  demonstration, or image-provenance record.
- Mark evidence directness: direct measurement, mechanism-supporting observation,
  triangulated inference, or speculation.
- Treat connected papers from one research programme as connected evidence, not independent
  replication.

Read [references/evidence-and-citation-protocol.md](references/evidence-and-citation-protocol.md)
before finalizing the library.

### 6. Design a question-led architecture

- Make every main section answer a scientific question.
- Allocate approximate word, table, figure, and evidence budgets before drafting.
- Keep a subsection only when it can support a claim, comparative evidence, boundary
  conditions, and synthesis. Merge one- or two-paragraph fragments.
- Use this default sequence when appropriate:
  1. problem, gap, scope, and contribution;
  2. search and critical-appraisal method;
  3. material identity, delivery state, and processing;
  4. mechanisms across fresh, early-age, and hardened states;
  5. performance and boundary conditions;
  6. emerging classes or application pathways;
  7. cross-study synthesis and design implications;
  8. scale-up, sustainability, reporting requirements, and research agenda;
  9. conclusions.
- Do not label a narrative search 鈥渟ystematic鈥?unless its protocol supports the claim.

Read [references/manuscript-architecture.md](references/manuscript-architecture.md) when
building or shortening the outline.

### 7. Process full text in controlled batches

- Group full texts by research question, material class, mechanism, outcome, or period.
- Extract evidence cards into the matrix before drafting prose.
- Preserve DOI, page or section, table or figure number, comparison basis, and an
  exact-location note for each decisive claim.
- Draft from verified evidence cards rather than model memory or an undifferentiated pile
  of PDFs.
- Mark incomplete fields `not reported`; never fill them by inference.
- Reconcile batch summaries against the complete evidence matrix before section drafting.

### 8. Draft in claim鈥揺vidence units

- Start each paragraph with a scientific claim or comparison, then provide evidence,
  boundary conditions, disagreement, and interpretation.
- Use author-led sentences when attribution matters, without turning a section into a list
  of 鈥淴 et al. found鈥︹€?statements.
- Split distinct claims and place each citation beside the statement it supports.
- Prefer primary evidence for values and mechanisms; use reviews for orientation.
- Separate observation from explanation. Use restrained language when the mechanism is
  inferred rather than measured.
- Explain contradictions through material identity, water, dispersion, air, binder,
  admixture chemistry, curing, and test method before calling the literature inconsistent.
- Use evidence tables with one finding, comparison, limitation, or recommendation per row
  and a dedicated reference column.

### 9. Design and precommit the visual programme

- Build a visual-precedent bank from high-quality reviews and primary studies using
  [assets/visual-benchmark-matrix.csv](assets/visual-benchmark-matrix.csv).
- Learn visual grammar鈥攓uestion, evidence type, panel logic, typography, density, caption
  structure, and limitations鈥攚ithout copying composition.
- Create one production brief per proposed figure using
  [assets/figure-brief.csv](assets/figure-brief.csv).
- Give every figure one primary question and one scientific job: scope, material identity,
  process evidence, quantitative comparison, microstructure, mechanism, field scale, or
  decision framework.
- Under a high-ambition profile, require the opening visual programme to include at least
  one author-original synthesis that changes how evidence is compared or used. A collage,
  taxonomy, or decorative graphical abstract does not satisfy this requirement.
- Prefer information gain over figure count. For mechanism-oriented venues, prioritize
  causal evidence maps, normalized comparisons, competing-hypothesis figures, and
  uncertainty. For application-oriented venues, prioritize validated design windows,
  durability, constructability, scale, and decision matrices.
- Freeze acceptance criteria before producing or viewing the final composition. Record them
  in [assets/visual-acceptance-gate.csv](assets/visual-acceptance-gate.csv).
- Remove a figure when its role duplicates another, its evidence is weak, the author
  rejected it, or it remains decorative.
- Use real micrographs, test photographs, field photographs, or primary-source data when
  the observation is evidence. Use an original synthesis graphic only when the review's
  cross-study interpretation is the contribution.
- Do not require an AI-generated figure. Generative assistance may support non-evidentiary
  style ideation only; it must never replace scientific observations, plots, scale bars,
  or source-grounded mechanisms.

Read
[references/visual-benchmark-and-production-protocol.md](references/visual-benchmark-and-production-protocol.md)
before selecting or producing figures.

Validate the plan before drawing:

```bash
python scripts/validate_visual_plan.py \
  assets/figure-brief.csv assets/visual-benchmark-matrix.csv
```

### 10. Produce and trace figures at panel level

- Record every external or adapted panel in
  [assets/figure-source-register.csv](assets/figure-source-register.csv).
- Link every panel to its source, transformation, caption claim, manuscript claim, and
  limitation.
- Place `(a)`, `(b)`, and later labels consistently at the upper left without opaque
  badges unless contrast requires one.
- Put panel descriptions in the caption, not as large titles inside the image.
- Preserve scale bars, axes, units, legends, and necessary annotations.
- Remove inherited panel letters and article-specific text only when permission and
  scientific integrity allow it. Never crop a panel into an incomplete or misleading
  image.
- Standardize font, label size, line weight, border treatment, colour meaning, background,
  spacing, and final-width legibility.
- Use a restrained, coherent palette and consistent flat/vector assets when creating an
  original synthesis.
- For mechanism figures, use editable vector construction and material-specific elements.
  Avoid generic boxes, childish icons, decorative gradients, and unexplained arrows.
- For published panels, retain observational truth. Do not reconstruct a micrograph,
  experimental photograph, or result with generative imagery.
- If a panel contains dense axes, legends, microstructural annotations, or source text,
  allocate enough area for final-size reading. Split mixed scientific jobs into separate
  figures rather than shrinking them.
- Treat 8鈥?2 substantive figures as a possible range for a long review, not a quota.

Validate provenance:

```bash
python scripts/validate_figure_register.py assets/figure-source-register.csv
```

### 11. Run a bounded adversarial visual review

- Render each figure inside the manuscript at its intended column or page width.
- Apply the frozen criteria in `visual-acceptance-gate.csv`; do not invent new criteria
  after seeing the result merely to justify a preferred figure.
- Reject any figure with unreadable final-size text, incomplete content, duplicated panels,
  unresolved legacy labels, misleading pairing, unsupported mechanism arrows, or unresolved
  permission.
- Use at most two critique-and-revision rounds per figure. If a hard blocker remains after
  two rounds, split, replace, or delete the figure.
- Prefer hard pass/fail blockers over a single subjective attractiveness score.
- Compare the whole set for palette, typography, panel labels, optical margins, evidence
  density, and repetition.

Read
[references/adversarial-visual-review-protocol.md](references/adversarial-visual-review-protocol.md)
before the final figure pass, then validate:

```bash
python scripts/validate_visual_acceptance.py assets/visual-acceptance-gate.csv
```

### 12. Synthesize, style, shorten, and audit

- Compare material鈥搈ixture鈥損rocessing combinations rather than papers.
- Grade confidence using directness, measurement quality, consistency, and independent
  replication.
- Identify stop criteria, failure modes, boundary conditions, and evidence maturity.
- Apply the target journal's current author guide and inspect recent accepted articles.
- Run a desk-rejection simulation against scope, article eligibility, novelty relative to
  recent reviews, evidence density, method-label accuracy, quantitative contribution,
  visual information gain, and reader utility.
- If the review is targeted rather than exhaustive, say so plainly and report its
  limitations; do not add PRISMA language or a flow diagram to create an appearance of
  systematicity.
- When data permit, normalize and synthesize effect magnitudes. When they do not, make the
  missing descriptors and incompatible comparison bases an explicit result rather than
  inventing pooled precision.
- Prepare a transfer map before submission: identify which sections, figures, abstract
  emphasis, and application depth would change for the best-fit and floor journals. Never
  merely replace the journal name.
- Use a verified journal template or restrained manuscript format. Do not imitate a random
  template or mechanically convert all prose to passive voice.
- Remove generic background, repeated mechanisms, paper-by-paper catalogues, weak tables,
  decorative figures, and unsupported future applications.
- Render the complete DOCX or PDF and inspect every page at 100% final reading size.
- Run [references/final-audit.md](references/final-audit.md).
- For a DOCX manuscript, run:

```bash
python scripts/audit_review_docx.py manuscript.docx
```

- Confirm sequential numbering and complete citation resolution.
- Check duplicate embedded images by hash and inspect visual near-duplicates manually.
- Inspect captions, panel completeness, equations, subscripts, superscripts, symbols, units,
  legends, and scale bars.
- Require the author to revise hard transitions, add original judgement on controversies,
  verify claim-level citations, and approve the final interpretation.

## Deliverables

Unless the user requests otherwise, deliver:

1. a novelty and scope statement;
2. a corpus and search record;
3. a question-led outline or revised manuscript;
4. evidence, benchmark, figure-brief, figure-source, and visual-acceptance registers;
5. a benchmark-gap and contradiction summary;
6. a final audit summary separating verified facts from unresolved uncertainty;
7. a target-journal ladder, eligibility record, and transfer map when journal targeting is
   requested;
8. a rendered, visually inspected DOCX or PDF when manuscript production is requested.

Do not expose confidential source files, internal reviewer documents, temporary render files,
or unpublished research data in final deliverables.

