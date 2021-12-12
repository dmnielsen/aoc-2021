import numpy as np
from pathlib import Path
from typing import List, Set, Tuple

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions


INPUT_FILENAME = AOC_DIR / 'inputs' / '202104_input.txt'


class BingoBoard:
    def __init__(self, board: np.ndarray):
        self.rows = [set(row) for row in board]
        self.columns = [set(col) for col in board.T]

    def is_bingo(self, numbers: Set) -> bool:
        if any(not (x - numbers) for x in self.rows):
            return True
        if any(not (x - numbers) for x in self.columns):
            return True
        else:
            return False

    def calculate_board_score(self, numbers: Set) -> int:
        unmarked_numbers = set().union(*self.rows) - numbers
        return sum([int(x) for x in unmarked_numbers])


def load(filename: Path = INPUT_FILENAME):
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> Tuple[List[str], List[BingoBoard]]:
    text = text.split()
    number_draw = text[0].split(',')
    board_rows = np.reshape(np.array(text[1:]), (-1, 5))

    boards = [BingoBoard(board_rows[i:i+5]) for i in range(0, len(board_rows), 5)]

    return number_draw, boards


def solve_part1(input_: str) -> int:
    numbers, boards = parse_input(input_)

    for i, number in enumerate(numbers[4:], start=4):
        called_numbers = numbers[:i+1]
        for board in boards:
            if board.is_bingo(set(called_numbers)):
                return int(number) * board.calculate_board_score(set(called_numbers))


def solve_part2(input_: str) -> int:
    numbers, boards = parse_input(input_)

    for i, number in enumerate(numbers[4:], start=4):
        called_numbers = numbers[:i+1]

        for i, board in enumerate(boards):
            bingo_status = board.is_bingo(set(called_numbers))
            if bingo_status and (len(boards) > 1):
                del boards[i]
            elif bingo_status and (len(boards) == 1):
                return int(number) * board.calculate_board_score(set(called_numbers))
            else:
                continue


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
