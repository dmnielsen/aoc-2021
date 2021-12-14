from math import prod
from pathlib import Path
from typing import Dict, List

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202109_input.txt'


class Coordinate:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __repr__(self):
        return f'Coordinate(row={self.row}, col={self.col})'

    def __eq__(self, other):
        return (
            hasattr(other, 'row')
            and hasattr(other, 'col')
            and self.row == other.row
            and self.col == other.col
        )

    def __hash__(self):
        return hash((self.row, self.col))


class HeightmapPoint:
    def __init__(self, coord: Coordinate, height: str, max_row: int, max_col: int):
        self.coord = coord
        self.height = int(height)
        self.risk = int(height) + 1
        self.max_row = max_row
        self.max_col = max_col
        self.neighbors = self.find_neighbors()

    def __repr__(self):
        return f'HeightmapPoint(coord={self.coord}, height={self.height}, max_row={self.max_row}, max_col={self.max_col})'

    def find_neighbors(self):
        points = [
            Coordinate(self.coord.row + 1, self.coord.col),
            Coordinate(self.coord.row - 1, self.coord.col),
            Coordinate(self.coord.row, self.coord.col - 1),
            Coordinate(self.coord.row, self.coord.col + 1),
        ]

        return [n for n in points if ((0 <= n.row < self.max_row) and (0 <= n.col < self.max_col))]


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> Dict[Coordinate, HeightmapPoint]:
    lines = text.strip().split()
    max_row = len(lines)
    max_col = len(lines[0])

    heightmaps = {}

    for row, line in enumerate(lines):
        for col, num in enumerate(line):
            coords = Coordinate(row, col)
            point_info = HeightmapPoint(coords, num, max_row=max_row, max_col=max_col)
            heightmaps[coords] = point_info
    return heightmaps


def find_low_points(heightmaps: Dict[Coordinate, HeightmapPoint]) -> List[Coordinate]:
    low_points = []
    for point_coords, info in heightmaps.items():
        neighbor_values = [heightmaps[coords].height for coords in info.neighbors]
        if all(info.height < value for value in neighbor_values):
            low_points.append(point_coords)
    return low_points


def find_basin(
    low_point: Coordinate, heightmaps: Dict[Coordinate, HeightmapPoint]
) -> List[Coordinate]:
    basin_points = [low_point]
    to_check = set(heightmaps[low_point].neighbors)
    checked = {low_point}

    while to_check:
        point = to_check.pop()
        checked.update([point])
        if heightmaps[point].height < 9:
            basin_points.append(point)
            neighbors = heightmaps[point].neighbors
            to_check.update([n for n in neighbors if n not in checked])
    return basin_points


def solve_part1(input_: str) -> int:
    all_points = parse_input(input_)
    low_points = find_low_points(all_points)
    return sum([all_points[coords].risk for coords in low_points])


def solve_part2(input_: str) -> int:
    all_points = parse_input(input_)
    low_points = find_low_points(all_points)
    basin_sizes = [len(find_basin(low_point, all_points)) for low_point in low_points]

    return prod(sorted(basin_sizes, reverse=True)[:3])


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
