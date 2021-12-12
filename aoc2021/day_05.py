import re
from collections import Counter, namedtuple
from pathlib import Path
from typing import List, NamedTuple, Tuple

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202105_input.txt'

Point = namedtuple('Point', ['x', 'y'])


class Vent(NamedTuple):
    point1: Point
    point2: Point


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_line_list(text: str) -> List[Vent]:
    raw_digits = re.findall(r'(\d*),(\d*) -> (\d*),(\d*)', text)
    points = [
        Vent(Point(int(x1), int(y1)), Point(int(x2), int(y2))) for x1, y1, x2, y2 in raw_digits
    ]
    return points


def is_horizontal_or_vertical(vent: Vent) -> bool:
    point1, point2 = vent
    if point1.x == point2.x or point1.y == point2.y:
        return True
    else:
        return False


def return_vent_points(vent: Vent) -> List[Point]:
    point1, point2 = vent
    points = []
    diff = Point(point2.x - point1.x, point2.y - point1.y)
    if diff.x and diff.y:
        step_x = -1 if diff.x < 0 else 1
        step_y = -1 if diff.y < 0 else 1
        for delta_x, delta_y in zip(
            range(0, diff.x + step_x, step_x), range(0, diff.y + step_y, step_y)
        ):
            points.append(Point(point1.x + delta_x, point1.y + delta_y))
    elif diff.x:
        step = -1 if diff.x < 0 else 1
        for dx in range(0, diff.x + step, step):
            points.append(Point(point1.x + dx, point1.y))
    else:
        step = -1 if diff.y < 0 else 1
        for dy in range(0, diff.y + step, step):
            points.append(Point(point1.x, point1.y + dy))
    return points


def count_vent_overlaps(vent_list):
    points = Counter()
    for vent in vent_list:
        points.update(return_vent_points(vent))
    return points


def solve_part1(input_: str) -> int:
    vents = parse_line_list(input_)
    vents = [vent for vent in vents if is_horizontal_or_vertical(vent)]
    point_counts = count_vent_overlaps(vents)
    return len([point for point, count in point_counts.items() if count >= 2])


def solve_part2(input_):
    vents = parse_line_list(input_)
    point_counts = count_vent_overlaps(vents)
    return len([point for point, count in point_counts.items() if count >= 2])


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
