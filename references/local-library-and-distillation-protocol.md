# Local library and distillation protocol

## Contents

- Choose the processing route
- Minimum corpus record
- Build the evidence graph
- Distil in two passes
- Batch full-text processing
- Quality control

## Purpose

Turn a large local PDF collection into a searchable, auditable evidence corpus without
exposing confidential files or overwhelming one model context.

## Choose the processing route

Inspect the environment and corpus before installing anything.

- For tens of clean born-digital PDFs, use a local lightweight PDF extractor and a
  literature manager.
- For hundreds of PDFs, complex layouts, or reference-network work, prefer a locally run
  structured parser such as GROBID or an equivalent TEI-producing tool.
- For scanned PDFs, run local OCR first and preserve the original file.
- Use Docker only with user authorization and only after checking storage, ports, licensing,
  and whether a simpler local route is sufficient.
- Do not send unpublished manuscripts, reviewer files, or restricted PDFs to a public API.

Record the parser name, version, options, date, and failures. Keep file hashes so a changed
PDF cannot silently replace an extracted record.

## Minimum corpus record

Retain:

- stable record ID and local file path;
- file hash;
- title, authors, journal, year, and DOI;
- abstract and keywords when reliably extracted;
- page count and text-extraction status;
- reference list or structured reference links;
- access or acquisition status;
- parser confidence or manual-QC status;
- notes on missing, scanned, corrupted, or duplicate files.

Verify metadata against Crossref, a publisher record, or another authoritative bibliographic
source. PDF metadata alone is not authoritative.

## Build the evidence graph

Start with benchmark reviews and field-defining primary papers.

1. Parse their reference lists for backward citation candidates.
2. Retrieve forward citation metadata through a lawful scholarly graph service.
3. Deduplicate by normalized DOI, then title and author-year when a DOI is absent.
4. Label each candidate by why it may matter:
   `scope-gap`, `replication`, `contradiction`, `negative-result`, `method`, `field-scale`,
   `visual-source`, or `background-only`.
5. Download full text only when access is lawful. Otherwise place it in an acquisition queue
   for the user.

Do not treat a citation link as endorsement. Check the citing context and the primary paper.

## Distil in two passes

### First pass: coverage

- map materials, processes, outcomes, scales, dates, and study types;
- identify underrepresented subtopics;
- identify papers repeatedly cited through one research programme;
- separate reviews from primary evidence;
- populate the evidence matrix only with information present in the source.

### Second pass: change and contradiction

- compare what newer studies confirm, narrow, overturn, or leave unresolved;
- separate true replication from repeated mixtures or shared authorship;
- identify changes in material identity, water accounting, dispersion, curing, or test
  method that explain disagreement;
- record negative or null results;
- identify unanswered questions with an observable failure criterion.

Use this pass to update the review gap. Do not assume that a newer paper is better evidence.

## Batch full-text processing

Do not place an entire 200–300-paper corpus into one undifferentiated request.

- batch by a declared scientific question;
- keep a manifest of records included in each batch;
- produce evidence cards with DOI, page or section, method, result, limitation, and
  directness;
- merge cards into the master matrix;
- check batch summaries against source locations;
- preserve `not reported` rather than inferring missing values;
- re-run deduplication and contradiction checks after each major batch.

Draft from the master evidence matrix. Reopen the primary PDF for every decisive numerical,
causal, controversial, or visual claim.

## Quality control

Manually inspect:

- all benchmark papers;
- every paper supporting a central novelty claim;
- every external figure source;
- all records with missing or conflicting DOI metadata;
- a random sample from each extraction batch;
- every apparent contradiction before writing a causal explanation.

Report extraction failures and inaccessible papers as limitations rather than silently
discarding them.

