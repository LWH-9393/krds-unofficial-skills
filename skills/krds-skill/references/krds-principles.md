# KRDS Principles Summary

Official references:
- KRDS outline: https://www.krds.go.kr/html/site/outline/outline_05.html
- Design principles: https://www.krds.go.kr/html/site/designSystem/contents/ux/ux_01.html
- Writing principles: https://www.krds.go.kr/html/site/designSystem/contents/ux/ux_02.html
- Foundation layout: https://www.krds.go.kr/html/site/designSystem/contents/foundation/foundation_03.html
- Pattern index: https://www.krds.go.kr/html/site/designSystem/contents/pattern/pattern_01.html
- Service pattern index: https://www.krds.go.kr/html/site/designSystem/contents/service/service_01.html

## Latest-first workflow

- Open the relevant official KRDS page before touching local assets.
- Read the page's information change history and linked HTML Component Kit version.
- If the official page changed after the bundled asset was created, patch or rebuild the local asset before reuse.

## What matters most for implementation

### 1. Trust before novelty
Public-sector interfaces should feel stable, explicit, and predictable.

Implement as:
- skip link to the main content
- official-service banner only on actual digital government services
- operating institution identifier only on actual digital government services and inside the footer
- header service identity linked to the main page
- clear institutional identity
- explicit page titles
- obvious current location
- breadcrumb where the service depth needs it
- footer with service identity, contact information, utility links, policy links, visually emphasized privacy policy, copyright, and identifier at the end when eligible
- restrained visual accents
- familiar board and form patterns

### 2. User task first
KRDS emphasizes service use over internal organization.

Implement as:
- menus named by what users do
- top tasks exposed on the first screen
- simple paths to notices, applications, status, and help

### 3. Plain language
Use short, direct Korean labels.

Implement as:
- short headings
- helper text only when needed
- consistent terms for states and actions
- no repeated subtitle strings

### 4. Consistent structure
Public services should reuse predictable structures.

Implement as:
- list -> detail -> apply -> confirm -> complete -> status flows
- reusable section headers
- aligned tables and metadata rows
- unified badges and filters
- footer grouped by service identity, contact, utility, policy, copyright, and identifier
- confirmation and completion steps for application flows when needed

Notes:
- Do not modify the official banner text or style.
- Do not use breadcrumb on main pages, landing pages, or shallow two-level structures.
- Do not ship a breadcrumb with the wrong KRDS label or without the current ellipsis branch.
- Do not place the identifier near the header.
- Do not leave instructional placeholder text visible in the identifier slot.
- Do not style badges like primary action buttons.
- Help panels should match the current trigger and panel structure when used.
- When a confirm step exists, the complete screen can omit the detailed submitted-information summary.

### 5. Accessibility as default
KRDS assumes accessible interaction, not optional accessibility.

Implement as:
- sufficient contrast
- visible keyboard focus on links, buttons, and fields
- visible focus
- semantic heading order
- step indicators with list semantics and current-step state
- button labels that describe action
- text labels on status badges

## Practical interpretation for mixed systems

### Public portal
Apply KRDS strongly.

### Internal work portal
Keep KRDS tone and clarity, but optimize for information density and speed.

### Admin
Use KRDS vocabulary discipline and accessibility rules, but keep admin workflows compact.
