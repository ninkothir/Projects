import pytest
from HW_1.simple_math import SimpleMath


@pytest.fixture
def math():
    return SimpleMath()


def test_square(math):
    assert math.square(2) == 4
    assert math.square(-3) == 9
    assert math.square(0) == 0


def test_cube(math):
    assert math.cube(2) == 8
    assert math.cube(-3) == -27
    assert math.cube(0) == 0