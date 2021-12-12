from collections import Counter
import pytest

from aoc2021 import day_06 as day


@pytest.fixture
def mock_input():
    return "3,4,3,1,2"


@pytest.mark.parametrize(
    'fish, expected', [([3, 4, 3, 1, 2], [2, 3, 2, 0, 1]), ([2, 3, 2, 0, 1], [1, 2, 1, 6, 0, 8])]
)
def test_day_increment(fish, expected):
    result = day.day_increment(fish)
    assert result == expected


def test_parse_input(mock_input):
    expected = [3, 4, 3, 1, 2]
    result = day.parse_input(mock_input)
    assert result == expected


@pytest.mark.parametrize(
    'fish, expected',
    [
        (
            Counter({3: 2, 4: 1, 1: 1, 2: 1}),
            Counter({2: 2, 3: 1, 0: 1, 1: 1, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0}),
        ),
        (
            Counter({2: 2, 3: 1, 0: 1, 1: 1}),
            Counter({1: 2, 2: 1, 6: 1, 0: 1, 8: 1, 7: 0, 5: 0, 4: 0, 3: 0}),
        ),
    ],
)
def test_day_increment(fish, expected):
    result = day.increment_timers(fish)
    assert result == expected


def test_solve_part1(mock_input):
    expected = 5934
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 26984457539
    result = day.solve_part2(mock_input)
    assert expected == result
