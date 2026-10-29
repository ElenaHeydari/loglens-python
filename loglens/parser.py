from dataclasses import dataclass
from datetime import datetime
import re


LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL) "
    r"(?P<message>.+)$"
)


@dataclass(frozen=True)
class LogEntry:
    timestamp: datetime
    level: str
    message: str


def parse_line(line: str) -> LogEntry | None:
    match = LOG_PATTERN.match(line.strip())

    if not match:
        return None

    try:
        timestamp = datetime.strptime(
            match.group("timestamp"),
            "%Y-%m-%d %H:%M:%S",
        )
    except ValueError:
        return None

    return LogEntry(
        timestamp=timestamp,
        level=match.group("level"),
        message=match.group("message").strip(),
    )