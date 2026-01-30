import pytest

from calcservice.scientific_calculator import scientific_calculator


def _run_sci(monkeypatch, inputs):
    it = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda prompt='': next(it))
    scientific_calculator()


def test_sin_function(monkeypatch, capsys):
    inputs = ['sin(pi/2)', 'exit']
    _run_sci(monkeypatch, inputs)
    out = capsys.readouterr().out
    assert "The result is:" in out
    assert "1.0" in out


def test_sqrt_and_invalid(monkeypatch, capsys):
    inputs = ['sqrt(16)', 'invalid_func()', 'exit']
    _run_sci(monkeypatch, inputs)
    out = capsys.readouterr().out
    assert "The result is:" in out
    assert "4.0" in out
    assert "Invalid input" in out
