from typing import Any


def format_linter_error(error: dict) -> dict[Any, Any]:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str,
                              errors: list[dict]) -> dict:
    return {"errors": [
        format_linter_error(error) for error in errors
    ],
        "path": file_path,
        "status": "failed" if any(errors) else "passed"
    }


def format_linter_report(linter_report: dict) -> list[dict]:
    return [
        format_single_linter_file(key, value)
        for (key, value) in linter_report.items()
    ]
