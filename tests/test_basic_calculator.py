import pytest

from calcservice.basic_calculator import basic_calculator


def _run_basic(monkeypatch, inputs):
    it = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda prompt='': next(it))
    basic_calculator()


def test_basic_simple_expression(monkeypatch, capsys):
    inputs = ['2 + 3', 'exit']
    _run_basic(monkeypatch, inputs)
    out = capsys.readouterr().out
    assert "The result is:" in out
    assert "5" in out


def test_basic_invalid_expression(monkeypatch, capsys):
    inputs = ['2 +', 'exit']
    _run_basic(monkeypatch, inputs)
    out = capsys.readouterr().out
    assert "Invalid input" in out
