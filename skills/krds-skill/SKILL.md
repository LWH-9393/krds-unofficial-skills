---
name: krds-skill
description: Apply the latest official KRDS guidance to Korean public-sector websites, portals, dashboards, and admin screens. Use when creating, reviewing, or refactoring a public institution web UI that should follow current KRDS information architecture, accessibility, content patterns, trust markers, and public-service templates.
---

# KRDS Skill

Use this skill to align a Korean public-sector web service with KRDS conventions without blindly copying the KRDS site.

## Quick Start

1. Identify the screen type first.
   - Public portal
   - Internal work portal
   - Admin or operations screen
2. Read [references/krds-verification.md](references/krds-verification.md) and [references/asset-verification-manifest.yaml](references/asset-verification-manifest.yaml) first before using any bundled asset.
3. Read [references/krds-principles.md](references/krds-principles.md) for baseline rules.
4. Read [references/decision-rules.md](references/decision-rules.md) when the correct pattern or omission condition is unclear.
5. Read [references/krds-public-checklist.md](references/krds-public-checklist.md) when designing or reviewing a public-facing page.
6. For a public-facing page, confirm the shell includes a skip link, a home-linked service identity, main navigation, and a footer built from the current KRDS footer pattern.
7. Only use the official banner on an actual digital government service, and pull the current official snippet from `krds.go.kr` without altering its text or style.
8. Only use breadcrumb on interior pages with real hierarchy depth. Do not place it on main pages, landing pages, or shallow two-level structures.
9. Reuse assets from `assets/` only after the official KRDS date/version check and the structural requirements above fit the target page.
10. Preserve keyboard focus, heading order, and current-location cues when lifting any markup or CSS.
11. Run `scripts/check_placeholders.py` against the target implementation before production handoff when example strings might still be present.
12. Keep the output focused on structure, clarity, accessibility, and trust markers.
13. Prefer official KRDS sources on `krds.go.kr` when you need to verify a pattern.

## Asset Use Order

When the request involves actual UI implementation, use assets in this order.

1. Relevant official KRDS page on `krds.go.kr`
   - Check the page's information change history and linked HTML Component Kit version first.
2. [references/asset-verification-manifest.yaml](references/asset-verification-manifest.yaml)
   - Confirm the asset-to-official-page mapping, last verification date, change date, kit version, and use conditions.
3. `assets/krds-tokens.css`
   - Start with color, spacing, radius, shadow, and typography tokens.
4. `assets/krds-components.css`
   - Reuse public-service components such as skip links, header, breadcrumb, quick links, board list, board detail, badges, forms, step indicators, help-panel trigger and panel states, confirmation panels, completion panels, page actions, and footer.
5. HTML templates
   - `assets/portal-shell.html`
   - `assets/breadcrumb.html`
   - `assets/board-list.html`
   - `assets/board-detail.html`
   - `assets/application-form.html`
   - `assets/application-confirm.html`
   - `assets/application-complete.html`
   - `assets/public-dashboard.html`
6. SVG icons in `assets/icons/`
   - Use only when they support navigation or actions.

Do not copy every asset into the user project blindly. Lift only the pieces that fit the requested page, and rebuild any local asset that lags behind the official KRDS page you verified.

## Working Rules

### 1. Start from user task structure

Organize menus and sections by user task, not by internal department jargon.

Default public-service groupings:
- introduction or overview
- notices or communication
- application or request
- knowledge or information
- education
- status or dashboard

Public portal shells should also expose trust markers before decorative content:
- skip link to the main content
- explicit current location
- header service identity linked to the main page
- footer with service identity, contact information, utility links, policy links, visually emphasized privacy policy, copyright, and identifier at the end when eligible

Apply these conditions when deciding what trust marker to render:
- official banner only for actual digital government services and only with the current official KRDS snippet
- operating institution identifier only for actual digital government services and only in the footer's last section
- breadcrumb only on interior pages with meaningful hierarchy depth
- footer should follow the current KRDS footer grouping instead of duplicating the header menu
- help panels should follow the current trigger and panel structure when used

### 2. Use restrained visual language

Prefer:
- clear section titles
- compact helper text
- consistent badges and status labels
- simple tables and lists
- familiar board, detail, and application patterns

Avoid:
- decorative gradients as the main identity
- unexplained KPI cards
- repeated subtitles
- multiple competing highlight colors
- marketing copy on transactional screens
- badge fills that reuse the service primary color like CTA buttons

### 3. Separate public and internal concerns

Do not force public-portal patterns onto internal work screens.

Apply KRDS more strongly to:
- landing pages
- notices
- FAQ and Q&A
- applications
- public dashboards
- service overview pages

Apply KRDS tone, but not rigidly identical layouts, to:
- kanban boards
- document management
- operations dashboards
- approval centers
- admin tables

### 4. Standardize statuses and actions

Keep user-facing statuses short and stable.

Preferred examples:
- 대기
- 승인
- 반려
- 완료
- 취소

Action labels should be direct verbs:
- 신청
- 저장
- 수정
- 승인
- 반려
- 다운로드
- 인쇄

### 5. Review accessibility explicitly

Always check:
- official KRDS page date and linked kit version before reusing a local asset
- the asset manifest entry still matches the official page you opened in the same turn
- skip link target lands on the real content start
- heading hierarchy
- color contrast
- focus visibility
- keyboard reachability
- badge text redundancy
- current navigation and breadcrumb state
- semantic step indicator markup on application flows
- help panel or equivalent assistance on complex application forms
- confirm step on irreversible submissions
- complete step after every submission
- when confirm exists, complete screen avoids repeating the full submitted-information summary
- table header clarity
- button hit area
- placeholder lint result before shipping example-derived markup into production

## Output Pattern

When using this skill, structure the answer in this order unless the user asks otherwise.

1. Current assessment
2. KRDS-aligned changes
3. Items that should remain different for internal or admin use
4. Concrete patch plan or code changes

## Source Discipline

If a user references a KRDS page or asks for current KRDS guidance:
- browse the official KRDS site
- cite the official page links
- paraphrase instead of copying long text

## References

- Latest verification workflow: [references/krds-verification.md](references/krds-verification.md)
- Asset verification metadata: [references/asset-verification-manifest.yaml](references/asset-verification-manifest.yaml)
- Baseline summary: [references/krds-principles.md](references/krds-principles.md)
- Decision rules: [references/decision-rules.md](references/decision-rules.md)
- Public website checklist: [references/krds-public-checklist.md](references/krds-public-checklist.md)

## Assets

- Tokens: [assets/krds-tokens.css](assets/krds-tokens.css)
- Components: [assets/krds-components.css](assets/krds-components.css)
- Portal shell: [assets/portal-shell.html](assets/portal-shell.html)
- Breadcrumb: [assets/breadcrumb.html](assets/breadcrumb.html)
- Board list: [assets/board-list.html](assets/board-list.html)
- Board detail: [assets/board-detail.html](assets/board-detail.html)
- Application form: [assets/application-form.html](assets/application-form.html)
- Application confirm: [assets/application-confirm.html](assets/application-confirm.html)
- Application complete: [assets/application-complete.html](assets/application-complete.html)
- Public dashboard: [assets/public-dashboard.html](assets/public-dashboard.html)
- Icons: `assets/icons/*.svg`

## Scripts

- Placeholder lint: `scripts/check_placeholders.py`
