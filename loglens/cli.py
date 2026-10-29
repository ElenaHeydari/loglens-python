import argparse
from pathlib import Path

from .analyzer import analyze_file
from .exporters import export_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analyze timestamped application log files."
    )

    parser.add_argument("file", help="Path to a log file")
    parser.add_argument(
        "--format",
        choices=("text", "json", "csv"),
        default="text",
    )
    parser.add_argument(
        "--output",
        help="Output path for JSON or CSV reports",
    )

    return parser


def main() -> int:
    args = build_parser().parse_args()
    path = Path(args.file)

    if not path.is_file():
        print(f"Error: file not found: {path}")
        return 2

    try:
        report = analyze_file(path)
    except OSError as exc:
        print(f"Error reading file: {exc}")
        return 2

    if args.format == "text":
        print(f"\nLogLens report: {report['source']}")
        print(
            f"Parsed lines: {report['parsed_lines']} "
            f"/ {report['total_lines']}"
        )
        print(f"Malformed lines: {report['malformed_lines']}")

        print("\nSeverity counts:")
        for level, count in report["level_counts"].items():
            print(f"  {level}: {count}")

        print("\nMost frequent messages:")
        for item in report["top_messages"]:
            print(f"  {item['count']}x {item['message']}")

        return 0

    output = args.output or f"report.{args.format}"

    try:
        export_report(report, output, args.format)
    except (OSError, ValueError) as exc:
        print(f"Error exporting report: {exc}")
        return 2

    print(f"Report written to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())