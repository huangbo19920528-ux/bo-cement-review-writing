---
name: bo-cement-review-writing
description: Plan, research, distil, draft, illustrate, revise, and audit evidence-grounded review manuscripts in cementitious and construction materials. Use for local PDF-library analysis, review-topic novelty checks, classic-review benchmarking, backward and forward citation chasing, DOI-verified evidence matrices, batch full-text synthesis, SCI/JBDE-style critical reviews, mechanism figures, published photographs and micrographs, figure permissions, DOCX production, benchmark comparison, and final scientific, visual, citation, and reproducibility audits. 适用于“本地PDF文献库、综述选题、经典综述拆解、引文追踪、二次蒸馏、SCI综述写作、核验参考文献、机理图与照片、版权溯源、逐页自查、对标高水平综述”等任务。
---

# Bo Cement Review Writing

Build a review as an auditable scientific synthesis. Treat corpus construction, topic
novelty, evidence traceability, visual provenance, journal fit, and rendered-page quality as
one connected workflow.

## Non-negotiable principles

1. Never invent a reference, DOI, author, result, permission statement, quotation, or figure
   source.
2. Verify bibliographic identity against a DOI registry or publisher record before citation.
3. Distinguish a verified publication from a valid interpretation of its evidence.
4. Do not upload confidential or unpublished files to an external service without explicit
   authorization.
5. Do not bulk-download paywalled papers or bypass access controls. Build an acquisition list
   for the user when lawful full text is unavailable.
6. Do not reproduce or adapt a published panel without a documented reuse basis.
7. Never use generative editing to fabricate, beautify, or replace experimental evidence.
8. Do not target a reference or figure count as a substitute for coverage and synthesis.
9. Keep numerical comparisons tied to dosage basis, water balance, mixture design, age,
   control, uncertainty, and test method.
10. Require author judgement for disputed interpretations, novelty claims, and final
    submission approval.

## Workflow

### 1. Build a secure local corpus

- Inventory supplied PDFs before searching for more sources.
- For a large corpus, use a local structured parser or literature manager rather than
  placing hundreds of raw PDFs in one prompt.
- Prefer a locally run, open workflow that preserves file hashes, source paths, page
  locations, metadata, abstracts, references, and extraction logs.
- Inspect the available environment before installing software. Use GROBID or an equivalent
  structured PDF parser when authorized; use a lightweight local extractor when Docker is
  unavailable.
- Manually quality-check a sample of extracted records and every source used for a decisive
  claim.

Read
[references/local-library-and-distillation-protocol.md](references/local-library-and-distillation-protocol.md)
before processing a large PDF collection.

### 2. Define the gap before fixing the title

- Record the target journal, intended scientific level, material system, practical problem,
  date range, and review type.
- Search recent reviews and primary studies around the proposed concept.
- Populate [assets/benchmark-review-matrix.csv](assets/benchmark-review-matrix.csv).
- Separate material, mechanism, outcome, application, date-range, method, and synthesis-axis
  overlap.
- Retain the topic only if it adds a defensible comparison unit, evidence framework,
  dataset, mechanism reconciliation, scale-up analysis, or reproducibility standard.
- Write a one-sentence novelty claim. Redesign the topic if its novelty is only “more recent
  papers.”

Read [references/benchmarking-protocol.md](references/benchmarking-protocol.md) when testing
topic novelty.

### 3. Learn the architecture of strong reviews

- Use two benchmark tiers:
  - inspect roughly 10–30 classic, highly influential, or field-defining reviews to learn
    recurring rhetorical and synthesis patterns;
  - select three to six directly comparable recent reviews for close structural and visual
    benchmarking.
- Extract how introductions establish the gap, methods delimit the corpus, sections compare
  evidence, contradictions are reconciled, figures carry evidence, and discussions close.
- Infer a reusable field-specific skeleton; do not copy sentences, figure layouts, or a
  single paper's outline.
- Record practices worth retaining and practices not worth imitating.

### 4. Expand and distil the evidence graph

- Use backward reference checking and forward citation searching from the benchmark set.
- Search Crossref, OpenAlex, Semantic Scholar, publisher records, or equivalent lawful
  sources for metadata and citation links.
- Add a cited or citing paper only when it closes a scope gap, provides independent
  replication, challenges an old conclusion, supplies missing negative evidence, or
  documents a method, field application, or visual source.
- Run a second distillation after new sources are added:
  - compare old and new conclusions;
  - identify repeated experiments and research-program dependence;
  - isolate unresolved contradictions and changed boundary conditions;
  - update the novelty claim and research questions.
- Treat citation counts as discovery signals, never as evidence quality.

### 5. Build a traceable evidence library

- Record databases, complete queries, search dates, filters, screening decisions, acquisition
  status, and update dates.
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
- Do not label a narrative search “systematic” unless its protocol supports the claim.

