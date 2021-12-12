import numpy as np
import pytest

from aoc2021 import day_01 as day


@pytest.fixture
def mock_input():
    depths = """199
200
208
210
200
207
240
269
260
263"""
    return np.array([int(depth) for depth in depths.split()])


def test_solve_part1(mock_input):
    expected = 7
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 5
    result = day.solve_part2(mock_input)
    assert expected == result
