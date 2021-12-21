import pytest

from aoc2021 import day_17 as day


@pytest.fixture
def mock_input():
    return """target area: x=20..30, y=-10..-5"""


def test_parse_input(mock_input):
    expected = ([20, 30], [-10, -5])
    result = day.parse_input(mock_input)
    assert expected == result


def test_find_x_velocities():
    x_range = [20, 30]
    expected = [6, 7]
    result = day.find_x_velocities(x_range)
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize(
    'vx, vy, expected', [(9, 0, True), (7, 2, True), (6, 3, True), (17, -4, False), (6, 9, True)]
)
def test_trajectory_hits_target(vx, vy, expected):
    result = day.trajectory_hits_target(vx, vy, [20, 30], [-10, -5])
    assert result == expected


def test_solve_part1(mock_input):
    expected = 45
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 112
    result = day.solve_part2(mock_input)
    assert expected == result
