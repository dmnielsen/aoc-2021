from pathlib import Path

import numpy as np

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202107_input.txt'


def load(filename: Path = INPUT_FILENAME):
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> np.ndarray:
    return np.fromstring(text, sep=',')


def optimize_fuel_usage(positions: np.ndarray) -> int:
    min_, max_ = int(positions.min()), int(positions.max())
    best_fuel_cost = max_ * len(positions)
    for position in range(min_, max_ + 1):
        fuel_cost = np.absolute(np.full_like(positions, fill_value=position) - positions).sum()
        if fuel_cost < best_fuel_cost:
            best_fuel_cost = fuel_cost
    return best_fuel_cost


def calculate_triangular_number(n: float) -> float:
    return n * (n + 1) / 2


def optimize_fuel_usage_harder(positions: np.ndarray) -> int:
    min_, max_ = int(positions.min()), int(positions.max())
    best_fuel_cost = calculate_triangular_number(max_) * len(positions)
    for position in range(min_, max_ + 1):
        abs_moves = np.absolute(np.full_like(positions, fill_value=position) - positions)
        fuel_cost = sum([calculate_triangular_number(x) for x in abs_moves])
        if fuel_cost < best_fuel_cost:
            best_fuel_cost = fuel_cost

    return best_fuel_cost


def solve_part1(input_: str) -> int:
    positions = parse_input(input_)
    fuel_cost = optimize_fuel_usage(positions)
    return int(fuel_cost)


def solve_part2(input_: str) -> int:
    positions = parse_input(input_)
    fuel_cost = optimize_fuel_usage_harder(positions)
    return int(fuel_cost)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
