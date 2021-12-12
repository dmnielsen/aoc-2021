import pytest

from aoc2021 import day_05 as day
from aoc2021.day_05 import Point, Vent


@pytest.fixture
def mock_input():
    text = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
    return text


def test_parse_line_list():
    text = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4"""
    expected = [(Point(0, 9), Point(5, 9)), (Point(8, 0), Point(0, 8)), (Point(9, 4), Point(3, 4))]
    result = day.parse_line_list(text)
    assert result == expected


@pytest.fixture
def mock_points(mock_input):
    return day.parse_line_list(mock_input)


@pytest.mark.parametrize(
    'vent, expected',
    [
        (Vent(Point(0, 9), Point(5, 9)), True),
        (Vent(Point(2, 2), Point(2, 1)), True),
        (Vent(Point(8, 0), Point(0, 8)), False),
    ],
)
def test_is_horizontal_or_vertical(vent, expected):
    result = day.is_horizontal_or_vertical(vent)
    assert result == expected


@pytest.mark.parametrize(
    'vent, expected',
    [
        (Vent(Point(0, 0), Point(2, 0)), [Point(0, 0), Point(1, 0), Point(2, 0)]),
        (Vent(Point(0, 0), Point(0, 2)), [Point(0, 0), Point(0, 1), Point(0, 2)]),
        (Vent(Point(2, 0), Point(0, 0)), [Point(2, 0), Point(1, 0), Point(0, 0)]),
        (Vent(Point(0, 2), Point(0, 0)), [Point(0, 2), Point(0, 1), Point(0, 0)]),
        (Vent(Point(0, 0), Point(2, 2)), [Point(0, 0), Point(1, 1), Point(2, 2)]),
        (Vent(Point(2, 2), Point(0, 0)), [Point(2, 2), Point(1, 1), Point(0, 0)]),
        (Vent(Point(0, 2), Point(2, 0)), [Point(0, 2), Point(1, 1), Point(2, 0)]),
        (Vent(Point(2, 0), Point(0, 2)), [Point(2, 0), Point(1, 1), Point(0, 2)]),
    ],
)
def test_return_vent_points(vent, expected):
    result = day.return_vent_points(vent)
    assert result == expected


def test_solve_part1(mock_input):
    expected = 5
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 12
    result = day.solve_part2(mock_input)
    assert expected == result
