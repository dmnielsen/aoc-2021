import numpy as np
import pytest

from aoc2021 import day_04 as day


@pytest.fixture
def mock_input():
    test = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
    return test


@pytest.fixture
def mock_boards(mock_input):
    return day.parse_input(mock_input)[1]


class TestBingoBoard:
    @pytest.fixture
    def mock_bingo_array_board_three(self):
        return np.array(
            [
                ['14', '21', '17', '24', '4'],
                ['10', '16', '15', '9', '19'],
                ['18', '8', '23', '26', '20'],
                ['22', '11', '13', '6', '5'],
                ['2', '0', '12', '3', '7'],
            ]
        )

    def mock_bingo_array_board_two(self):
        return np.array(
            [
                ['3', '15', '0', '2', '22'],
                ['9', '18', '13', '17', '5'],
                ['19', '8', '7', '25', '23'],
                ['20', '11', '10', '24', '4'],
                ['14', '21', '16', '12', '6'],
            ]
        )

    def test_is_bingo(self, mock_bingo_array_board_three):
        board = day.BingoBoard(mock_bingo_array_board_three)
        numbers = '7,4,9,5,11,17,23,2,0,14,21,24'.split(',')
        assert board.is_bingo(set(numbers))

    def test_calculate_board_score(self, mock_bingo_array_board_three):
        board = day.BingoBoard(mock_bingo_array_board_three)
        numbers = '7,4,9,5,11,17,23,2,0,14,21,24'.split(',')
        result = board.calculate_board_score(set(numbers))

        expected = 188

        assert result == expected


def test_solve_part1(mock_input):
    expected = 4512
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 1924
    result = day.solve_part2(mock_input)
    assert expected == result
