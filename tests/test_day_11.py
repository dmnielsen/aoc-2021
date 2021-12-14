import pytest

from aoc2021 import day_11 as day
from aoc2021.day_11 import Coordinate


@pytest.fixture
def mock_input():
    text = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
    return text


@pytest.fixture
def mock_valid_coordinates():
    coords = []
    for i in range(0, 3):
        for j in range(0, 3):
            coords.append(Coordinate(i, j))
    return coords


@pytest.mark.parametrize(
    'coord, expected',
    [
        (Coordinate(0, 0), [Coordinate(0, 1), Coordinate(1, 1), Coordinate(1, 0)]),
        (
            Coordinate(1, 1),
            [
                Coordinate(0, 0),
                Coordinate(0, 1),
                Coordinate(0, 2),
                Coordinate(1, 0),
                Coordinate(1, 2),
                Coordinate(2, 0),
                Coordinate(2, 1),
                Coordinate(2, 2),
            ],
        ),
        (
            Coordinate(2, 1),
            [
                Coordinate(1, 0),
                Coordinate(1, 1),
                Coordinate(1, 2),
                Coordinate(2, 0),
                Coordinate(2, 2),
            ],
        ),
    ],
)
def test_find_valid_adjacent_coords(coord, expected, mock_valid_coordinates):
    result = day.find_valid_adjacent_coords(coord, mock_valid_coordinates)
    assert len(result) == len(expected)
    assert all([coord in result for coord in expected])


def test_solve_part1(mock_input):
    expected = 1656
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 195
    result = day.solve_part2(mock_input)
    assert expected == result
