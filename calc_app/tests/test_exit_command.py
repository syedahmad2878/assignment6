# calc_app/tests/test_exit_command.py
from calc_app.plugins.exit.exit_command import exitCommand
import pytest
import sys

@pytest.fixture
def command():
    return exitCommand()

def test_execute_exit(monkeypatch, command):
    results = []

    def mock_print(x):
        results.append(x)

    monkeypatch.setattr('builtins.print', mock_print)  # Capture print output during test

    with pytest.raises(SystemExit) as e:
        command.execute()

    assert e.value.code == 0  # Check if the exit code is as expected
    assert results == ['Goodbye']  # Check if the output is as expected
