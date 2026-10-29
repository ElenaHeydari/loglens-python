from collections import Counter
from pathlib import Path

from .parser import LogEntry, parse_line


def analyze_file(path: str | Path) -> dict:
    entries: list[LogEntry] = []
    malformed = 0

    with Path(path).open(
        "r",
        encoding="utf-8",
        errors="replace",
    ) as handle:
        for line in handle:
            if not line.strip():
                continue

            entry = parse_line(line)

            if entry is None:
                malformed += 1
            else:
                entries.append(entry)

    levels = Counter(entry.level for entry in entries)
    messages = Counter(entry.message for entry in entries)

    timestamps = [entry.timestamp for entry in entries]

    return {
        "source": Path(path).name,
        "total_lines": len(entries) + malformed,
        "parsed_lines": len(entries),
        "malformed_lines": malformed,
        "level_counts": dict(sorted(levels.items())),
        "top_messages": [
            {"message": message, "count": count}
            for message, count in messages.most_common(5)
        ],
        "first_timestamp": (
            min(timestamps).isoformat(sep=" ")
            if timestamps else None
        ),
        "last_timestamp": (
            max(timestamps).isoformat(sep=" ")
            if timestamps else None
        ),
    }