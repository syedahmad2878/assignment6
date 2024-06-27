# calc_app/tests/test_add_command.py
from calc_app.plugins.greet.greet_command import greetCommand
import pytest

@pytest.fixture
def command():
    return greetCommand()

def test_execute_addition(monkeypatch, command):
    #inputs = iter(['2', '3'])

    def mock_input(prompt):
        return next(inputs)

    results = []

    def mock_print(x):
        results.append(x)

    monkeypatch.setattr('builtins.input', mock_input)
    monkeypatch.setattr('builtins.print', mock_print)  # Capture print output during test

    command.execute()

    assert results == ['Hello World!']  # Adjust expected output to match actual output
