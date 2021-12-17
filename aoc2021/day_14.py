import re
from collections import Counter
from pathlib import Path
from typing import Dict, List, Tuple

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


def create_polymer_pair_map(rules: Dict[str, str]) -> Dict[str, List[str]]:
    return {k: [f'{k[0]}{v}', f'{v}{k[1]}'] for k, v in rules.items()}


def insert_elements(polymer: str, rules: Dict[str, str]) -> str:
    pairs = [polymer[i : i + 2] for i, _ in enumerate(polymer)]
    trailing_letter = [pairs.pop()]
    return ''.join([f'{pair[0]}{rules[pair]}' for pair in pairs] + trailing_letter)


def update_pairs(pairs: Counter, pair_map: Dict[str, List[str]]) -> Counter:
    new_pairs = Counter()
    for pair, count in pairs.items():
        new_pairs.update({pp: count for pp in pair_map[pair]})

    return new_pairs


def calculate_difference(polymer_str: str) -> int:
    element_counts = Counter(polymer_str)
    # print(element_counts.most_common())
    return element_counts.most_common(1)[0][1] - element_counts.most_common()[-1][1]


def count_elements_calculate_difference(pair_counts: Counter, trailing_letter: str) -> int:
    element_counts = Counter()
    for pair, count in pair_counts.items():
        element_counts.update({pair[0]: count})
        # element_counts.update({pair[1]: count})
    element_counts.update({trailing_letter: 1})
    return element_counts.most_common(1)[0][1] - element_counts.most_common()[-1][1]


def solve_part1(input_: str) -> int:
    template, rules = parse_input(input_)
    for i in range(10):
        template = insert_elements(template, rules)
        calculate_difference(template)

    return calculate_difference(template)


def count_elements(pair_counts):
    element_counts = Counter()
    for pair, count in pair_counts.items():
        element_counts.update({pair[0]: count})
        # element_counts.update({pair[1]: count})
    return element_counts


def solve_part2(input_: str) -> int:
    template, rules = parse_input(input_)
    pairs_map = create_polymer_pair_map(rules)

    polymer_pairs = [template[i : i + 2] for i, _ in enumerate(template)]
    trailing_letter = polymer_pairs.pop()
    pairs = Counter(polymer_pairs)

    for i in range(40):
        pairs = update_pairs(pairs, pairs_map)
    return count_elements_calculate_difference(pairs, trailing_letter)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
