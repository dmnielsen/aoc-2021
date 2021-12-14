from pathlib import Path
from typing import Dict, List

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202111_input.txt'


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


class Octopus:
    def __init__(self, coords: Coordinate, initial_energy: int):
        self.coords = coords
        self.energy = initial_energy
        self.neighbors = None

    def set_neighbors(self, neighbor_list: List[Coordinate]):
        self.neighbors = neighbor_list

    def increment_energy(self) -> bool:
        self.energy += 1
        if self.energy > 9:
            self.energy = 0
            return True
        else:
            return False


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> Dict[Coordinate, Octopus]:
    octopus_map = {}
    for i, row in enumerate(text.strip().split()):
        for j, value in enumerate(row):
            coords = Coordinate(i, j)
            octopus_map[coords] = Octopus(coords, int(value))
    all_points = octopus_map.keys()
    for loc, octopus in octopus_map.items():
        neighbors = find_valid_adjacent_coords(loc, all_points)
        octopus.set_neighbors(neighbors)
    return octopus_map


def find_valid_adjacent_coords(loc: Coordinate, valid_coords: List[Coordinate]):
    adjacent_coords = []
    for i in range(loc.row - 1, loc.row + 2):
        for j in range(loc.col - 1, loc.col + 2):
            point = Coordinate(i, j)
            if (point != loc) and (point in valid_coords):
                adjacent_coords.append(point)
    return adjacent_coords


def take_step(octopus_map: Dict[Coordinate, Octopus]) -> int:
    flashes = 0
    already_flashed = set()
    neighbors_flashed = []
    for coords, octopus in octopus_map.items():
        did_flash = octopus.increment_energy()
        if did_flash:
            flashes += 1
            already_flashed.add(coords)
            neighbors_flashed.extend([n for n in octopus.neighbors if n not in already_flashed])

    # clear out any octopi in neighbors list that have already flashed
    neighbors_flashed = [n for n in neighbors_flashed if n not in already_flashed]

    while neighbors_flashed:
        coords = neighbors_flashed.pop()
        if coords in already_flashed:
            continue
        octopus = octopus_map[coords]
        did_flash = octopus.increment_energy()
        if did_flash:
            flashes += 1
            already_flashed.add(coords)
            neighbors_flashed.extend([n for n in octopus.neighbors if n not in already_flashed])

    return flashes


def print_octopus_map(octopus_map: Dict[Coordinate, Octopus]):
    grid = []
    for i in range(10):
        row = ''
        for j in range(10):
            coords = Coordinate(i, j)
            row += str(octopus_map[coords].energy)
        grid.append(row)
    print('\n'.join(grid))


def solve_part1(input_: str) -> int:
    octopus_map = parse_input(input_)
    flashes = 0

    for i in range(100):
        # print(f'\nStep{i}')
        # print(f'Flashes={flashes}\n')
        # print_octopus_map(octopus_map)
        flashes += take_step(octopus_map)

    return flashes


def solve_part2(input_: str) -> int:
    octopus_map = parse_input(input_)
    all_flashed = False

    i = 1
    while not all_flashed:
        flashes = take_step(octopus_map)
        if flashes == 100:
            return i
        else:
            i += 1


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
