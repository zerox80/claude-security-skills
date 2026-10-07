#!/usr/bin/env python3
"""Read-only schema validation for a supplied patch-risk JSON artifact.

Added in the Claude adaptation of openai/codex-security, 2026-10-07.
Requires the already installed jsonschema package. Makes no network requests.
"""
import json
import sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: validate_assessment.py <assessment.json|->", file=sys.stderr)
        return 2
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        print("Full schema validation unavailable: jsonschema is not installed.", file=sys.stderr)
        return 2
    try:
        value = json.load(sys.stdin) if sys.argv[1] == "-" else json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        schema = json.loads((Path(__file__).resolve().parent.parent / "references/patch-risk-assessment.schema.json").read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(Draft202012Validator(schema).iter_errors(value), key=lambda e: list(map(str, e.absolute_path)))
        if errors:
            for err in errors:
                print("/" + "/".join(map(str, err.absolute_path)) + ": " + err.message, file=sys.stderr)
            return 1
        print("Patch-risk assessment matches the bundled JSON schema. Factual correctness was not tested.")
        return 0
    except (OSError, ValueError) as err:
        print(type(err).__name__ + ": " + str(err), file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
