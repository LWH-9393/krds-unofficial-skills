# KRDS Public Website Checklist

Use this checklist when building or reviewing a Korean public institution homepage or service page.

## Latest KRDS Check
- Did you open the relevant current KRDS page before reusing a bundled asset?
- Did you note the information change history date and linked HTML Component Kit version?
- If the KRDS page changed later than the local asset, did you patch the local asset first?

## Common Shell
- Is there a skip link that lands on the true main content start?
- Does the header service identity link to the main page?
- If this is an actual digital government service, is the official banner inserted with the current KRDS text and style unchanged?
- If this is an actual digital government service, is the operating institution identifier placed in the footer's last section?
- Does the footer expose service identity, contact information, utility links, policy links, a visually emphasized privacy policy, and copyright?
- Is any identifier slot free of instructional placeholder text when the official identifier is not inserted?
- Is breadcrumb omitted on main/landing pages and shallow two-level structures, and included only when the page depth requires it?
- If breadcrumb is used, does it use the current KRDS label, a non-link current item, and the current ellipsis handling when depth exceeds four links?

## Information Architecture
- Is the menu grouped by user tasks?
- Does the page title match the selected navigation state?
- Can users reach the main service in one or two clicks?
- Are public and internal functions separated?

## Home Page
- Are quick links tied to actual services?
- Are notice and schedule blocks using real data?
- Is the first screen structured around service entry, not decoration?
- Is the institutional identity visible immediately?

## Board and Detail Pages
- Does the list use a familiar board layout?
- Does the detail page show title, meta, content, attachments, and return path?
- Are comments, answers, and admin actions visually subordinate to the main content?
- Are duplicated subtitles removed?

## Application and Status Pages
- Is the flow clear: guide, input, confirm, complete, status?
- When a help panel is used, does it follow the current KRDS trigger and panel structure?
- If a help panel is not used, does the form still provide contextual help, FAQ links, or a contact path?
- Does the step indicator use ordered list semantics and mark the current step?
- If submission cannot be cancelled or edited later, is there a confirm step before final submission?
- Is there a complete screen after submission with result links or next actions?
- When a confirm step already summarized the input, does the complete screen avoid repeating the whole submitted-information summary?
- Are required fields obvious?
- Are statuses short and user-facing?
- Can users understand what happens next after submission?

## Dashboard and Statistics
- Is the public dashboard limited to information safe for disclosure?
- Are internal or operational indicators hidden from public users?
- Are card styles consistent with the rest of the service?
- Are charts explanatory rather than decorative?

## Accessibility and Tone
- Is text contrast sufficient?
- Are badges understandable without color?
- Do badge colors avoid looking like primary CTA buttons?
- Is helper text concise?
- Does the page feel institutional rather than promotional?
