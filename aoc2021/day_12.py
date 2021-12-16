from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Dict, List

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202112_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> Dict[str, List[str]]:
    nodes = defaultdict(list)
    for line in text.strip().split('\n'):
        left, right = line.split('-')
        if right != 'start' and left != 'end':
            nodes[left].append(right)
        if left != 'start' and right != 'end':
            nodes[right].append(left)
    return nodes


def is_small_cave(cave_name: str) -> bool:
    if cave_name == 'start' or cave_name == 'end':
        return False
    return cave_name.lower() == cave_name


def visit_cave(cave_name: str, path_str: str) -> bool:
    small_caves_visited = Counter([cave for cave in path_str.split('-') if is_small_cave(cave)])
    if is_small_cave(cave_name):
        if any([x >= 2 for x in small_caves_visited.values()]) and cave_name in small_caves_visited:
            return False
        else:
            return True
    else:
        return True


def find_paths(cave_map: Dict[str, List[str]]) -> List[str]:
    queue = deque(['start'])
    complete_paths = []

    while queue:
        node_str = queue.popleft()
        node = node_str.split('-')[-1]
        if node == 'end':
            complete_paths.append(node_str)
        else:
            queue.extend(
                [
                    f'{node_str}-{child}'
                    for child in cave_map[node]
                    if (not is_small_cave(child)) or (child not in node_str)
                ]
            )

    return complete_paths


def find_paths_again(cave_map: Dict[str, List[str]]) -> List[str]:
    queue = deque(['start'])
    complete_paths = []

    while queue:
        node_str = queue.popleft()
        node = node_str.split('-')[-1]
        if node == 'end':
            complete_paths.append(node_str)
        else:
            queue.extend(
                [f'{node_str}-{child}' for child in cave_map[node] if visit_cave(child, node_str)]
            )
    return complete_paths


def solve_part1(input_: str) -> int:
    cave_map = parse_input(input_)
    paths = find_paths(cave_map)
    return len(paths)


def solve_part2(input_: str) -> int:
    cave_map = parse_input(input_)
    paths = find_paths_again(cave_map)
    # print('\n'.join(sorted([x.replace('-', ',') for x in paths])))
    return len(paths)


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
