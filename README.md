# LogLens — Python Log Analyzer

A modular command-line tool for analyzing application logs.

## Features

- Parse timestamped log entries
- Count INFO, WARNING, ERROR, DEBUG, and CRITICAL messages
- Detect malformed log lines
- Find the most frequent messages
- Export reports to JSON and CSV
- Automated tests with pytest

## Requirements

- Python 3.10+
- pytest for development and testing

## Installation

```powershell```
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -e ".[dev]"

## Usage

```powershell```
py -m loglens sample.log
py -m loglens sample.log --format json --output report.json
py -m loglens sample.log --format csv --output report.csv


## Run tests

py -m pytest


## Architecture

- parser.py: log parsing and validation
- analyzer.py: statistical aggregation
- exporters.py: JSON and CSV output
- cli.py: command-line interface
- tests/: automated tests


## Limitations

The parser supports a documented timestamped text format.
Additional parsers can be added for JSON and vendor-specific logs.
