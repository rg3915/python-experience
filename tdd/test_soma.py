# File: test_soma.py
# Comando: py.test


def soma(a, b):
    return a + b


def test_soma():
    assert soma(0, 0) == 0
    assert soma(1, -2) == -1
    assert soma(10, 5) == 15
