import re
from collections import namedtuple
from pathlib import Path
from typing import List, Tuple

import numpy as np

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202113_input.txt'

Point = namedtuple('Point', ['x', 'y'])


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> Tuple[List[Point], List[Tuple[str, int]]]:
    dots, instructions = text.split('\n\n')

    dots = [d.split(',') for d in dots.split('\n')]
    dots = [Point(int(x), int(y)) for x, y in dots]

    instructions = re.findall(r'.*([xy])=(\d*)', instructions)
    instructions = [(dir, int(line)) for dir, line in instructions]

    return dots, instructions


def fold_sheet(dots: List[Point], instruction: Tuple[str, int]):
    if instruction[0] == 'y':
        fold_row = instruction[1]
        dots = [
            Point(point.x, fold_row - (point.y - fold_row)) if point.y > fold_row else point
            for point in dots
        ]
    else:
        fold_col = instruction[1]
        dots = [
            Point(fold_col + (fold_col - point.x), point.y) if point.x > fold_col else point
            for point in dots
        ]
    return list(set(dots))


def fold_twice(text: str):
    dots, instructions = parse_input(text)
    folded_dots = fold_sheet(dots, instructions[0])
    folded_dots = fold_sheet(folded_dots, instructions[1])
    # print_sheet(folded_dots)
    return len(folded_dots)


def print_sheet(dots: List[Point]):
    print()
    grid = np.full((7, 256), ' ')
    for dot in dots:
        grid[dot.y, dot.x] = '█'
    raster_grid = [''.join(row) for row in grid]
    print('\n'.join(raster_grid))
    return grid


def solve_part1(input_: str) -> int:
    dots, instructions = parse_input(input_)
    folded_dots = fold_sheet(dots, instructions[0])
    # print_sheet(folded_dots)

    return len(folded_dots)


def solve_part2(input_: str):
    dots, instructions = parse_input(input_)
    for instruction in instructions:
        dots = fold_sheet(dots, instruction)

    print_sheet(dots)
    return len(dots)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
