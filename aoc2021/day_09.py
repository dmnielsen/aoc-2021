from collections import namedtuple
from pathlib import Path
from typing import Dict

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202109_input.txt'

Coordinate = namedtuple('Coordinate', ['row', 'col'])


class HeightmapPoint:
    def __init__(self, coord: Coordinate, value: str, max_row: int, max_col: int):
        self.coord = coord
        self.value = int(value)
        self.risk = int(value) + 1
        self.max_row = max_row
        self.max_col = max_col
        self.neighbors = self.find_neighbors()

    def __repr__(self):
        return f'HeightmapPoint(coord={self.coord}, value={self.value}, max_row={self.max_row}, max_col={self.max_col})'

    def find_neighbors(self):
        points = [
            Coordinate(self.coord.row + 1, self.coord.col),
            Coordinate(self.coord.row - 1, self.coord.col),
            Coordinate(self.coord.row, self.coord.col - 1),
            Coordinate(self.coord.row, self.coord.col + 1),
        ]

        return [n for n in points if ((0 <= n.row < self.max_row) and (0 <= n.col < self.max_col))]


def load(filename: Path = INPUT_FILENAME):
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> Dict[Coordinate, HeightmapPoint]:
    lines = text.strip().split()
    max_row = len(lines)
    max_col = len(lines[0])

    heightmap = {}

    for row, line in enumerate(lines):
        for col, num in enumerate(line):
            coords = Coordinate(row, col)
            point_info = HeightmapPoint(coords, num, max_row=max_row, max_col=max_col)
            heightmap[coords] = point_info
    return heightmap


def solve_part1(input_: str):
    all_points = parse_input(input_)
    low_point_risk = []
    for point_coords, info in all_points.items():
        neighbor_values = [all_points[coords].value for coords in info.neighbors]
        if all(info.value < value for value in neighbor_values):
            low_point_risk.append(info.risk)
    return sum(low_point_risk)


def solve_part2(input_):
    return


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
