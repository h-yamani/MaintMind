#!/usr/bin/env python3
"""Download or verify MaintMind real datasets and write provenance manifests."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REAL_DATA_DIR = ROOT / "data" / "real"
MANIFEST_DIR = ROOT / "data" / "manifests"

SOURCES = {
    "nestor": {
        "dataset_group": "nist_nestor",
        "manifest": "nestor_v1.json",
        "allowed_join": None,
        "files": [
            {
                "source_id": "nist_nestor_excavators",
                "filename": "excavator_work_orders.csv",
                "directory": "nestor/raw",
                "source_version": "2015_raw",
                "source_url": (
                    "https://prognosticsdl.systemhealthlab.com/dataset/"
                    "f4780ee0-efa6-45b6-b6dc-cfc60bfb5687/resource/"
                    "7c2b0da9-8a8a-4d3a-8102-5d02ea5ba57a/download/"
                    "excavator_2015_raw_forpdl.csv"
                ),
            }
        ],
    },
    "nyc_amps": {
        "dataset_group": "nyc_amps",
        "manifest": "nyc_amps_v1.json",
        "allowed_join": "work_orders.EVT_OBJECT = assets.OBJ_CODE",
        "files": [
            {
                "source_id": "nyc_amps_work_orders",
                "filename": "work_orders.csv",
                "directory": "nyc_amps/raw",
                "source_version": "8sdw-8vja",
                "source_url": (
                    "https://data.cityofnewyork.us/api/v3/views/"
                    "8sdw-8vja/export.csv?accessType=DOWNLOAD"
                ),
            },
            {
                "source_id": "nyc_amps_assets",
                "filename": "assets.csv",
                "directory": "nyc_amps/raw",
                "source_version": "e25p-jzfy",
                "source_url": (
                    "https://data.cityofnewyork.us/api/views/"
                    "e25p-jzfy/rows.csv?accessType=DOWNLOAD"
                ),
            },
        ],
    },
}


def sha256(path: Path) -> str:
    """Return the SHA-256 checksum for a file."""
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for block in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def download(url: str, destination: Path, overwrite: bool) -> bool:
    """Download a file atomically and return whether a download occurred."""
    destination.parent.mkdir(parents=True, exist_ok=True)

    if destination.exists() and not overwrite:
        print(f"Using existing file: {destination}")
        return False

    partial = destination.with_suffix(destination.suffix + ".part")
    partial.unlink(missing_ok=True)
    request = Request(url, headers={"User-Agent": "MaintMind/1.0"})

    print(f"Downloading {url}")
    try:
        with urlopen(request, timeout=120) as response, partial.open("wb") as output:
            while block := response.read(1024 * 1024):
                output.write(block)
        os.replace(partial, destination)
    except Exception:
        partial.unlink(missing_ok=True)
        raise

    print(f"Downloaded: {destination}")
    return True


def existing_records(manifest_path: Path) -> dict[str, dict]:
    """Return existing manifest records keyed by source ID."""
    if not manifest_path.exists():
        return {}

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    return {record["source_id"]: record for record in manifest.get("files", [])}


def process_source(name: str, overwrite: bool, verify_only: bool) -> None:
    """Download or verify one source group and write its manifest."""
    config = SOURCES[name]
    manifest_path = MANIFEST_DIR / config["manifest"]
    previous = existing_records(manifest_path)
    records = []

    for item in config["files"]:
        path = REAL_DATA_DIR / item["directory"] / item["filename"]

        if verify_only:
            if not path.exists():
                raise FileNotFoundError(f"Missing file: {path}")
            downloaded = False
        else:
            downloaded = download(item["source_url"], path, overwrite)

        old_record = previous.get(item["source_id"], {})
        retrieved_at = old_record.get("retrieved_at")
        if downloaded or not retrieved_at:
            retrieved_at = datetime.now(timezone.utc).isoformat()

        records.append(
            {
                "source_id": item["source_id"],
                "original_filename": item["filename"],
                "local_path": str(path.relative_to(ROOT)),
                "source_url": item["source_url"],
                "source_version": item["source_version"],
                "retrieved_at": retrieved_at,
                "file_size_bytes": path.stat().st_size,
                "sha256": sha256(path),
                "raw_file_committed_to_git": False,
            }
        )

        print(
            f"Verified {path.name}: {path.stat().st_size:,} bytes; "
            f"SHA-256 {records[-1]['sha256']}"
        )

    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {
        "schema_version": "1.0",
        "dataset_group": config["dataset_group"],
        "allowed_join": config["allowed_join"],
        "files": records,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Manifest written: {manifest_path}")


def main() -> None:
    """Run the requested acquisition or verification."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, choices=[*SOURCES, "all"])
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--verify-only", action="store_true")
    arguments = parser.parse_args()

    selected = list(SOURCES) if arguments.source == "all" else [arguments.source]
    for source in selected:
        process_source(source, arguments.overwrite, arguments.verify_only)


if __name__ == "__main__":
    main()
