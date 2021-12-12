import numpy as np
import pytest

from aoc2021 import day_03 as day


@pytest.fixture()
def mock_tiny_input():
    text = """00100
11110
10110"""
    return text


@pytest.fixture
def mock_input():
    text = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    return text


def test_parse_input(mock_tiny_input):
    expected = np.array(
        [['0', '0', '1', '0', '0'], ['1', '1', '1', '1', '0'], ['1', '0', '1', '1', '0']]
    )
    result = day.parse_input(mock_tiny_input)
    np.testing.assert_array_equal(result, expected)


@pytest.fixture
def mock_report(mock_input):
    return day.parse_input(mock_input)


@pytest.mark.parametrize(
    'bits, expected', [(['0', '0', '0'], '0'), (['1', '0', '1'], '1'), (['0', '1'], '1')]
)
def test_return_most_frequent_bit(bits, expected):
    result = day.return_most_frequent_bit(bits)
    assert result == expected


@pytest.mark.parametrize(
    'bits, expected', [(['0', '0', '1'], '1'), (['1', '0', '1'], '0'), (['0', '1'], '0')]
)
def test_return_least_frequent_bit(bits, expected):
    result = day.return_least_frequent_bit(bits)
    assert result == expected


def test_determine_gamma_rate(mock_report):
    expected = 22
    result = day.determine_gamma_rate(mock_report)
    assert result == expected


def test_determine_epsilon_rate(mock_report):
    expected = 9
    result = day.determine_epsilon_rate(mock_report)
    assert result == expected


def test_determine_oxygen_generator_rating(mock_report):
    expected = 23
    result = day.determine_oxygen_generator_rating(mock_report)
    assert result == expected


def test_determine_co2_scrubber_rating(mock_report):
    expected = 10
    result = day.determine_co2_scrubber_rating(mock_report)
    assert result == expected


def test_solve_part1(mock_input):
    expected = 198
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 230
    result = day.solve_part2(mock_input)
    assert expected == result
