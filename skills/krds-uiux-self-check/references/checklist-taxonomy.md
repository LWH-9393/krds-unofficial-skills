# Checklist Taxonomy

Use this file to decide which checklist families and subfamilies apply to the target screens.

## Stage-1 Families

### 1. Style

Use for visual-system consistency checks.

Subfamilies in the source document:
- color
- font
- shape

Typical review focus:
- KRDS palette usage
- interaction-state styling
- background and border consistency
- typography family, size, weight, and hierarchy
- corner radius and clipping behavior

### 2. Component

Use for reusable UI structures and input/action controls.

Subfamilies in the source document:
- official banner
- operating institution identifier
- footer
- header
- skip link
- main menu
- breadcrumb
- side menu
- in-content navigation
- pagination
- link
- button
- radio button
- select
- checkbox
- tag
- date input field
- text area
- text input field
- file upload

Typical review focus:
- structural presence
- position and order consistency
- style fidelity
- labels and affordances
- interaction behavior

### 3. Basic Pattern

Use for task structures that span multiple components.

Subfamilies in the source document:
- personal identification information input
- input form
- attachment
- filtering and sorting

Typical review focus:
- labels and explanation text
- privacy-sensitive input handling
- upload clarity
- retrieval controls and defaults

### 4. Service Pattern

Use for end-to-end public-service journeys.

Subfamilies in the source document:
- visit - visit
- search - overview
- search - search feature discovery
- search - query entry
- search - result review
- search - detailed search
- search - result use
- search - retry
- search - end
- login - find login entry
- login - review or choose login method
- login - enter login information
- login - use service
- application - explore eligible services
- application - review service information
- application - review cautions and eligibility
- application - fill application
- application - confirm and finalize
- application - completion
- application - review result or status
- policy information review - information review

Typical review focus:
- user-task flow continuity
- clarity of next action
- current-state visibility
- alternatives when results are absent
- post-submit or post-login outcome clarity

## Practical Selection Guide

Use these heuristics:
- a shell or repeated structure problem usually maps to `component`
- a typography or color inconsistency usually maps to `style`
- a form-wide issue usually maps to `basic pattern`
- a journey or screen-sequence issue usually maps to `service pattern`

When the target review is broad, start in this order:
1. service pattern
2. component
3. basic pattern
4. style

That order usually surfaces the biggest public-service risks first.
