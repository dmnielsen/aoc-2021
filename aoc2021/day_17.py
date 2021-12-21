from pathlib import Path
from typing import List, Tuple

import numpy as np

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202117_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> Tuple[List[int], List[int]]:
    x, y = text.strip('target area: ').strip().split(',')
    x = [int(xx) for xx in x.strip('x=').split('..')]
    y = [int(yy) for yy in y.strip(' y=').split('..')]
    return x, y


def quadratic_formula(a: int, b: int, c: int) -> Tuple[int, int]:
    d = (b ** 2 - 4 * a * c) ** 0.5
    return (-b + d) / (2 * a), (-b - d) / (2 * a)


def find_x_velocities(vx: List[int]):
    solutions = []
    for v in vx:
        solutions.extend(quadratic_formula(1, 1, -2 * v))
    return list(set(round(sol, 0) for sol in solutions if sol > 0))


def triangular_number(n: int) -> int:
    return int(n * (n + 1) / 2)


def timesteps_inside_target_horizontal(v_x, min_x, max_x) -> np.ndarray:
    position_til_stop = np.cumsum(np.arange(v_x, -1, -1))

    inside_target = np.where((min_x <= position_til_stop) & (max_x >= position_til_stop))

    return inside_target[0]


def trajectory_hits_target(vx, vy, x_range, y_range):
    x, y = 0, 0
    t = 0
    # breakpoint()
    while (x < x_range[1]) and (y > y_range[0]):
        x += vx
        y += vy
        if (x_range[0] <= x <= x_range[1]) and (y_range[0] <= y <= y_range[1]):
            return True
        vx = vx - 1 if vx > 0 else 0
        vy = vy - 1
        t += 1

    return False


def solve_part1(input_: str) -> int:
    x, y = parse_input(input_)
    # find v_x where v_x = 0 and probe in free fall
    vxs = find_x_velocities(x)

    value = abs(min(y)) - 1

    return triangular_number(value)


def solve_part2(input_: str):
    # This is a terrible way to do this
    x_range, y_range = parse_input(input_)

    min_vx = int(min(find_x_velocities(x_range)))
    max_vx = int(max(x_range))

    min_vy = int(min(y_range))
    max_vy = triangular_number(abs(min(y_range)) - 1)
    # breakpoint()
    possible_launch = []
    for vx in range(min_vx, max_vx + 1):
        for vy in range(min_vy, max_vy + 1):
            if trajectory_hits_target(vx, vy, x_range, y_range):
                possible_launch.append((vx, vy))

    return len(possible_launch)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
