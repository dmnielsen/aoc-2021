import pytest

from aoc2021 import day_13 as day


@pytest.fixture
def mock_input():
    text = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
    return text


def test_fold_twice(mock_input):
    expected = 16
    result = day.fold_twice(mock_input)


def test_solve_part1(mock_input):
    expected = 17
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = None
    result = day.solve_part2(mock_input)
    assert expected == result
