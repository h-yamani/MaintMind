import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

MANIFEST_DIR = Path("data/manifests")
SCHEMA_PATH = MANIFEST_DIR / "manifest.schema.json"
REGISTRY_PATH = Path("data/registry/sources.json")


def load_json(path: Path) -> dict:
    """Load a JSON document."""
    return json.loads(path.read_text(encoding="utf-8"))


def test_manifest_schema_is_valid() -> None:
    """Ensure the ingestion-manifest schema is valid."""
    Draft202012Validator.check_schema(load_json(SCHEMA_PATH))


def test_dataset_manifests_are_valid_and_registered() -> None:
    """Validate every dataset manifest and its registered source IDs."""
    schema = load_json(SCHEMA_PATH)
    registry = load_json(REGISTRY_PATH)
    registered_source_ids = {source["source_id"] for source in registry["sources"]}

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )

    manifest_paths = sorted(
        path for path in MANIFEST_DIR.glob("*.json") if path.name != SCHEMA_PATH.name
    )

    assert manifest_paths, "No dataset manifests were found."

    for manifest_path in manifest_paths:
        manifest = load_json(manifest_path)
        errors = sorted(
            validator.iter_errors(manifest),
            key=lambda error: list(error.path),
        )

        assert not errors, "\n".join(
            f"{manifest_path}: {error.message}" for error in errors
        )

        for file_record in manifest["files"]:
            assert file_record["source_id"] in registered_source_ids
            assert file_record["raw_file_committed_to_git"] is False
