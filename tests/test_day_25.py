import pytest

from aoc2021 import day_25 as day


@pytest.fixture
def mock_input():
    text = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""
    return text


@pytest.mark.parametrize(
    'in_text, expected_text',
    [
        ('...>>>>>...', '...>>>>.>..'),
        ('...>>>>.>..', '...>>>.>.>.')
    ]
)
def test_move_east_herd(in_text, expected_text):
    east_herd, _, empty_spaces = day.parse_map(in_text)
    boundary = len(in_text)

    expected_herd, _, expected_spaces = day.parse_map(expected_text)

    result_spaces, result_herd = day.move_east_herd(empty_spaces, east_herd, boundary)
    assert result_spaces == expected_spaces
    assert result_herd == expected_herd


def test_get_south_and_east_boundaries(mock_input):
    expected = (9, 10)
    result = day.get_south_and_east_boundaries(mock_input)
    assert result == expected


def test_solve_part1(mock_input):
    expected = 58
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = None
    result = day.solve_part2(mock_input)
    assert expected == result
