import pytest

from aoc2021 import day_12 as day


@pytest.fixture
def mock_input():
    text = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
    return text


def test_parse_input(mock_input):
    expected = {
        'start': ['A', 'b'],
        'A': ['c', 'b', 'end'],
        'b': ['A', 'd', 'end'],
        'c': ['A'],
        'd': ['b'],
    }
    result = day.parse_input(mock_input)
    assert result == expected


@pytest.mark.parametrize(
    'name, path, expected',
    [('d', 'start-d-end', True), ('d', 'start-d-A-d-A', False), ('A', 'start-d-A-d-A-b', True)],
)
def test_visit_cave(name, path, expected):
    result = day.visit_cave(name, path)
    assert result == expected


def test_solve_part1(mock_input):
    expected = 10
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 36
    result = day.solve_part2(mock_input)
    assert expected == result
