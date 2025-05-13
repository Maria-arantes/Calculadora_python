import pytest
from calculadora import calcular

@pytest.mark.parametrize("a, b, op, esperado", [
    (2, 3, '+', 5),
    (2, 3, '-', -1),
    (2, 3, '*', 6),
    (6, 3, '/', 2),
    (2, 3, '^', 8),
    (-2, -3, '+', -5),
    (5.5, 2.5, '+', 8.0),
    ("a", 2, '+', None),
    (2, "b", '-', None),
    (2, 0, '/', None),
    (3, 3, 'x', None),
    (10, 2, '*', 20),
    (9, 3, '/', 3),
    (2, 4, '^', 16),
    (-3, 3, '^', -27),
    (2, -2, '^', 0.25),
    (1.5, 2.5, '+', 4.0),
    (100, 0, '/', None),
    ("3", "5", '+', 8.0),
    ("5", "xyz", '+', None),
])
def test_calculadora(a, b, op, esperado):
    assert calcular(a, b, op) == esperado
