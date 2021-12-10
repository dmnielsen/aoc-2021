import pytest

from aoc2021 import day_02 as day


@pytest.fixture
def mock_input():
    text = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
    return text.split('\n')


def test_solve_part1(mock_input):
    expected = 150
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 900
    result = day.solve_part2(mock_input)
    assert expected == result
