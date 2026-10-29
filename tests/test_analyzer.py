from loglens.analyzer import analyze_file


def test_analyzer_counts_and_malformed(tmp_path):
    log = tmp_path / "app.log"

    log.write_text(
        "2026-10-29 09:00:00 ERROR DB down\n"
        "2026-10-29 09:00:01 ERROR DB down\n"
        "broken line\n",
        encoding="utf-8",
    )

    result = analyze_file(log)

    assert result["parsed_lines"] == 2
    assert result["malformed_lines"] == 1
    assert result["level_counts"] == {"ERROR": 2}
    assert result["top_messages"][0] == {
        "message": "DB down",
        "count": 2,
    }