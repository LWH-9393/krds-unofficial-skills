# Review Workflow

## 1. Prepare The Audit

Define:
- site or service name
- audit period
- reviewer
- target environment
- scope type: full or sampled
- screen list

When a whole-service audit is too large, use representative sampling.
The source document recommends selecting at least 10 target screens when sampling across a service.

Good sampling priorities from the source document:
- screens with high usage
- screens where users report difficulty
- screens tied to public-service policy goals
- screens that include repeated structures used across the service

## 2. Fix The Review Environment

Baseline environment from the source document:
- operating system: Windows 10 or later required, macOS Monterey or later recommended
- resolution: 1920x1080
- browser: latest Chrome
- zoom: 100%
- extensions/plugins: none installed
- browser state: cache and cookies cleared
- input devices: keyboard and mouse both tested

Keyboard checks should include:
- text input
- shortcut behavior when relevant
- `Tab` traversal
- `Enter` and `Space` activation

Mouse checks should include:
- click
- double-click where relevant
- scroll

## 3. Confirm The Right Checklist Applies

Before judging an item:
- confirm the target screen or element is actually in scope
- check whether the item is an exception
- check whether the source notes the case as `해당 없음`

Do not review an item that the target screen does not meaningfully contain.

## 4. Run The Checklist Procedures In Order

For each checklist item:
- follow the listed review procedure in numeric order
- do not skip intermediate checks
- if the checklist says "다음 중 1개의 방법으로", one qualifying method is enough
- if the checklist says "다음을 모두 수행하여" or "다음 모든 상황에서", all listed conditions must hold

Where the source checklist points to tool usage, use browser developer tools and visual inspection accordingly.

## 5. Decide The Verdict

Use [verdict-rules.md](verdict-rules.md) for `P`, `F`, `E`, `N/A`.

Always judge against the compliance criteria, not against example failures alone.

## 6. Write The Result Sheet

The source document expects a structured result sheet that includes:
- audit overview
- audit environment
- audit scope
- detailed checklist results

Use [assets/self-check-report-template.md](../assets/self-check-report-template.md) as the repository-ready starting structure.

## 7. Turn The Audit Into Improvement Work

After the verdicts:
- identify high-priority failures
- link each failure to the affected screens
- propose a concrete improvement path
- repeat the audit after fixes

This skill should help the user move from audit to action, not stop at a checklist mark.
