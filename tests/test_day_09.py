import pytest

from aoc2021 import day_09 as day
from aoc2021.day_09 import Coordinate


@pytest.fixture
def mock_input():
    text = """2199943210
3987894921
9856789892
8767896789
9899965678"""
    return text


@pytest.fixture
def mock_point_dict(mock_input):
    return day.parse_input(mock_input)


def test_find_low_points(mock_point_dict):
    expected = [Coordinate(0, 1), Coordinate(0, 9), Coordinate(2, 2), Coordinate(4, 6)]
    result = day.find_low_points(mock_point_dict)
    assert len(result) == len(expected)
    assert all([point in result for point in expected])


@pytest.mark.parametrize(
    'point, expected',
    [
        (Coordinate(0, 1), [Coordinate(0, 1), Coordinate(0, 0), Coordinate(1, 0)]),
        (
            Coordinate(2, 2),
            [
                Coordinate(1, 2),
                Coordinate(1, 3),
                Coordinate(1, 4),
                Coordinate(2, 1),
                Coordinate(2, 2),
                Coordinate(2, 3),
                Coordinate(2, 4),
                Coordinate(2, 5),
                Coordinate(3, 0),
                Coordinate(3, 1),
                Coordinate(3, 2),
                Coordinate(3, 3),
                Coordinate(3, 4),
                Coordinate(4, 1),
            ],
        ),
    ],
)
def test_find_basin(point, expected, mock_point_dict):
    result = day.find_basin(point, mock_point_dict)
    assert len(result) == len(expected)
    assert all([point in result for point in expected])


def test_solve_part1(mock_input):
    expected = 15
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 1134
    result = day.solve_part2(mock_input)
    assert expected == result