Read [references/manuscript-architecture.md](references/manuscript-architecture.md) when
building or shortening the outline.

### 7. Process full text in controlled batches

- Group full texts by research question, material class, mechanism, outcome, or time period.
- Extract evidence cards into the matrix before drafting prose.
- Preserve the source DOI, page or section, table or figure number, comparison basis, and an
  exact-location note for each decisive claim.
- Draft from verified evidence cards rather than from model memory or an undifferentiated
  pile of PDFs.
- Mark incomplete fields `not reported`; never fill them by inference.
- Reconcile batch summaries against the complete evidence matrix before section drafting.

### 8. Draft in claim–evidence units

- Start each paragraph with a scientific claim or comparison, then provide evidence,
  boundary conditions, disagreement, and interpretation.
- Use author-led sentences when attribution matters, without turning a section into a list
  of “X et al. found…” statements.
- Split distinct claims and place each citation beside the statement it supports.
- Prefer primary evidence for values and mechanisms; use reviews for orientation.
- Separate observation from explanation. Use restrained language when the mechanism is
  inferred rather than directly measured.
- Explain contradictions through material identity, water, dispersion, air, binder,
  admixture chemistry, curing, and test method before calling the literature inconsistent.
- Use evidence tables with one finding, comparison, limitation, or recommendation per row
  and a dedicated reference column.

### 9. Design the visual programme before drawing

- Build a visual-precedent bank from high-quality reviews and primary studies using
  [assets/visual-benchmark-matrix.csv](assets/visual-benchmark-matrix.csv).
- Record what each successful figure does, its evidence type, panel logic, typography,
  density, caption structure, and limitations. Learn the design grammar; do not copy its
  composition.
- Create one production brief per proposed figure using
  [assets/figure-brief.csv](assets/figure-brief.csv).
- Give every figure one primary question and one scientific job: scope, material identity,
  process evidence, quantitative comparison, microstructure, mechanism, field scale, or
  decision framework.
- Remove a figure when its role duplicates another, its evidence is weak, or it remains
  decorative.
- Use a real micrograph, test photograph, field photograph, or primary-source data panel when
  the original observation is the evidence. Use an original synthesis graphic when the
  review's cross-study interpretation is the contribution.

Read
[references/visual-benchmark-and-production-protocol.md](references/visual-benchmark-and-production-protocol.md)
before selecting or producing figures.

Validate the visual plan before drawing:

```bash
python scripts/validate_visual_plan.py \
  assets/figure-brief.csv assets/visual-benchmark-matrix.csv
```

### 10. Produce figures at panel level

- Record every external or adapted panel in
  [assets/figure-source-register.csv](assets/figure-source-register.csv).
- Place `(a)`, `(b)`, and later labels consistently at the upper left without opaque badges
  unless contrast requires one.
- Put panel descriptions in the caption, not as large titles inside the image.
- Preserve scale bars, axes, units, legends, and scientifically necessary annotations.
- Remove inherited panel letters and article-specific text only when permission and
  scientific integrity allow it; never crop a panel into an incomplete or misleading image.
- Standardize font, label size, line weight, border treatment, colour meaning, background,
  spacing, and final-width legibility across the manuscript.
- For mechanism figures, use editable vector construction and visually material-specific
  elements. Avoid generic boxes, childish icons, decorative gradients, and unexplained
  arrows.
- For published panels, retain observational truth. Do not reconstruct a micrograph,
  experimental photo, or result with generative imagery.
- Treat 8–12 substantive figures as a possible range for a long review, not a quota.

Validate the source register with:

```bash
python scripts/validate_figure_register.py assets/figure-source-register.csv
```

### 11. Synthesize, style, and shorten

- Compare material–mixture–processing combinations rather than papers.
- Grade confidence using directness, measurement quality, consistency, and independent
  replication.
- Identify stop criteria, failure modes, boundary conditions, and evidence maturity.
- Apply the target journal's current author guide and inspect recent accepted articles.
- Use a verified journal template or a restrained manuscript format. Do not imitate a random
  GitHub template or mechanically convert all prose to passive voice.
- Standardize terminology, tense, symbols, abbreviations, captions, and reference style.
- Remove generic background, repeated mechanisms, paper-by-paper catalogues, weak tables,
  decorative figures, and unsupported future applications.

### 12. Run author-led scientific and visual audits

- Compare the complete manuscript with the benchmark set.
- Render the complete DOCX or PDF and inspect every page at final readable size.
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
4. evidence, benchmark, figure-brief, and figure-source registers;
5. a benchmark-gap and contradiction summary;
6. a final audit summary separating verified facts from unresolved uncertainty;
7. a rendered, visually inspected DOCX or PDF when manuscript production is requested.

Do not expose confidential source files, internal reviewer documents, temporary render files,
or unpublished research data in final deliverables.

