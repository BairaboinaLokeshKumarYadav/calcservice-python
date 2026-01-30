import re

from calcservice.programmer_calculator import programmer_calculator


def _run_prog(monkeypatch, inputs):
    it = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda prompt='': next(it))
    programmer_calculator()


def _capture_value(text, label):
    m = re.search(rf"{re.escape(label)}\s*:\s*([\w\-]+)", text)
    assert m, f"{label} not found in output"
    return m.group(1)


def test_binary_and_masking(monkeypatch, capsys):
    # 0b1010 & 0b1100 = 0b1000 -> decimal 8
    inputs = ['0b1010 & 0b1100', '8', 'u', 'no', 'exit']
    _run_prog(monkeypatch, inputs)
    out = capsys.readouterr().out
    binary = _capture_value(out, 'binary')
    assert binary.endswith('00001000') or binary.endswith('1000')


def test_hex_addition(monkeypatch, capsys):
    # 0xFF + 1 => 256 with 16 bit size
    inputs = ['0xFF + 1', '16', 'u', 'no', 'exit']
    _run_prog(monkeypatch, inputs)
    out = capsys.readouterr().out
    dec = _capture_value(out, 'decimal')
    assert dec.strip() == '256'


def test_shift_and_signed(monkeypatch, capsys):
    # 255 << 2 = 1020
    inputs = ['255 << 2', '16', 's', 'no', 'exit']
    _run_prog(monkeypatch, inputs)
    out = capsys.readouterr().out
    dec = _capture_value(out, 'decimal')
    assert dec.strip() == '1020'
