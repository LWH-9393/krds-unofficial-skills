#!/usr/bin/env python3
"""Check or refresh the tracked KRDS UIUX upstream release metadata."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


UPSTREAM_RELEASE_API = "https://api.github.com/repos/KRDS-uiux/krds-uiux/releases/latest"
DEFAULT_MANIFEST = Path("skills/krds-skill/references/asset-verification-manifest.yaml")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Compare the latest KRDS-uiux release on GitHub with the version "
            "recorded in the local asset verification manifest."
        )
    )
    parser.add_argument(
        "--manifest",
        default=str(DEFAULT_MANIFEST),
        help="Path to the asset-verification manifest to inspect or update.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write the latest upstream version/date/url into the manifest.",
    )
    return parser.parse_args()


def fetch_latest_release() -> tuple[str, str, str]:
    try:
        result = subprocess.run(
            [
                "gh",
                "api",
                "repos/KRDS-uiux/krds-uiux/releases/latest",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)
    except (FileNotFoundError, subprocess.CalledProcessError, json.JSONDecodeError):
        request = Request(
            UPSTREAM_RELEASE_API,
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "krds-unofficial-skills-upstream-check",
            },
        )
        with urlopen(request, timeout=15) as response:
            payload = json.load(response)

    tag_name = payload["tag_name"]
    version = tag_name if tag_name.startswith("v") else f"v{tag_name}"
    released_on = payload["published_at"][:10]
    url = payload["html_url"]
    return version, released_on, url


def read_manifest(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_manifest_values(text: str) -> tuple[str, str, str]:
    block_match = re.search(
        r"html_component_kit_latest:\n(?P<block>(?:\s{4}.+\n){3})",
        text,
    )
    if not block_match:
        raise ValueError("Could not find html_component_kit_latest block in manifest.")

    block = block_match.group("block")
    version_match = re.search(r"^\s{4}version:\s*(.+)$", block, re.MULTILINE)
    released_match = re.search(r"^\s{4}released_on:\s*(.+)$", block, re.MULTILINE)
    url_match = re.search(r"^\s{4}url:\s*(.+)$", block, re.MULTILINE)

    if not (version_match and released_match and url_match):
        raise ValueError("Manifest release block is missing one or more required fields.")

    return (
        version_match.group(1).strip(),
        released_match.group(1).strip(),
        url_match.group(1).strip(),
    )


def normalize_version(value: str) -> tuple[int, ...]:
    cleaned = value.strip().lstrip("vV")
    return tuple(int(part) for part in cleaned.split("."))


def update_manifest(
    text: str,
    version: str,
    released_on: str,
    url: str,
) -> str:
    text = re.sub(
        r"(^\s{4}version:\s*).+$",
        rf"\g<1>{version}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"(^\s{4}released_on:\s*).+$",
        rf"\g<1>{released_on}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"(^\s{4}url:\s*).+$",
        rf"\g<1>{url}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    return text


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest)
    if not manifest_path.exists():
        print(f"Manifest not found: {manifest_path}", file=sys.stderr)
        return 2

    try:
        latest_version, latest_date, latest_url = fetch_latest_release()
    except (HTTPError, URLError, TimeoutError) as exc:
        print(f"Failed to fetch latest upstream release: {exc}", file=sys.stderr)
        return 2

    manifest_text = read_manifest(manifest_path)
    current_version, current_date, current_url = parse_manifest_values(manifest_text)

    print(f"Manifest version: {current_version} ({current_date})")
    print(f"Upstream version: {latest_version} ({latest_date})")

    is_outdated = (
        normalize_version(current_version) < normalize_version(latest_version)
        or current_date != latest_date
        or current_url != latest_url
    )

    if args.write:
        new_text = update_manifest(manifest_text, latest_version, latest_date, latest_url)
        if new_text != manifest_text:
            manifest_path.write_text(new_text, encoding="utf-8")
            print(f"Updated manifest: {manifest_path}")
        else:
            print("Manifest already matched upstream release metadata.")
        return 0

    if is_outdated:
        print("Upstream release metadata is newer than the local manifest.")
        print("Run: python3 scripts/check_krds_upstream.py --write")
        return 1

    print("Manifest release metadata matches upstream.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
