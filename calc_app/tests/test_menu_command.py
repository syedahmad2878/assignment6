# tests/test_menu_command.py
from calc_app.plugins.menu.menu_command import menuCommand
from unittest.mock import patch
import io
import pytest

@pytest.fixture
def menu_command():
    return menuCommand()

def test_execute(menu_command):
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        menu_command.execute()
        expected_output = "greet\ngoodbye\nadd\nsubtract\nmultiply\ndivide\nexit\n"
        assert mock_stdout.getvalue() == expected_output
