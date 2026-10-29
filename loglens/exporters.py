import csv
import json


def export_report(report: dict, output_path: str, output_format: str) -> None:
    if output_format == "json":
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(report, file, indent=2, ensure_ascii=False)

    elif output_format == "csv":
        with open(output_path, "w", encoding="utf-8-sig", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["Metric", "Value"])
            writer.writerow(["Source", report["source"]])
            writer.writerow(["Total Lines", report["total_lines"]])
            writer.writerow(["Parsed Lines", report["parsed_lines"]])
            writer.writerow(["Malformed Lines", report["malformed_lines"]])

            writer.writerow([])
            writer.writerow(["Log Level", "Count"])

            for level, count in report["level_counts"].items():
                writer.writerow([level, count])

            writer.writerow([])
            writer.writerow(["Message", "Count"])

            for message, count in report["top_messages"]:
                writer.writerow([message, count])