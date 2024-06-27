

from calc_app.plugins.env.read_enviornment import readEnviornment
from unittest.mock import patch, mock_open
import pytest
@pytest.fixture
def mock_env_file(monkeypatch):
    # Mock the content of .env file
    env_content = "DEBUG=True\nSECRET_KEY=mysecret\n"
    monkeypatch.setattr('builtins.open', mock_open(read_data=env_content))

def test_read_environment_valid_key(monkeypatch, capsys, mock_env_file):
    # Mock user input for the key 'DEBUG'
    inputs = iter(['DEBUG'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create an instance of readEnviornment and execute
    cmd = readEnviornment()
    cmd.execute()

    # Capture the output and check
    captured = capsys.readouterr()
    assert "True" in captured.out

def test_read_environment_invalid_key(monkeypatch, capsys, mock_env_file):
    # Mock user input for an invalid key 'INVALID_KEY'
    inputs = iter(['INVALID_KEY'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create an instance of readEnviornment and execute
    cmd = readEnviornment()
    cmd.execute()

    # Capture the output and check
    captured = capsys.readouterr()
    assert "Key 'INVALID_KEY' not found." in captured.out
