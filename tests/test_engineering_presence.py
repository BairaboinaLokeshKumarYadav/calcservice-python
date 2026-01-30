import importlib


def test_engineering_module_importable():
    m = importlib.import_module('calcservice.engineering_calculator')
    assert m is not None
