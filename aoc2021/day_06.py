from collections import Counter
from pathlib import Path
from typing import List

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202106_input.txt'


def load(filename: Path = INPUT_FILENAME):
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> List[int]:
    return [int(x) for x in text.split(',')]


def day_increment(fish: List[int]) -> List[int]:
    new_fish = [8] * fish.count(0)
    fish = [timer - 1 if (timer > 0) else 6 for timer in fish]
    fish.extend(new_fish)
    return fish


def increment_timers(fish: Counter) -> Counter:
    new_fish = fish[0]
    next_increment_dict = {8: new_fish, 6: new_fish}
    for i in range(8, 0, -1):
        next_increment_dict[i - 1] = fish[i] + next_increment_dict.get(i - 1, 0)
    return Counter(next_increment_dict)


def solve_part1(input_: str) -> int:
    fish = parse_input(input_)
    for day in range(80):
        fish = day_increment(fish)
    return len(fish)


def solve_part2(input_: str):
    fish = Counter(parse_input(input_))
    for day in range(256):
        fish = increment_timers(fish)
    return sum(fish.values())


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
