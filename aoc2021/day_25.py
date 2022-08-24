from copy import copy, deepcopy
from pathlib import Path
from typing import Set, Tuple, NamedTuple

import numpy as np

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202125_input.txt'


class Coords(NamedTuple):
    row: int
    col: int


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def get_south_and_east_boundaries(text: str) -> Tuple[int, int]:
    text = text.strip().split('\n')
    return len(text), len(text[0])


def parse_map(text: str) -> Tuple[Set[Coords], Set[Coords], Set[Coords]]:
    east_herd = set()
    south_herd = set()
    grid = set()
    empty_spaces = set()
    for i, row in enumerate(text.strip().split('\n')):
        for j, marker in enumerate(row):
            position = Coords(i, j)
            if marker == '>':
                east_herd.add(position)
                grid.add(position)
            elif marker == 'v':
                south_herd.add(position)
                grid.add(position)
            else:
                empty_spaces.add(position)
    print(f'empty_spaces: {len(empty_spaces)}')
    return east_herd, south_herd, empty_spaces


def move_east_herd(empty_spaces: Set[Coords], herd: Set[Coords], boundary: int) -> Tuple[Set[Coords], Set[Coords]]:
    filled_space = []
    emptied_space = []
    for coords in empty_spaces:
        look_west = Coords(coords.row, coords.col - 1)
        if look_west.col < 0:
            look_west = Coords(look_west.row, boundary - 1)
        if look_west in herd:
            filled_space.append(coords)
            emptied_space.append(look_west)

    if filled_space:
        empty_spaces = empty_spaces.copy()
        empty_spaces.difference_update(filled_space)
        empty_spaces.update(emptied_space)

        herd = herd.copy()
        herd.difference_update(emptied_space)
        herd.update(filled_space)

    return empty_spaces, herd


def move_south_herd(empty_spaces: Set[Coords], herd: Set[Coords], boundary: int) -> Tuple[Set[Coords], Set[Coords]]:
    filled_space = []
    emptied_space = []
    for coords in empty_spaces:
        look_north = Coords(coords.row - 1, coords.col)
        if look_north.row < 0:
            look_north = Coords(boundary - 1, look_north.col)
        if look_north in herd:
            filled_space.append(coords)
            emptied_space.append(look_north)

    if filled_space:
        empty_spaces = empty_spaces.copy()
        empty_spaces.difference_update(filled_space)
        empty_spaces.update(emptied_space)

        herd = herd.copy()
        herd.difference_update(emptied_space)
        herd.update(filled_space)

    return empty_spaces, herd


def print_grid(east_herd: Set[Coords], south_herd: Set[Coords], east_bound: int, south_bound: int):
    grid = np.full((south_bound, east_bound), fill_value='.')
    for coord in east_herd:
        grid[coord] = '>'
    for coord in south_herd:
        grid[coord] = 'v'
    for row in grid:
        print(''.join(row))
    print()


def solve_part1(input_: str):
    south_max, east_max = get_south_and_east_boundaries(input_)
    east_herd, south_herd, empty_spaces = parse_map(input_)
    # print_grid(east_herd, south_herd, east_max, south_max)
    # print(len(east_herd), len(south_herd))

    step = 1
    while True:
        # if step % 10 == 0:
        #     print(step)
        empty_spaces, update_east_herd = move_east_herd(empty_spaces, east_herd, east_max)
        empty_spaces, update_south_herd = move_south_herd(empty_spaces, south_herd, south_max)

        # print_grid(update_east_herd, update_south_herd, east_max, south_max)

        if (update_east_herd == east_herd) and (update_south_herd == south_herd):
            break
        else:
            east_herd = update_east_herd
            south_herd = update_south_herd
            step += 1

    return step


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
