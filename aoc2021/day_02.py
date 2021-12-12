from pathlib import Path
from typing import List, Tuple

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202102_input.txt'


def load(filename: Path = INPUT_FILENAME) -> List[str]:
    with open(filename, 'r') as f:
        return f.read().strip().split('\n')


def parse_instruction(instruction: str) -> Tuple[int, int]:
    x, y = 0, 0
    direction, value = instruction.split()
    if direction == 'forward':
        x = int(value)
    elif direction == 'down':
        y = int(value)
    else:
        y = -int(value)
    return x, y


def solve_part1(input_: List[str]) -> int:
    x, y = (0, 0)
    for instruction in input_:
        delta_x, delta_y = parse_instruction(instruction)
        x += delta_x
        y += delta_y
    return x * y


def calculate_direction_update(instruction: str) -> Tuple[int, int, int]:
    x, y, aim = 0, 0, 0
    direction, value = instruction.split()
    if direction == 'forward':
        x, y = int(value), int(value)
    elif direction == 'down':
        aim = int(value)
    else:
        aim = -int(value)
    return x, y, aim


def solve_part2(input_: List[str]) -> int:
    x, y, aim = 0, 0, 0
    for instruction in input_:
        delta_x, delta_y, delta_aim = calculate_direction_update(instruction)
        aim += delta_aim
        x += delta_x
        y += delta_y * aim
    return x * y


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
