from pathlib import Path
from typing import Tuple, List

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202121_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> Tuple[int, int]:
    text = text.split('\n')
    pos1 = int(text[0].split(':')[1])
    pos2 = int(text[1].split(':')[1])
    return pos1, pos2


def take_turn(loc: int, die_rolls: List[int]) -> int:
    loc += sum(die_rolls)
    loc = loc % 10
    if loc == 0:
        loc = 10
    return loc


def solve_part1(input_: str) -> int:
    loc1, loc2 = parse_input(input_)

    game_end_score = 1000
    score1, score2 = 0, 0
    total_rolls = 0
    die_value = 1

    player1_turn = True
    while (score1 < game_end_score) and (score2 < game_end_score):
        rolls = [v % 100 if (v % 100) else 100 for v in range(die_value, die_value + 3)]
        # print(rolls)
        if player1_turn:
            loc1 = take_turn(loc1, rolls)
            score1 += loc1
            # print(f'player 1: score={score1}; loc={loc1}')
            player1_turn = False
        else:
            loc2 = take_turn(loc2, rolls)
            score2 += loc2
            player1_turn = True
            # print(f'player 2: score={score2}; loc={loc2}')
        total_rolls += 3
        die_value = (die_value + 3) % 100
        if die_value == 0:
            die_value = 100

    losing_score = min([score1, score2])
    return losing_score * total_rolls


def solve_part2(input_: str):
    return


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
