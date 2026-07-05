"""Shared pytest configuration for Lab 03.

Keeps the CI output clean: students see only whether every test passed, or a
short "expected X but got Y" line per failure, never a Python stack trace.
"""

import pytest


def pytest_configure(config):
    # Silence tracebacks and the noisy default reporting.
    config.option.tbstyle = "no"
    config.option.verbose = -1
    # Drop pytest's own "short test summary info" (the FAILED ... list),
    # so students only see our tidy result block below.
    config.option.reportchars = ""


# Collect the clean, one-line reason for each failing test.
_failures = []


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.failed and report.when == "call":
        message = report.longrepr.reprcrash.message if report.longrepr else "test failed"
        clean = message.strip().splitlines()[0]
        for prefix in ("AssertionError:", "Failed:"):
            if clean.startswith(prefix):
                clean = clean[len(prefix):].strip()
        _failures.append(clean)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    # Replace pytest's default summary with our own tidy result block.
    terminalreporter.line("")
    if _failures:
        terminalreporter.line("SOME TESTS FAILED:")
        for line in _failures:
            terminalreporter.line(f"  - {line}")
    else:
        terminalreporter.line("ALL TESTS PASSED")
