from loglens.parser import parse_line


def test_parse_valid_line():
    entry = parse_line("2026-10-29 09:00:00 ERROR Disk full")

    assert entry is not None
    assert entry.level == "ERROR"
    assert entry.message == "Disk full"


def test_reject_malformed_line():
    assert parse_line("not a log") is None


def test_reject_invalid_date():
    assert parse_line("2026-99-99 09:00:00 INFO Nope") is None