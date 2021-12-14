import pytest

from aoc2021 import day_10 as day


@pytest.fixture
def mock_input():
    text = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
    return text


@pytest.mark.parametrize('line, expected', [('{([(<{}[<>[]}>{[]{[(<()>', '}'),
                                            ('[[<[([]))<([[{}[[()]]]', ')'),
                                            ('[{[{({}]{}}([{[{{{}}([]', ']'),
                                            ('[<(<(<(<{}))><([]([]()', ')'),
                                            ('<{([([[(<>()){}]>(<<{{', '>')])
def test_find_corrupted_line(line, expected):
    result = day.find_corrupted_line(line)
    assert result == expected


@pytest.mark.parametrize('line, expected', [('[({(<(())[]>[[{[]{<()<>>', '}}]])})]'),
                                            ('[(()[<>])]({[<{<<[]>>(', ')}>]})'),
                                            ('(((({<>}<{<{<>}{[]{[]{}', '}}>}>))))'),
                                            ('{<[[]]>}<{[{[{[]{()[[[]', ']]}}]}]}>'),
                                            ('<{([{{}}[<[[[<>{}]]]>[]]', '])}>')])
def test_find_incomplete_chunks(line, expected):
    result = day.correct_incomplete_chunks(line)
    assert result == expected


@pytest.mark.parametrize('line, expected', [
('}}]])})]', 288957),
(')}>]})', 5566),
('}}>}>))))', 1480781),
(']]}}]}]}>', 995444),
('])}>', 294)
])
def test_score_completion(line, expected):
    result = day.score_completion(line)
    assert result == expected


def test_solve_part1(mock_input):
    expected = 26397
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 288957
    result = day.solve_part2(mock_input)
    assert expected == result
