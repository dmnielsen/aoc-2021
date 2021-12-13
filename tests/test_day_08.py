import pytest

from aoc2021 import day_08 as day


@pytest.fixture
def mock_input():
    text = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
    return text


def test_build_decoder():
    input_ = [
        'acedgfb',
        'cdfbe',
        'gcdfa',
        'fbcad',
        'dab',
        'cefabd',
        'cdfgeb',
        'eafb',
        'cagedb',
        'ab',
    ]
    expected = [
        {'a', 'b', 'c', 'd', 'e', 'g'},
        {'a', 'b'},
        {'a', 'c', 'd', 'f', 'g'},
        {'a', 'b', 'c', 'd', 'f'},
        {'a', 'b', 'e', 'f'},
        {'b', 'c', 'd', 'e', 'f'},
        {'b', 'c', 'd', 'e', 'f', 'g'},
        {'a', 'b', 'd'},
        {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        {'a', 'b', 'c', 'd', 'e', 'f'},
    ]
    result = day.build_decoder(input_)
    assert result == expected


def test_solve_part1(mock_input):
    expected = 26
    result = day.solve_part1(mock_input)
    assert expected == result


def test_solve_part2(mock_input):
    expected = 61229
    result = day.solve_part2(mock_input)
    assert expected == result
