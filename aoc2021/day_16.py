from math import prod
from pathlib import Path
from typing import Tuple

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202116_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def hex_to_binary(text: str) -> str:
    text = text.strip()
    binary = bin(int(text, 16))
    return f'{binary[2:]:0>{len(text) * 4}}'


def extract_literal_value(s: str):
    bits = []
    i = 0
    while True:
        if s[i] == '0':
            bits.append(s[i + 1 : i + 5])
            i += 5
            break
        else:
            bits.append(s[i + 1 : i + 5])
            i += 5
    return i, int(''.join(bits), 2)


def b2int(b: str) -> int:
    return int(b, 2)


def part_one_again(i, message) -> Tuple[int, int]:
    version_sum = b2int(message[i : i + 3])
    type_id = b2int(message[i + 3 : i + 6])

    i += 6

    if type_id == 4:  # literal type
        while True:
            if message[i] == '0':
                i += 5
                break
            else:
                i += 5
    else:
        length_type_id = b2int(message[i])
        i += 1
        if length_type_id == 0:
            # next 15 bits define length of sub-packet in bits
            subpacket_end = i + 15 + b2int(message[i : i + 15])
            i += 15
            while i < subpacket_end:
                i, version = part_one_again(i, message)
                version_sum += version
        else:
            # next 11 bits define count of sub-packets
            number_of_subpackets = b2int(message[i : i + 11])
            i += 11
            for n in range(number_of_subpackets):
                i, version = part_one_again(i, message)
                version_sum += version

    return i, version_sum


OPERATIONS = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1]),
}


def decode_transmission(i, message) -> Tuple[int, int]:
    version = b2int(message[i : i + 3])
    type_id = b2int(message[i + 3 : i + 6])
    # breakpoint()

    i += 6

    if type_id == 4:  # literal type
        bits = []
        while True:
            if message[i] == '0':
                bits.append(message[i + 1 : i + 5])
                i += 5
                break
            else:
                bits.append(message[i + 1 : i + 5])
                i += 5
        value = b2int(''.join(bits))
    else:
        length_type_id = b2int(message[i])
        i += 1
        values = []
        if length_type_id == 0:
            # next 15 bits define length of sub-packet in bits
            subpacket_end = i + 15 + b2int(message[i : i + 15])
            i += 15
            while i < subpacket_end:
                i, v = decode_transmission(i, message)
                values.append(v)

        else:
            # next 11 bits define count of sub-packets
            number_of_subpackets = b2int(message[i : i + 11])
            i += 11
            for n in range(number_of_subpackets):
                i, v = decode_transmission(i, message)
                values.append(v)
        value = OPERATIONS[type_id](values)

    return i, value


def solve_part1(input_: str) -> int:
    message = hex_to_binary(input_)
    return part_one_again(0, message)[1]


def solve_part2(input_: str) -> int:
    message = hex_to_binary(input_)
    return decode_transmission(0, message)[1]


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
