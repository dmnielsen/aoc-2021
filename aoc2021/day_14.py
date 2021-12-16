import re
from collections import Counter
from pathlib import Path
from typing import Dict, Tuple

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202114_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> Tuple[str, Dict[str, str]]:
    template, rules = text.split('\n\n')

    rules = re.findall(r'(\S\S) -> (\S)', rules)
    rules = {pair: element for pair, element in rules}
    return template, rules


def insert_elements(polymer: str, rules: Dict[str, str]) -> str:
    pairs = [polymer[i : i + 2] for i, _ in enumerate(polymer)]
    trailing_letter = [pairs.pop()]
    return ''.join([f'{pair[0]}{rules[pair]}' for pair in pairs] + trailing_letter)


def solve_part1(input_: str) -> int:
    template, rules = parse_input(input_)
    for i in range(10):
        template = insert_elements(template, rules)

    element_counts = Counter(template)
    return element_counts.most_common(1)[0][1] - element_counts.most_common()[-1][1]


def solve_part2(input_: str) -> int:
    return


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
