# KRDS Decision Rules

Use this file when the correct KRDS pattern is unclear or when a local asset seems "almost right" but context rules matter.

## Fast Decision Tree

1. Is the target an actual digital government service?
   - Yes: official banner may be used, and identifier may be used in the footer's last section.
   - No: omit both official banner and identifier.
2. Is the page an interior page with meaningful hierarchy depth?
   - Yes: breadcrumb can be used directly above the page title.
   - No: omit breadcrumb.
3. Is the page a complex public application input step?
   - Yes: provide at least one help path and prefer the current KRDS help-panel pattern when that panel form fits.
   - No: do not add help-panel UI by habit.
4. Is the submission irreversible or not editable after submit?
   - Yes: include a confirm step before final submission.
   - No: confirm is optional.
   - Exception: issuance-style repetitive requests can omit confirm even when the result itself is irreversible.
5. Has submission completed successfully?
   - Yes: always show a completion step.
   - If a confirm step already existed: omit the full detailed submitted-information summary on the completion screen.

## Rule Table

| Rule ID | Pattern | Use when | Do not use when | Required checks | Official basis |
| --- | --- | --- | --- | --- | --- |
| `KRDS-RULE-001` | Official banner | The site is an official digital government service. | The site is not an official digital government service. | Banner text/style must remain official; skip link must come before repeated regions. | [공식 배너](https://www.krds.go.kr/html/site/component/component_02_01.html) |
| `KRDS-RULE-002` | Operating institution identifier | The site is an official digital government service and the footer is present. | The site is unofficial, private, internal, or the identifier would sit outside the footer. | Use the operating institution logo, keep the official text pattern, place it in the footer's last section. | [운영기관 식별자](https://www.krds.go.kr/html/site/component/component_02_02.html) |
| `KRDS-RULE-003` | Header service identity | Every public-facing shell. | Never omit on a page that is part of the same service shell. | The identity must link to the main page. | [헤더](https://www.krds.go.kr/html/site/component/component_02_03.html) |
| `KRDS-RULE-004` | Footer | Every public-facing shell. | Do not replace with a minimal copyright-only strip. | Keep service logo, contact info, utility links, policy links, emphasized privacy policy, and copyright. | [푸터](https://www.krds.go.kr/html/site/component/component_02_04.html) |
| `KRDS-RULE-005` | Breadcrumb | Interior pages with real hierarchy depth and a stable parent path. | Main pages, landing pages, or shallow structures where breadcrumb adds little value. | `aria-label="브레드크럼"`, ordered list, home item first, current item non-link when needed, ellipsis when the visible path would exceed four links. | [브레드크럼](https://www.krds.go.kr/html/site/component/component_03_03.html) |
| `KRDS-RULE-006` | Help panel | Complex public forms where users may need contextual help, examples, or contact info while filling the form. | Simple low-risk inputs or screens where inline guidance is sufficient. | Keep the current trigger and panel structure; on narrow screens, the panel can collapse to an open button. | [도움 패널](https://www.krds.go.kr/html/site/component/component_08_01.html), [신청서 작성](https://www.krds.go.kr/html/site/service/service_04_05.html) |
| `KRDS-RULE-007` | Confirm step | Submission cannot be cancelled, withdrawn, or edited later. | Reversible submissions or issuance-style repetitive requests where KRDS allows omission. | Summarize key values only; provide confirm and back actions; state the irreversible consequences. | [확인·확정](https://www.krds.go.kr/html/site/service/service_04_06.html) |
| `KRDS-RULE-008` | Complete step | Every successful submission flow. | Never skip after a successful submission. | Confirm success and next steps; if confirm already existed, omit repeated full-data summary. | [완료](https://www.krds.go.kr/html/site/service/service_04_07.html) |

## Standardized Edge Cases

### Breadcrumb depth

- If the page is effectively "home -> current page" and the page title already carries the location clearly, omit the breadcrumb.
- If the breadcrumb would need more than four visible links on a wide screen, collapse the middle path using the KRDS ellipsis pattern.
- If no valid parent link exists, keep the terminal item as text, not as a dead link.

### Confirm-step exception

- Default to including confirm when the user cannot safely recover from a bad submission.
- Omit confirm only when the request is effectively repeatable issuance and the user can simply perform the request again without unique irreversible data loss.
- When in doubt, include confirm and keep it concise.

### Completion summary

- If confirm did not exist, the completion page may summarize key information.
- If confirm already existed, the completion page should focus on success, receipt/status path, and next actions rather than repeating the same review block.
