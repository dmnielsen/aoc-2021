from pathlib import Path
from typing import Tuple

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202120_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> Tuple[str, np.ndarray]:
    text = text.strip().split('\n')
    algo = text[0].replace('.', '0').replace('#', '1')

    image = text[2:]
    max_rows, max_cols = len(image), len(image[0])

    image = np.array(['0' if xx == '.' else '1' for x in image for xx in x]).reshape(
        (max_rows, max_cols)
    )

    return algo, image


def pad_image(image: np.ndarray, pad_value) -> np.ndarray:
    return np.pad(image, pad_width=2, mode='constant', constant_values=pad_value)


def enhance_image(image: np.ndarray, algo: str, pad_value: str) -> np.ndarray:
    windows = sliding_window_view(image, (3, 3))
    new_image = np.full_like(image, pad_value)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            new_image[i, j] = algo[int(''.join(windows[i - 1, j - 1].flatten()), 2)]
    return new_image


def solve_part1(input_: str) -> int:
    # breakpoint()
    algo, image = parse_input(input_)
    start_pad_value = algo[int('000000000', 2)]
    end_pad_value = algo[int(start_pad_value * 9, 2)]

    image = pad_image(image, pad_value=end_pad_value)
    new_image = enhance_image(image, algo, pad_value=start_pad_value)

    new_image = pad_image(new_image, pad_value=start_pad_value)
    final_image = enhance_image(new_image, algo, pad_value=end_pad_value)

    return (final_image == '1').sum()


def solve_part2(input_: str):
    algo, image = parse_input(input_)
    start_pad_value = algo[int('000000000', 2)]
    end_pad_value = algo[int(start_pad_value * 9, 2)]

    for i in range(25):
        image = pad_image(image, pad_value=end_pad_value)
        new_image = enhance_image(image, algo, pad_value=start_pad_value)

        new_image = pad_image(new_image, pad_value=start_pad_value)
        image = enhance_image(new_image, algo, pad_value=end_pad_value)

    return (image == '1').sum()


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
