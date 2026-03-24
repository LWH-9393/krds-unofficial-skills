---
name: krds-uiux-self-check
description: Audit a Korean public-sector website, portal, or service flow against the KRDS self-check checklist, including scope selection, review environment, P/F/E/N/A verdict rules, and report writing. Use when the user asks for self-check, audit, checklist-based review, compliance review sheet, or structured UI/UX validation based on the KRDS self-review checklist PDF.
---

# KRDS UIUX Self Check

Use this skill when the task is to run or structure a checklist-based self-audit for a Korean digital government service.

This skill is based on the `디지털 정부 서비스 UI/UX 가이드라인 자체 검증 체크리스트` document dated `2024.11`.
Use it as the audit framework.
Use [$krds-skill](../krds-skill/SKILL.md) alongside it when the user also needs the latest component-page verification on `krds.go.kr`.

## Quick Start

1. Define the audit target first.
   - Whole public website
   - Representative sample of screens
   - Specific component family
   - Specific service flow such as search, login, or application
2. Read [references/source-basis.md](references/source-basis.md) and [references/review-workflow.md](references/review-workflow.md) first.
3. Read [references/checklist-taxonomy.md](references/checklist-taxonomy.md) to choose the correct review categories.
4. Read [references/verdict-rules.md](references/verdict-rules.md) before assigning `P`, `F`, `E`, or `N/A`.
5. If the user asks for "latest KRDS" or the audit depends on current component behavior, verify the exact official KRDS pages with [$krds-skill](../krds-skill/SKILL.md) first and then apply this checklist framework.
6. Use [assets/self-check-report-template.md](assets/self-check-report-template.md) when the user needs a formal audit result sheet or a reusable review report structure.

## What This Skill Does

This skill should help with:
- selecting audit scope and representative screens
- preparing a consistent review environment
- mapping screens to checklist families
- applying checklist verdict semantics consistently
- writing a reusable self-check report
- separating official checklist-based failures from optional improvement advice

This skill should not:
- replace the latest official KRDS component-page verification
- invent new official checklist items not grounded in the source checklist
- treat mobile-web or mobile-app criteria as fully covered when the source document says they are not yet separately defined

## Working Rules

### 1. Start with scope, not findings

Before reviewing individual screens, identify:
- whether the audit is full-scope or sample-based
- which screen families are in scope
- which checklist families apply
- which items are clearly `E` or `N/A`

When a full audit is not realistic, prefer representative sampling.
The source checklist recommends at least 10 target screens when sampling across a service.

### 2. Keep the review environment stable

Use the source checklist environment as the baseline:
- Windows 10 or later required, macOS Monterey or later recommended
- 1920x1080 resolution
- latest Chrome
- 100% zoom
- no browser extensions or plugins
- cache and cookies cleared before testing
- keyboard and mouse interaction both checked

### 3. Review by checklist family

Choose only the relevant families:
- style
- component
- basic pattern
- service pattern

Do not force every checklist family onto every screen.

### 4. Separate official verdicts from improvement advice

For each reviewed item:
- assign the official-style verdict first: `P`, `F`, `E`, or `N/A`
- then add a short reason
- only after that, add improvement advice or a patch recommendation

Do not mark an item `P` just because it avoids an example failure.
It must satisfy the checklist's own compliance criteria.

### 5. Call out document-version limits explicitly

The self-check checklist document provides a strong structured audit baseline, but the KRDS component pages and kits have continued to evolve after `2024.11`.

If there is any conflict between:
- the document-era checklist framing, and
- the latest official KRDS component page

state that explicitly and prefer the latest official KRDS page for implementation details.

## Output Pattern

When using this skill, structure the answer in this order unless the user asks otherwise.

1. Audit scope and environment
2. Checklist families applied
3. Findings with `P/F/E/N/A`
4. High-priority failures and why they failed
5. Improvement actions
6. Optional report-ready summary

## References

- Source basis: [references/source-basis.md](references/source-basis.md)
- Review workflow: [references/review-workflow.md](references/review-workflow.md)
- Checklist taxonomy: [references/checklist-taxonomy.md](references/checklist-taxonomy.md)
- Verdict rules: [references/verdict-rules.md](references/verdict-rules.md)

## Assets

- Report template: [assets/self-check-report-template.md](assets/self-check-report-template.md)
