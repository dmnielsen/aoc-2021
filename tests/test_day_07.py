import numpy as np
import pytest

from aoc2021 import day_07 as day


@pytest.fixture
def mock_input():
    return "16,1,2,0,4,2,7,1,2,14"


def test_parse_input(mock_input):
    expected = np.array([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
    result = day.parse_input(mock_input)
    np.testing.assert_array_equal(result, expected)


@pytest.mark.parametrize('n, expected', [(1, 1), (2, 3), (3, 6), (4, 10), (5, 15)])
def test_calculate_triangular_number(n, expected):
    result = day.calculate_triangular_number(n)
    assert result == expected


def test_solve_part1(mock_input):
    expected = 37
    result = day.solve_part1(mock_input)
    assert result == expected


def test_solve_part2(mock_input):
    expected = 168
    result = day.solve_part2(mock_input)
    assert result == expected
