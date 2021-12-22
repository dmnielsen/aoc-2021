from collections import defaultdict
from itertools import product
from pathlib import Path

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202122_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str):
    instructions = []
    for line in text.strip().split('\n'):
        direction, coords = line.split(' ')
        direction = [1] if direction == 'on' else [0]
        for char in 'xyz=':
            coords = coords.replace(char, '')
        coords = [(int(v.split('..')[0]), int(v.split('..')[1]) + 1) for v in coords.split(',')]
        direction.extend(coords)
        instructions.append(direction)

    return instructions


def solve_part1(input_: str):
    # area_of_interest = "x=-50..50,y=-50..50,z=-50..50"
    area_of_interest = [(-50, 51), (-50, 51), (-50, 51)]

    instructions = parse_input(input_)

    cube = defaultdict(int)
    for direction, x_range, y_range, z_range in instructions:
        trim_x = (max(area_of_interest[0][0], x_range[0]), min(area_of_interest[0][1], x_range[1]))
        trim_y = (max(area_of_interest[1][0], y_range[0]), min(area_of_interest[1][1], y_range[1]))
        trim_z = (max(area_of_interest[2][0], z_range[0]), min(area_of_interest[2][1], z_range[1]))

        to_update = product(range(*trim_x), range(*trim_y), range(*trim_z))
        cube.update({coords: direction for coords in to_update})

    return sum(
        [
            cube[k]
            for k in list(
                product(
                    range(*area_of_interest[0]),
                    range(*area_of_interest[1]),
                    range(*area_of_interest[2]),
                )
            )
        ]
    )


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
