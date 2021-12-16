import pytest

from aoc2021 import day_14 as day


@pytest.fixture
def mock_input():
    text = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
    return text


@pytest.fixture
def trial_inputs(mock_input):
    return day.parse_input(mock_input)


def test_insert_elements(trial_inputs):
    expected = 'NCNBCHB'
    result = day.insert_elements(*trial_inputs)
    assert result == expected


def test_solve_part1(mock_input):
    expected = 1588
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 2188189693529
    result = day.solve_part2(mock_input)
    assert expected == result
