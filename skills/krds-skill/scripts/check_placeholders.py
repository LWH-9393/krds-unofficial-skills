#!/usr/bin/env python3
"""Lint implementation files for obvious KRDS example placeholders."""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path


TEXT_EXTENSIONS = {
    ".css",
    ".csv",
    ".html",
    ".htm",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".mjs",
    ".svelte",
    ".ts",
    ".tsx",
    ".txt",
    ".vue",
    ".yaml",
    ".yml",
}

IGNORED_DIRS = {
    ".git",
    ".next",
    ".nuxt",
    ".parcel-cache",
    ".turbo",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "out",
    "vendor",
}


@dataclass(frozen=True)
class Rule:
    severity: str
    name: str
    pattern: re.Pattern[str]
    message: str


RULES = [
    Rule(
        "error",
        "example-domain",
        re.compile(r"\b(?:[a-z0-9._%+-]+@)?example\.(?:org|com)\b", re.IGNORECASE),
        "Replace example.com/example.org placeholder domains or emails.",
    ),
    Rule(
        "error",
        "zero-phone",
        re.compile(r"\b(?:0{2,3}-0{3,4}-0{4}|02-0000-0000|010-0000-0000)\b"),
        "Replace zeroed phone-number placeholders.",
    ),
    Rule(
        "error",
        "example-service-name",
        re.compile(r"예시\s+(?:공공서비스|기관|누리집|포털)"),
        "Replace visible Korean example service naming before shipping.",
    ),
    Rule(
        "error",
        "placeholder-labels",
        re.compile(r"\b(?:DUMMY|PLACEHOLDER|SAMPLE|TEST-[A-Z0-9-]+)\b", re.IGNORECASE),
        "Replace explicit placeholder labels.",
    ),
    Rule(
        "warning",
        "dummy-receipt-number",
        re.compile(
            r"(?:접수번호|신청번호)[\s\S]{0,80}\b[A-Z]{2,10}-20\d{2}-\d{4}-\d{3}\b"
        ),
        "Review hard-coded receipt or application numbers.",
    ),
    Rule(
        "warning",
        "fixed-date-label",
        re.compile(
            r"(?:작성일|등록일|최종 수정일|수정일)[\s\S]{0,40}20\d{2}[-./]\d{2}[-./]\d{2}"
        ),
        "Review hard-coded visible dates before production handoff.",
    ),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Scan implementation files for obvious placeholder strings such as "
            "example.org, zeroed phone numbers, fixed sample dates, and dummy receipt numbers."
        )
    )
    parser.add_argument("paths", nargs="+", help="File or directory paths to scan")
    parser.add_argument(
        "--fail-on",
        choices=("error", "warning", "never"),
        default="error",
        help="Exit non-zero on errors only, warnings too, or never.",
    )
    return parser.parse_args()


def is_probably_text(path: Path) -> bool:
    if path.suffix.lower() in TEXT_EXTENSIONS:
        return True
    try:
        with path.open("rb") as handle:
            chunk = handle.read(1024)
    except OSError:
        return False
    return b"\0" not in chunk


def iter_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path] if is_probably_text(path) else []
    files: list[Path] = []
    for root, dirs, filenames in os.walk(path):
        dirs[:] = [name for name in dirs if name not in IGNORED_DIRS]
        for name in filenames:
            candidate = Path(root) / name
            if is_probably_text(candidate):
                files.append(candidate)
    return files


def collect_findings(path: Path) -> list[tuple[str, Path, int, str, str]]:
    findings: list[tuple[str, Path, int, str, str]] = []
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError as exc:
        findings.append(("warning", path, 0, "read-failed", f"Could not read file: {exc}"))
        return findings

    for rule in RULES:
        for match in rule.pattern.finditer(text):
            line_number = text.count("\n", 0, match.start()) + 1
            findings.append((rule.severity, path, line_number, rule.name, rule.message))
    return findings


def should_fail(findings: list[tuple[str, Path, int, str, str]], mode: str) -> bool:
    if mode == "never":
        return False
    severities = {severity for severity, *_ in findings}
    if mode == "warning":
        return bool(severities)
    return "error" in severities


def main() -> int:
    args = parse_args()
    all_findings: list[tuple[str, Path, int, str, str]] = []
    scanned_files = 0

    for raw_path in args.paths:
        path = Path(raw_path)
        if not path.exists():
            all_findings.append(("warning", path, 0, "missing-path", "Path does not exist."))
            continue
        for file_path in iter_files(path):
            scanned_files += 1
            all_findings.extend(collect_findings(file_path))

    if not all_findings:
        print(f"No placeholder findings in {scanned_files} file(s).")
        return 0

    for severity, path, line_number, name, message in sorted(
        all_findings,
        key=lambda item: (str(item[1]), item[2], item[0], item[3]),
    ):
        location = f"{path}:{line_number}" if line_number else str(path)
        print(f"[{severity.upper()}] {location} {name}: {message}")

    error_count = sum(1 for severity, *_ in all_findings if severity == "error")
    warning_count = sum(1 for severity, *_ in all_findings if severity == "warning")
    print(
        f"Summary: {error_count} error(s), {warning_count} warning(s), "
        f"{scanned_files} file(s) scanned."
    )

    return 1 if should_fail(all_findings, args.fail_on) else 0


if __name__ == "__main__":
    sys.exit(main())
