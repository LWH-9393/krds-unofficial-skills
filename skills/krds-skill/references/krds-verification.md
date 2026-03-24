# KRDS Verification Workflow

Use this file before reusing any bundled KRDS asset.

## 1. Find the exact official KRDS page

- Open the official KRDS page for the component or service pattern you are about to use.
- Prefer the exact pattern page over a general overview page.

Examples:
- official banner
- header
- breadcrumb
- footer
- help panel
- badge
- application form
- confirm step
- completion step

## 2. Check freshness before reuse

On the official KRDS page, read:
- information change history date
- linked HTML Component Kit version

Treat the official KRDS page as newer than the bundled asset unless you have confirmed otherwise in the same turn.

## 3. Decide whether the local asset is safe to use

Reuse the bundled asset only when:
- the official page still matches the bundled structure closely
- no newer KRDS change invalidates the local pattern
- the local asset is being used in the right context

Patch or rebuild the local asset first when:
- the official page has newer change history
- the usage conditions changed
- the bundled asset hard-codes a pattern that should be conditional
- the bundled asset omits a required step such as confirm or completion
- the bundled asset leaves developer placeholder text in visible UI

## 4. Context rules that change whether a pattern should appear

- Official banner:
  Use only for actual digital government services.
  Do not alter the official text or style.
- Operating institution identifier:
  Use only for actual digital government services.
  Place it inside the footer's last section.
- Header:
  Link the service identity to the main page.
- Breadcrumb:
  Do not use on main pages, landing pages, or shallow two-level structures.
  Use the current KRDS breadcrumb label and non-link current item pattern.
  When the path exceeds four links, apply the current KRDS ellipsis pattern.
- Footer:
  Keep the current KRDS grouping and visually distinguish the privacy policy link.
- Help panel:
  Match the current KRDS trigger and panel structure when used.
- Application confirm step:
  Include when the submission cannot be cancelled, withdrawn, or edited later.
- Application completion step:
  Provide after every successful submission.
  If the flow already has a confirm step, the completion screen can omit the detailed submitted-information summary.

## 5. Report with concrete dates when "latest" matters

If the user asks for the latest KRDS guidance, include the official change dates you verified.
