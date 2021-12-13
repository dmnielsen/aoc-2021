from collections import Counter, namedtuple
from pathlib import Path
from typing import Dict, List, Set, Tuple

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202108_input.txt'


def load(filename: Path = INPUT_FILENAME):
    with open(filename, 'r') as f:
        return f.read()


def split_and_flatten_input(text: str) -> Tuple[List[str], List[str]]:
    signal_patterns = []
    output_values = []
    lines = text.strip().split('\n')
    for line in lines:
        left, right = line.strip().split(' | ')
        signal_patterns.extend(left.split())
        output_values.extend(right.split())
    return signal_patterns, output_values


def parse_input(text: str) -> List[Tuple[List[str], List[str]]]:
    signal_list = []
    lines = text.strip().split('\n')
    for line in lines:
        signals, digits = line.strip().split(' | ')
        signals = [x for x in signals.split()]
        digits = [x for x in digits.split()]
        signal_list.append((signals, digits))
    return signal_list


def build_decoder(signal_text: List[str]) -> List[Set[str]]:
    signals = sorted(signal_text, key=len)
    decode_list = [
        -1,
        set(signals[0]),
        -1,
        -1,
        set(signals[2]),
        -1,
        -1,
        set(signals[1]),
        set(signals[-1]),
        -1,
    ]

    signals = [set(s) for s in signals if set(s) not in decode_list]
    # find 3
    for sig in signals:
        if len(sig) == 5 and len(sig - decode_list[1]) == 3:
            decode_list[3] = sig
            signals.remove(sig)
            break
    # find 9
    for sig in signals:
        if len(sig) == 6 and len(sig - decode_list[3]) == 1:
            decode_list[9] = sig
            signals.remove(sig)
            break
    # find 0
    for sig in signals:
        if len(sig) == 6 and len(sig - decode_list[1]) == 4:
            decode_list[0] = sig
            signals.remove(sig)
            break
    # pull 6 out
    decode_list[6] = signals[-1]
    del signals[-1]

    # find 5
    for sig in signals:
        if len(sig - decode_list[6]) == 0:
            decode_list[5] = sig
            signals.remove(sig)
    decode_list[2] = signals[0]

    return decode_list


def decode_digits(decoder, digits) -> int:
    digit_str = ''
    for digit in digits:
        digit_str += str(decoder.index(set(digit)))
    return int(digit_str)


def solve_part1(input_: str) -> int:
    _, output_values = split_and_flatten_input(input_)
    counts = Counter([len(digit) for digit in output_values])
    return counts[2] + counts[4] + counts[3] + counts[7]


def solve_part2(input_: str):
    number_lists = parse_input(input_)
    decoded_digits = []
    for signals, digits in number_lists:
        decoder = build_decoder(signals)
        decoded_digits.append(decode_digits(decoder, digits))

    return sum(decoded_digits)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
