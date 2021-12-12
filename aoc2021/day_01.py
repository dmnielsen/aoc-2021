from pathlib import Path

import numpy as np

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202101_input.txt'


def load(filename: Path = INPUT_FILENAME) -> np.ndarray:
    with open(filename, 'r') as f:
        depths = np.loadtxt(f)  # f.read()
    return depths


def solve_part1(input_: np.ndarray) -> int:
    return sum((input_[1:] - input_[:-1]) > 0)


def sum_sliding_windows(depths: np.ndarray, window_size: int) -> np.ndarray:
    grouped = np.lib.stride_tricks.sliding_window_view(depths, window_size)
    return np.sum(grouped, 1)


def solve_part2(input_: np.ndarray) -> int:
    depth_windows = sum_sliding_windows(input_, window_size=3)
    return sum((depth_windows[1:] - depth_windows[:-1]) > 0)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
