from copy import deepcopy
from itertools import permutations
from pathlib import Path
from typing import List

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202118_input.txt'


class SnailNumber(object):
    def __init__(self, left, right):
        if isinstance(left, list):
            left = SnailNumber(*left)
        if isinstance(right, list):
            right = SnailNumber(*right)

        self.left = left
        self.right = right

    def __str__(self):
        return f'[{self.left}, {self.right}]'

    def __repr__(self):
        return f'SnailNumber({self.left}, {self.right})'

    def __eq__(self, other) -> bool:
        if self.left == other.left and self.right == other.right:
            return True
        return False

    def reduce(self):
        while True:
            if self.must_explode():
                self.explode()
                continue
            elif self.must_split():
                self.split()
                continue
            else:
                break

    def magnitude(self):
        return 3 * self.magnitude_left() + 2 * self.magnitude_right()

    def magnitude_left(self):
        if self.left_is_snail():
            return self.left.magnitude()
        else:
            return self.left

    def magnitude_right(self):
        if self.right_is_snail():
            return self.right.magnitude()
        else:
            return self.right

    def left_is_snail(self) -> bool:
        return isinstance(self.left, SnailNumber)

    def right_is_snail(self) -> bool:
        return isinstance(self.right, SnailNumber)

    def add_to_right(self, val):
        if self.right_is_snail():
            self.right.add_to_leftmost_right_leaf(val)
        else:
            # breakpoint()
            self.right += val

    def add_to_leftmost_right_leaf(self, val):
        # I hate this so much
        if self.left_is_snail():
            self.left.add_to_leftmost_right_leaf(val)
        else:
            self.left += val

    def add_to_left(self, val):
        if self.left_is_snail():
            self.left.add_to_rightmost_left_leaf(val)
        else:
            self.left += val

    def add_to_rightmost_left_leaf(self, val):
        if self.right_is_snail():
            self.right.add_to_rightmost_left_leaf(val)
        else:
            self.right += val

    def must_explode(self, n_parents: int = 0):
        if n_parents == 3:
            if self.left_is_snail() or self.right_is_snail():
                return True
            return False
        else:
            status_left, status_right = False, False
            if self.left_is_snail():
                status_left = self.left.must_explode(n_parents=n_parents + 1)
            if self.right_is_snail():
                status_right = self.right.must_explode(n_parents=n_parents + 1)
            return status_left or status_right

    def set_node_to_zero(self, vals):
        if vals is None:
            return False
        return all([val is not None for val in vals])

    def explode(self, n_parents: int = 0):
        # breakpoint()

        if not self.left_is_snail() and not self.right_is_snail():
            if n_parents >=4:
                return [self.left, self.right]
            else:
                return None
        else:
            vals = None
            if self.left_is_snail():
                vals = self.left.explode(n_parents=n_parents + 1)
                # if both vals present, set left node to 0
                if self.set_node_to_zero(vals):
                    self.left = 0
                if vals is not None and vals[1] is not None:
                    self.add_to_right(vals[1])
                    vals[1] = None
                    return vals
            if vals is None and self.right_is_snail():
                vals = self.right.explode(n_parents=n_parents + 1)
                if self.set_node_to_zero(vals):
                    self.right = 0
                if vals is not None and vals[0] is not None:
                    self.add_to_left(vals[0])
                    vals[0] = None
                    return vals
            return vals

    def must_split(self) -> bool:
        status_left, status_right = False, False
        if not self.left_is_snail():
            if self.left > 9:
                status_left = True
        else:
            status_left = self.left.must_split()
        if not self.right_is_snail():
            if self.right > 9:
                status_right = True
        else:
            status_right = self.right.must_split()
        return status_left or status_right

    def split(self):
        already_split = False
        if not self.left_is_snail():
            if self.left > 9:
                l = self.left // 2
                r = self.left - l
                self.left = SnailNumber(l, r)
                already_split = True
        else:
            already_split = self.left.split()
        if not already_split:
            if not self.right_is_snail():
                if self.right > 9:
                    l = self.right // 2
                    r = self.right - l
                    self.right = SnailNumber(l, r)
                    already_split = True
            else:
                already_split = self.right.split()
        return already_split


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def load_snail_numbers(text: str) -> List[SnailNumber]:
    numbers = []
    for line in text.strip().split('\n'):
        numbers.append(parse_written_snail_number(line))
    return numbers


def parse_written_snail_number(text) -> SnailNumber:
    text = text.replace('[', 'SnailNumber(').replace(']', ')')
    return eval(text)


def add(sn1: SnailNumber, sn2: SnailNumber) -> SnailNumber:
    added_number = SnailNumber(deepcopy(sn1), deepcopy(sn2))
    added_number.reduce()
    return added_number


def solve_part1(input_: str) -> int:
    print()
    numbers = load_snail_numbers(input_)
    current_number = numbers[0]
    for number in numbers[1:]:
        current_number = add(current_number, number)
    return current_number.magnitude()


def solve_part2(input_: str):
    print()
    numbers = load_snail_numbers(input_)
    largest_magnitude = -1
    for pair in permutations(numbers, 2):
        current_number = add(*pair)
        if (curr_mag := current_number.magnitude()) > largest_magnitude:
            largest_magnitude = curr_mag
    return largest_magnitude


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
