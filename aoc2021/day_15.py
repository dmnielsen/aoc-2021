from collections import namedtuple
from pathlib import Path
from typing import Dict, List, Set, Tuple

import numpy as np

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202115_input.txt'

Coords = namedtuple('Coords', ['x', 'y'])


class Node:
    def __init__(self, coords: Coords, risk: int, neighbors: List[Coords]):
        self.coords = coords
        self.risk = risk
        self.neighbors = neighbors

        self._cost = float('inf')
        self._parent = None

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> Tuple[Dict[Coords, Node], Coords]:
    text = text.split()
    max_rows, max_cols = len(text), len(text[0])

    grid_points = set((x, y) for x in range(max_cols) for y in range(max_rows))

    grid = {}

    for y, row in enumerate(text):
        for x, value in enumerate(row):
            coords = Coords(x, y)
            neighbors = [
                point
                for point in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                if point in grid_points
            ]
            node = Node(coords, int(value), neighbors)

            grid[coords] = node

    # set starting point to have zero cost and zero risk
    grid[Coords(0, 0)].cost = 0
    grid[Coords(0, 0)].risk = 0

    # remove neighbors from ending coordinate
    grid[Coords(max_cols - 1, max_rows - 1)].neighbors = []
    return grid, Coords(max_cols - 1, max_rows - 1)


def create_full_grid(text: str) -> np.ndarray:

    text = text.split()
    max_rows, max_cols = len(text), len(text[0])
    base_grid = np.array([int(xx) for x in text for xx in x]).reshape((max_rows, max_cols))

    # This is a very silly thing
    grid1 = np.where(base_grid + 1 > 9, 1, base_grid + 1)
    grid2 = np.where(grid1 + 1 > 9, 1, grid1 + 1)
    grid3 = np.where(grid2 + 1 > 9, 1, grid2 + 1)
    grid4 = np.where(grid3 + 1 > 9, 1, grid3 + 1)
    grid5 = np.where(grid4 + 1 > 9, 1, grid4 + 1)
    grid6 = np.where(grid5 + 1 > 9, 1, grid5 + 1)
    grid7 = np.where(grid6 + 1 > 9, 1, grid6 + 1)
    grid8 = np.where(grid7 + 1 > 9, 1, grid7 + 1)

    rows = [
        np.concatenate([base_grid, grid1, grid2, grid3, grid4], axis=1),
        np.concatenate((grid1, grid2, grid3, grid4, grid5), axis=1),
        np.concatenate([grid2, grid3, grid4, grid5, grid6], axis=1),
        np.concatenate([grid3, grid4, grid5, grid6, grid7], axis=1),
        np.concatenate([grid4, grid5, grid6, grid7, grid8], axis=1),
    ]

    return np.concatenate(rows, axis=0)


def get_lowest_cost_node(grid: Dict[Coords, int], processed: Set) -> Coords:
    for coords, cost in sorted(grid.items(), key=lambda x: x[1]):
        if coords not in processed:
            return coords
    return None


def solve_part1(input_: str) -> int:
    grid, target = parse_input(input_)

    processed = set()
    unprocessed_with_cost = {Coords(0, 0): 0}

    node_coords = get_lowest_cost_node(unprocessed_with_cost, processed)
    while node_coords is not None:
        if node_coords == target:
            return grid[node_coords].cost

        node_info = grid[node_coords]
        for n in node_info.neighbors:
            new_cost = node_info.cost + grid[n].risk
            if new_cost < grid[n].cost:
                grid[n].cost = new_cost
                grid[n].parent = node_coords
                if n not in processed:
                    unprocessed_with_cost[n] = new_cost
        processed.update([node_coords])
        node_coords = get_lowest_cost_node(unprocessed_with_cost, processed)
    return grid[target].cost


def get_neighbors(coords: Coords, target_coords: Coords) -> List[Coords]:
    x, y = coords
    default_neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    if (0 < x < target_coords.x) and (0 < y < target_coords.y):
        return default_neighbors
    else:
        return [
            (xx, yy)
            for xx, yy in default_neighbors
            if (0 <= xx <= target_coords.x) and (0 <= yy <= target_coords.y)
        ]


def solve_part2(input_: str) -> int:
    grid = create_full_grid(input_)
    costs = np.ones_like(grid) * np.inf
    costs[Coords(0, 0)] = 0
    target = Coords(grid.shape[0] - 1, grid.shape[1] - 1)
    processed = set()
    unprocessed_with_cost = {Coords(0, 0): 0}

    node_coords = get_lowest_cost_node(unprocessed_with_cost, processed)
    while node_coords is not None:
        del unprocessed_with_cost[node_coords]
        if node_coords == target:
            return costs[node_coords]
        for n in get_neighbors(node_coords, target):
            new_cost = costs[node_coords] + grid[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                if n not in processed:
                    unprocessed_with_cost[n] = new_cost
        processed.update([node_coords])
        node_coords = get_lowest_cost_node(unprocessed_with_cost, processed)

    return int(costs[target])


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    print('finished 1')
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
