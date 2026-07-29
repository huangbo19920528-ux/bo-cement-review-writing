# Evidence and citation protocol

## Bibliographic verification

For every scholarly source:

1. resolve the DOI through a DOI registry or publisher;
2. confirm title, authors, journal, year, volume, issue, pages or article number;
3. deduplicate by normalized DOI;
4. record corrections rather than silently guessing missing metadata.

A DOI that resolves proves the bibliographic object exists. It does not prove that a quoted
interpretation, numerical value, or mechanism is correct.

## Evidence extraction

Use one row per material–mixture–processing–outcome combination. Record:

- source DOI, local record ID, page or section, and acquisition status;
- material source, pretreatment, morphology, and surface chemistry;
- dimensions, crystallinity, charge, solids, pH, and delivery state;
- dry-equivalent dosage and suspension dosage;
- carrier water and nominal/total water-to-binder ratio;
- binder, SCMs, aggregate, admixture, air, temperature, and curing;
- dispersion equipment, energy, duration, sequence, and rest time;
- outcome, age, control, replicate count, uncertainty, and test method;
- reported finding;
- review interpretation;
- limitation and evidence-directness class.

Use `not reported` rather than inventing a value.

## Citation chaining

Use benchmark reviews and field-defining primary studies as seeds.

- inspect backward references for original methods, early observations, and primary data;
- inspect forward citations for replication, changed boundary conditions, contradictions,
  negative results, and scale-up;
- use Crossref, OpenAlex, Semantic Scholar, publisher records, or equivalent lawful sources
  for discovery and metadata;
- verify the primary full text before using a citation context as evidence;
- record inaccessible full text in an acquisition queue rather than bypassing access.

Run a second distillation after citation chaining. Compare old and new evidence, connected
research programmes, unresolved disagreements, and claims whose scope has narrowed.

## Controlled batch processing

- group full texts by one declared research question;
- keep a batch manifest;
- extract evidence cards before drafting;
- retain page, section, table, or figure locations for decisive claims;
- merge cards into the master matrix and re-run deduplication;
- check batch summaries against source text;
- draft only after the matrix exposes sufficient coverage and contradiction handling.

Do not feed hundreds of unstructured PDFs into a single prompt and treat fluent prose as
evidence synthesis.

## Evidence hierarchy

- **Direct measurement:** the claimed variable was measured with an appropriate method.
- **Mechanism-supporting observation:** the result supports but does not uniquely establish
  the mechanism.
- **Triangulated inference:** several independent methods or studies converge.
- **Speculation:** plausible explanation without discriminating evidence.

Match the language to the class. Use “demonstrates” only for direct, discriminating evidence.

## Citation placement

- Put citations beside the exact supported statement.
- Split a sentence when different clauses require different sources.
- Prefer primary experiments for values and mechanisms.
- Use review articles for orientation, terminology, or broad field mapping.
- Avoid attaching many references to a broad claim without explaining their contribution.
- Identify connected papers from one research programme so they are not counted as
  independent replications.

## Reference-count discipline

The appropriate number depends on scope. A broad review may require well over 100 sources,
but a target count is never a quality criterion. Add a source only when it:

- closes a material, method, outcome, time, or scale gap;
- provides independent replication;
- supplies a standard or reporting method;
- supports a specific table or figure;
- documents image provenance or permission.

Remove duplicate reviews, weakly relevant citations, and sources cited only to inflate
coverage.

