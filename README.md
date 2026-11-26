# log-parser

A lightweight command-line utility for summarizing application logs by level.

## Requirements

Python 3. No external dependencies.

## Usage

```bash
python log_summary.py sample.log
```

The input is a plain text log file. Each line should contain a timestamp followed by a log level and an optional message, for example:

```text
2026-11-20 INFO Application started
```

The script counts occurrences of each level and prints the totals in alphabetical order. A sample log is included for testing.

Lines with fewer than two whitespace-separated fields are ignored.
