import pytest

from aoc2021 import day_09 as day


@pytest.fixture
def mock_input():
    text = """2199943210
3987894921
9856789892
8767896789
9899965678"""
    return text


def test_solve_part1(mock_input):
    expected = 15
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = None
    result = day.solve_part2(mock_input)
    assert expected == result
