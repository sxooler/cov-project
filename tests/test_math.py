from my_package.math import sum, mult


def test_sum():
    assert sum(1, 2) == 3


def test_mult():
    assert mult(2, 3) == 6
