# Texture Activation Rules

Use this file to decide whether the texture layer should be added at all.

## Fast Decision Tree

1. Has KRDS compliance already been verified?
   - No: use [$krds-skill](../krds-skill/SKILL.md) first.
   - Yes: continue.
2. Is the target public-facing and expected to resemble a live service?
   - Yes: texture is usually appropriate.
   - No: skip texture or apply only a minimal ownership block.
3. Does the screen feel like a demo because it lacks ownership, notices, attachments, filters, or operational metadata?
   - Yes: add the smallest texture partials that solve the gap.
   - No: do not add density for its own sake.
4. Are institution names, contacts, dates, or receipt numbers still sample data?
   - Yes: do not ship until placeholder lint passes.

## Rule Table

| Rule ID | Apply texture when | Skip or limit texture when | Recommended assets |
| --- | --- | --- | --- |
| `TEXTURE-RULE-001` | The user explicitly wants a real public-service feel, not just KRDS compliance. | The request is purely about compliance or accessibility review. | Start with [home-service-layout.html](../assets/home-service-layout.html) or [notice-list-panel.html](../assets/notice-list-panel.html). |
| `TEXTURE-RULE-002` | The page is public-facing and needs service-entry, notice, support, or ownership cues. | The page is an internal admin, operations, or back-office screen. | [contact-owner-box.html](../assets/contact-owner-box.html) |
| `TEXTURE-RULE-003` | A list page feels too clean or empty and needs real retrieval controls. | The page is only a short curated menu or a landing shortcut page. | [search-filter-toolbar.html](../assets/search-filter-toolbar.html), [notice-list-panel.html](../assets/notice-list-panel.html) |
| `TEXTURE-RULE-004` | A detail page needs downloadable files, owner info, or related links. | The detail page has no durable content to support those blocks. | [attachment-list.html](../assets/attachment-list.html), [contact-owner-box.html](../assets/contact-owner-box.html) |
| `TEXTURE-RULE-005` | A form needs preparation context, support, and realistic next-step cues. | The action is a trivial one-step update where extra density would distract. | Use texture around the base KRDS form rather than replacing it. |
| `TEXTURE-RULE-006` | The page already follows KRDS but still reads like a design-system sample. | The page already contains enough real operational density. | Add only the missing partials, not all texture assets at once. |

## Guardrails

- Never use texture to justify breaking KRDS trust-marker rules.
- Never add operational density with stale or placeholder content.
- Prefer one or two believable public-service blocks over a full page of decorative "realism".
- If the page already has enough metadata and support cues, stop.
