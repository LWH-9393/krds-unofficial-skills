# KRDS Unofficial Skills

Unofficial Codex skills for Korean public-sector UI work based on KRDS references.

This bundle separates two concerns:
- `skills/krds-skill`
  - KRDS compliance, structure, trust markers, accessibility, and latest-reference verification
- `skills/krds-public-service-texture`
  - real public-service texture, operational density, ownership cues, notice/detail/filter/contact patterns
- `skills/krds-uiux-self-check`
  - checklist-based self-audit, scope planning, P/F/E/N/A verdicting, and report writing based on the KRDS self-check checklist

## Status

- This repository is unofficial.
- It is not affiliated with KRDS, the Ministry of the Interior and Safety, or NIA.
- Always verify the latest official KRDS guidance before production use.

Official sources:
- https://www.krds.go.kr/
- https://github.com/KRDS-uiux/krds-uiux

## Install

Copy the skill folders under your Codex skills directory:

```text
$CODEX_HOME/skills/krds-skill
$CODEX_HOME/skills/krds-public-service-texture
$CODEX_HOME/skills/krds-uiux-self-check
```

## Usage

- Use `$krds-skill` when the task is about latest KRDS compliance, review, accessibility, trust markers, or public-service structure.
- Use `$krds-public-service-texture` when the screen already follows KRDS but still feels too generic, too clean, or unlike a live public institution service.
- Use `$krds-uiux-self-check` when the task is a structured self-audit, checklist-based review, verdict sheet, or KRDS-style P/F/E/N/A validation.
- Use both when you need compliance first and real-service texture second.
- Use `$krds-uiux-self-check` with `$krds-skill` when you need the `2024.11` self-check framework plus the latest official KRDS page verification.

## Reliability Aids

- `skills/krds-skill/references/asset-verification-manifest.yaml`
  - asset-to-official KRDS page mapping, last verification date, change date, kit version, and use conditions
- `skills/krds-skill/references/decision-rules.md`
  - rule table for banner, identifier, breadcrumb, help panel, confirm, and complete patterns
- `skills/krds-skill/scripts/check_placeholders.py`
  - placeholder lint for `example.org`, zeroed phone numbers, hard-coded sample dates, and dummy receipt numbers
- `skills/krds-public-service-texture/references/asset-derivation-manifest.yaml`
  - texture-asset derivation map back to current official KRDS references
- `skills/krds-public-service-texture/references/texture-activation-rules.md`
  - when to add real-service texture and when not to
- `skills/krds-public-service-texture/references/transformation-examples.md`
  - concrete "generic mockup -> KRDS aligned -> textured public-service screen" examples

## Repository Notes

- Example institution names, addresses, phone numbers, emails, dates, and attachments in the assets are fictional examples for demonstration.
- Do not treat this repository as an official KRDS distribution.
- Do not assume the bundled assets remain current without checking `krds.go.kr`.

## Attribution and License

- Repository-authored skill instructions, example templates, and supporting CSS are released under the MIT License in [LICENSE](LICENSE).
- KRDS references, terminology, and any upstream materials remain subject to their original terms and attribution requirements.
- See [NOTICE.md](NOTICE.md) before publishing derivatives or redistributing adapted materials.
