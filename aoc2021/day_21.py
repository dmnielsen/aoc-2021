from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
from typing import Dict, List, Tuple

from aoc2021 import AOC_DIR
from aoc2021.util import print_solutions

INPUT_FILENAME = AOC_DIR / 'inputs' / '202121_input.txt'


def load(filename: Path = INPUT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def parse_input(text: str) -> Tuple[int, int]:
    text = text.split('\n')
    pos1 = int(text[0].split(':')[1])
    pos2 = int(text[1].split(':')[1])
    return pos1, pos2


def take_turn(loc: int, die_rolls: List[int]) -> int:
    loc += sum(die_rolls)
    loc = loc % 10
    if loc == 0:
        loc = 10
    return loc


def solve_part1(input_: str) -> int:
    loc1, loc2 = parse_input(input_)

    game_end_score = 1000
    score1, score2 = 0, 0
    total_rolls = 0
    die_value = 1

    player1_turn = True
    while (score1 < game_end_score) and (score2 < game_end_score):
        rolls = [v % 100 if (v % 100) else 100 for v in range(die_value, die_value + 3)]
        # print(rolls)
        if player1_turn:
            loc1 = take_turn(loc1, rolls)
            score1 += loc1
            # print(f'player 1: score={score1}; loc={loc1}')
            player1_turn = False
        else:
            loc2 = take_turn(loc2, rolls)
            score2 += loc2
            player1_turn = True
            # print(f'player 2: score={score2}; loc={loc2}')
        total_rolls += 3
        die_value = (die_value + 3) % 100
        if die_value == 0:
            die_value = 100

    losing_score = min([score1, score2])
    return losing_score * total_rolls


def build_roll_map():
    roll_map = {}
    for i in range(1, 11):
        roll_map[i] = {k: v if (v := (k + i) % 10) else 10 for k in range(3, 10)}
    return roll_map


def calculate_turns_to_win(positions: Dict[int, Counter], target=21) -> Dict[int, Counter]:

    multiverse_roll = Counter([sum(s) for s in product([1, 2, 3], repeat=3)])
    roll_map = build_roll_map()

    n_turns_in_completed_game = defaultdict(int)
    scores_after_turns_dict = {}
    turns = 1

    while True:
        # print(f'Turn {turns}')
        # print('------')
        next_position = defaultdict(Counter)
        scores_during_this_turn = Counter()
        for roll_value, roll_count in multiverse_roll.items():
            for cur_pos, scores in positions.items():
                new_position = roll_map[cur_pos][roll_value]
                new_scores = defaultdict(Counter)
                for score, count in scores.items():
                    if (p := score + new_position) < target:
                        new_scores[p] = count * roll_count
                    else:
                        n_turns_in_completed_game[turns] += count * roll_count
                    scores_during_this_turn.update({score + new_position: count * roll_count})
                next_position[new_position].update(new_scores)
                # print(next_position)

        positions = next_position
        scores_after_turns_dict[turns] = scores_during_this_turn
        if all(not v for v in positions.values()):
            break
        turns += 1
    return scores_after_turns_dict


def solve_part2(input_: str):
    loc1, loc2 = parse_input(input_)

    target = 21

    # position: Counter(score: count)
    positions1 = {loc1: Counter([0])}
    player1_turns = calculate_turns_to_win(positions1, target=target)

    positions2 = {loc2: Counter([0])}
    player2_turns = calculate_turns_to_win(positions2, target=target)

    player1_wins = 0
    player2_wins = 0
    total_turns = min([len(player1_turns), len(player2_turns)])
    for i in range(2, total_turns + 1):
        for score, count in player1_turns[i].items():
            if score >= 21:
                games_won = sum([c for s, c in player2_turns[i - 1].items() if s < 21])
                player1_wins += games_won * count
        for score, count in player2_turns.items():
            if score >= 21:
                games_won = sum([c for s, c, in player1_turns[i].items() if s < 21])
                player2_wins += games_won * count
    return max([player1_wins, player2_wins])


def main(show_solution: bool = True):
    input_ = load(INPUT_FILENAME)

    result1 = solve_part1(input_)
    result2 = solve_part2(input_)

    if show_solution:
        print_solutions(result1, result2)


if __name__ == '__main__':
    main()
