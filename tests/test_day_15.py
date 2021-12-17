import pytest

from aoc2021 import day_15 as day


@pytest.fixture
def mock_input():
    text = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
    return text


def test_solve_part1(mock_input):
    expected = 40
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 315
    result = day.solve_part2(mock_input)
    assert expected == result
