---
name: krds-public-service-texture
description: Add real-service texture and operational density to a KRDS-aligned Korean public-sector website, portal, notice board, application flow, or public dashboard. Use when Codex needs a public institution UI to feel like a live operating service rather than a clean compliance mockup, including requests for realistic public-site tone, institutional identity, dense notice/detail/search patterns, attachments, contact boxes, or an actual government-service look and feel.
---

# KRDS Public Service Texture

Use this skill after or alongside [$krds-skill](../krds-skill/SKILL.md).

`krds-skill` protects official KRDS structure, accessibility, and trust markers.
This skill adds the parts that make a screen feel like a real public service in operation:
- institutional tone
- operational metadata
- realistic content density
- service-entry and support blocks
- notice, attachment, and contact patterns

## Quick Start

1. Decide whether the request is about compliance, texture, or both.
   - If official KRDS compliance is still unsettled, use [$krds-skill](../krds-skill/SKILL.md) first.
   - If the user says the screen feels too generic, too clean, too demo-like, or unlike a real public institution site, use this skill.
2. Identify the page archetype.
   - Home or service overview
   - Notice or board list
   - Detail page
   - Application input
   - Confirm, complete, or status
   - Public dashboard or integrated search
3. Read the right reference files.
   - Start with [references/texture-principles.md](references/texture-principles.md)
   - Use [references/page-archetypes.md](references/page-archetypes.md) for block recipes
   - Use [references/copy-patterns.md](references/copy-patterns.md) when the screen sounds too generic
   - Use [references/realism-checklist.md](references/realism-checklist.md) when reviewing
4. Reuse only the texture assets that match the page.
   - Load [assets/public-service-texture.css](assets/public-service-texture.css) after the base KRDS tokens and components
   - Lift only the partials that add believable public-service density
5. Preserve official KRDS conditions.
   - Do not invent banner or identifier usage
   - Do not break breadcrumb, footer, help-panel, or step-flow rules already enforced by [$krds-skill](../krds-skill/SKILL.md)

## What This Skill Changes

This skill should change the screen in these ways:
- turn generic headings into institution-specific service titles
- replace perfect demo-card layouts with mixed service-entry, notice, support, and metadata blocks
- add ownership, update date, attachment, contact, and next-step context
- increase information density without making the page visually noisy
- make lists, detail pages, and forms feel operational instead of promotional

This skill should not:
- replace official KRDS verification
- add decorative marketing visuals
- force public-site texture onto internal admin screens
- duplicate the sibling skill's compliance rules

## Texture Rules

### 1. Favor operational density over showcase polish

Prefer:
- short utility headings
- mixed block sizes
- visible counts, dates, status, and owner information
- more than one supporting block around the main task
- realistic empty-state, deadline, and contact wording

Avoid:
- four equal cards with equal copy length
- oversized hero sections on transactional screens
- startup-style value propositions
- abstract KPI tiles without source or explanation
- perfectly symmetrical layouts everywhere

### 2. Make institutional ownership obvious

Real public-service screens usually reveal who owns the service.

Add where appropriate:
- operating department or center
- contact number or email
- update date
- responsible team label
- related policy or FAQ link

If ownership is invisible, the screen will still feel like a concept mockup.

### 3. Use realistic public-service content blocks

Public-service texture usually comes from repeated practical blocks:
- notice summaries
- attachment download lists
- search and filter bars
- contact and owner boxes
- requirement summaries
- process or schedule notes
- related services and FAQ links

Do not rely on quick links alone.

### 4. Use procedural copy, not brand copy

Microcopy should sound administrative and useful:
- what the user can do
- what they need before starting
- what happens next
- when the information was updated
- where to ask for help

Do not write vague promotional lines when a task-oriented sentence will do.

### 5. Keep believable asymmetry

A real service page is rarely a single repeated component grid.

Use combinations like:
- main service area + notice panel + support box
- board list + filter toolbar + total count + sort or category controls
- detail body + attachment section + owner box + related links
- application form + requirements summary + help panel + contact path

## Page Use Guide

### Home or service overview

Use:
- service-entry area
- latest notices or schedules
- support or contact box
- short institutional intro only when it helps service entry

### Notice or board list

Use:
- filter toolbar
- total count
- category, date, or view metadata
- pinned or badge-treated important items

### Detail page

Use:
- clear metadata row
- attachment list
- owner or contact box
- related links or return path

### Application input

Use:
- requirement summary before the form
- help, FAQ, or contact path near the form
- realistic helper text
- next-step clarity before submission

### Confirm, complete, or status

Use:
- receipt or application number
- next-step summary
- processing expectations
- links to list, status, or contact path

### Public dashboard or integrated search

Use:
- source or update stamp
- explanatory labels
- safe-for-disclosure metrics only
- surrounding notice, definition, or caveat text

## Working With Assets

Use these assets only as partials, not as entire page solutions:
- [assets/public-service-texture.css](assets/public-service-texture.css)
- [assets/home-service-layout.html](assets/home-service-layout.html)
- [assets/search-filter-toolbar.html](assets/search-filter-toolbar.html)
- [assets/notice-list-panel.html](assets/notice-list-panel.html)
- [assets/attachment-list.html](assets/attachment-list.html)
- [assets/contact-owner-box.html](assets/contact-owner-box.html)

Lift only the pieces the target page needs.

## Output Pattern

When using this skill, structure the answer in this order unless the user asks otherwise.

1. Current texture gap
2. Real-service texture changes
3. What must remain governed by KRDS compliance
4. Concrete patch plan or asset lift

## References

- Texture principles: [references/texture-principles.md](references/texture-principles.md)
- Page archetypes: [references/page-archetypes.md](references/page-archetypes.md)
- Copy patterns: [references/copy-patterns.md](references/copy-patterns.md)
- Realism checklist: [references/realism-checklist.md](references/realism-checklist.md)
