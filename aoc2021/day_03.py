from pathlib import Path
from typing import List

import numpy as np

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202103_input.txt'


def load(filename: Path = INPUT_FILENAME):
    with open(filename, 'r') as f:
        return f.read().strip()


def parse_input(input_: str) -> np.ndarray:
    output = []
    for line in input_.split():
        output.append(list(line))
    return np.array(output)


def return_most_frequent_bit(bits: List[str]) -> str:
    most_common_bit = max(set(bits), key=bits.count)
    if bits.count('0') == bits.count('1'):
        most_common_bit = '1'
    return most_common_bit


def return_least_frequent_bit(bits: List[str]) -> str:
    most_common_bit = min(set(bits), key=bits.count)
    if bits.count('0') == bits.count('1'):
        most_common_bit = '0'
    return most_common_bit


def determine_gamma_rate(report: np.ndarray) -> int:
    gamma_bin = []
    for col, _ in enumerate(report[0]):
        gamma_bin.append(return_most_frequent_bit(report[:, col].tolist()))
    return int(''.join(gamma_bin), 2)


def determine_epsilon_rate(report: np.ndarray) -> int:
    epsilon_bin = []
    for col, _ in enumerate(report[0]):
        epsilon_bin.append(return_least_frequent_bit(report[:, col].tolist()))
    return int(''.join(epsilon_bin), 2)


def filter_report(report: np.ndarray, col: int, filter_num: str) -> np.ndarray:
    return report[report[:, col] == filter_num]


def determine_oxygen_generator_rating(report: np.ndarray) -> int:
    filtered_report = report.copy()
    for col, _ in enumerate(report[0]):
        most_common_num = return_most_frequent_bit(filtered_report[:, col].tolist())
        filtered_report = filter_report(filtered_report, col, most_common_num)

        if filtered_report.shape[0] == 1:
            return int(''.join(filtered_report[0]), 2)


def determine_co2_scrubber_rating(report: np.ndarray) -> int:
    filtered_report = report.copy()
    for col, _ in enumerate(report[0]):
        least_common_num = return_least_frequent_bit(filtered_report[:, col].tolist())
        filtered_report = filter_report(filtered_report, col, least_common_num)

        if filtered_report.shape[0] == 1:
            return int(''.join(filtered_report[0]), 2)


def solve_part1(input_: str) -> int:
    report = parse_input(input_)
    gamma_rate = determine_gamma_rate(report)
    epsilon_rate = determine_epsilon_rate(report)

    return gamma_rate * epsilon_rate


def solve_part2(input_):
    report = parse_input(input_)
    oxygen_generator_rating = determine_oxygen_generator_rating(report)
    CO2_scrubber_rating = determine_co2_scrubber_rating(report)

    return oxygen_generator_rating * CO2_scrubber_rating


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
