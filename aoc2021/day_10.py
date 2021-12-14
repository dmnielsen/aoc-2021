from pathlib import Path
from typing import List

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202110_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> List[str]:
    return text.strip().split()


def replace_chunks_in_line(line: str) -> str:
    valid_chunks = ['()', '[]', '{}', '<>']
    for chunk in valid_chunks:
        line = line.replace(chunk, '')
    return line


def find_corrupted_line(line: str) -> str:
    corruptions = ['(]', '(}', '(>', '[)', '[}', '[>', '{)', '{]', '{>', '<)', '<]', '<}']
    replace_line = replace_chunks_in_line(line)
    while line != replace_line:
        line = replace_line
        replace_line = replace_chunks_in_line(line)
    check = [corruption for corruption in corruptions if corruption in line]
    if check:
        return check[0][1]
    else:
        return ''


def correct_incomplete_chunks(line: str) -> str:
    replace_line = replace_chunks_in_line(line)

    while line != replace_line:
        line = replace_line
        replace_line = replace_chunks_in_line(line)

    autocomplete = (
        line[::-1].replace('(', ')',).replace('[', ']').replace('{', '}').replace('<', '>')
    )
    return autocomplete


def score_completion(line: str) -> int:
    lookup = {')': 1, ']': 2, '}': 3, '>': 4}

    score = 0
    for char in line:
        score = score * 5 + lookup[char]
    return score


def solve_part1(input_: str) -> int:
    lookup = {')': 3, ']': 57, '}': 1197, '>': 25137}

    lines = parse_input(input_)
    corrupted_characters = [find_corrupted_line(line) for line in lines]
    return sum([lookup[char] for char in corrupted_characters if char])


def solve_part2(input_):
    lines = parse_input(input_)
    incomplete_lines = [
        correct_incomplete_chunks(line) for line in lines if not find_corrupted_line(line)
    ]
    scores = sorted([score_completion(line) for line in incomplete_lines])
    return scores[len(scores) // 2]


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
