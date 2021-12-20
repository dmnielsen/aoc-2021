import numpy as np
import pytest

from aoc2021 import day_20 as day


@pytest.fixture
def mock_input():
    text = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""
    return text


def test_parse_input_returns_correct_size_str_for_algo(mock_input):
    algo, _ = day.parse_input(mock_input)
    assert len(algo) == 512
    assert isinstance(algo, str)


def test_parse_input_returns_image_array(mock_input):
    expected = np.array(
        [
            ['1', '0', '0', '1', '0'],
            ['1', '0', '0', '0', '0'],
            ['1', '1', '0', '0', '1'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '1', '1', '1'],
        ]
    )
    _, result = day.parse_input(mock_input)
    np.testing.assert_array_equal(result, expected)


def test_solve_part1(mock_input):
    expected = 35
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 3351
    result = day.solve_part2(mock_input)
    assert expected == result
