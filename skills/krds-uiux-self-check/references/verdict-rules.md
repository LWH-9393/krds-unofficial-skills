# Verdict Rules

Use these rules before assigning `P`, `F`, `E`, or `N/A`.

## Verdict Meanings

- `P`
  - The item meets the source checklist's compliance criteria.
- `F`
  - The item does not meet the source checklist's compliance criteria.
- `E`
  - The source checklist treats the case as an exception.
- `N/A`
  - The reviewed screen or element does not contain the relevant target or the source notes the case as not applicable.

## Core Decision Rules

1. Judge against the compliance criteria, not against example failures.
2. If the compliance section references multiple procedure numbers, all of them must be satisfied.
3. If one source guideline is split across several checklist items, treat the guideline as met only when the related checklist items all pass.
4. If the item is outside scope for the reviewed screen, use `N/A` rather than forcing `F`.
5. If a documented exception applies, use `E` and record the reason briefly.

## Practical Interpretation Rules

### `P`

Use `P` only when the relevant compliance conditions are positively verified.
Absence of an obvious failure is not enough.

### `F`

Use `F` when:
- a required element is missing
- a required order or position is broken
- a required label or guidance is missing
- the checklist's explicit style or interaction requirement is not met
- the related latest KRDS page clearly invalidates the current implementation and the item is materially out of date

### `E`

Use `E` only when the checklist or the review context clearly identifies a legitimate exception.
Do not use `E` to avoid making a difficult judgment.

### `N/A`

Use `N/A` when:
- the screen does not contain that element or pattern
- the review scope intentionally excludes that family
- the source checklist says the case is not applicable

## Score Handling

The source document expects organizations to define a target score in advance, but it does not force a single universal score formula in the extracted sections reviewed here.

Repository convention when a user asks for a quick score:
- count only `P` and `F`
- exclude `E` and `N/A`
- compute `P / (P + F)`

State clearly that this score formula is a repository convention unless the user already has an organizational scoring rule.

## Reporting Discipline

For each `F`, record:
- checklist family
- checklist item
- reviewed screen or element
- short failure reason
- fix direction

That keeps the audit actionable rather than purely clerical.
