import pytest

from aoc2021 import day_21 as day


@pytest.fixture
def mock_input():
    text = """Player 1 starting position: 4
Player 2 starting position: 8"""
    return text


def test_parse_input(mock_input):
    expected = (4, 8)
    result = day.parse_input(mock_input)
    assert result == expected


def test_solve_part1(mock_input):
    expected = 739785
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = None
    result = day.solve_part2(mock_input)
    assert expected == result
