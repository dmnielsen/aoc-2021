import pytest

from aoc2021 import day_18 as day
from aoc2021.day_18 import SnailNumber


@pytest.fixture
def mock_input():
    text = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
    return text


@pytest.mark.parametrize(
    'text, expected',
    [('[1,2]', SnailNumber(1, 2)),
     ('[[1,2],3]', SnailNumber(SnailNumber(1, 2), 3)),
     ('[9,[8,7]]', SnailNumber(9, SnailNumber(8, 7))),
     ('[[1,9],[8,5]]', SnailNumber(SnailNumber(1, 9), SnailNumber(8, 5)))
     ]
)
def test_parse_written_snail_number(text, expected):
    result = day.parse_written_snail_number(text)
    assert result == expected
    pass


def test_add_super_simple():
    sn1 = SnailNumber(1, 2)
    sn2 = SnailNumber(SnailNumber(3, 4), 5)
    expected = SnailNumber(SnailNumber(1, 2), SnailNumber(SnailNumber(3, 4), 5))

    result = day.add(sn1, sn2)
    assert result == expected


@pytest.mark.parametrize(
    'in_text, expected',
    [
        ('[[[[[9,8],1],2],3],4]', True),
        ('[7,[6,[5,[4,[3,2]]]]]', True),
        ('[[6,[5,[4,[3,2]]]],1]', True),
        ('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]', True),
        ('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]', True),
        ('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]', True),
        ('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]', True),
        ('[[[[0,7],4],[15,[0,13]]],[1,1]]', False),
        ('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]', False),
        ('[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]', True),
        ('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', False)
    ]
)
def test_must_explode(in_text, expected):
    result = day.parse_written_snail_number(in_text).must_explode()
    assert result == expected


@pytest.mark.parametrize(
    'in_text, expected_text',
    [
        ('[[[[[9,8],1],2],3],4]', '[[[[0,9],2],3],4]'),
        ('[7,[6,[5,[4,[3,2]]]]]', '[7,[6,[5,[7,0]]]]'),
        ('[[6,[5,[4,[3,2]]]],1]', '[[6,[5,[7,0]]],3]'),
        ('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'),
        ('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'),
    ]
)
def test_explode(in_text, expected_text):
    expected = day.parse_written_snail_number(expected_text)
    sn = day.parse_written_snail_number(in_text)
    sn.explode()
    assert sn == expected


@pytest.mark.parametrize(
    'in_text, expected',
    [
        ('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]', False),
        ('[[[[0,7],4],[15,[0,13]]],[1,1]]', True),
        ('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]', True),
        ('[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]', False),
        ('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', False)
    ]
)
def test_msut_split(in_text, expected):
    result = day.parse_written_snail_number(in_text).must_split()
    assert result == expected


@pytest.mark.parametrize(
    'in_text, expected_text',
    [
        # ('[[[[0,7],4],[15,[0,13]]],[1,1]]', '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'),
        ('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]', '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]')
    ]
)
def test_split(in_text, expected_text):
    expected = day.parse_written_snail_number(expected_text)
    sn = day.parse_written_snail_number(in_text)
    sn.split()
    assert sn == expected


def test_reduce():
    expected = day.parse_written_snail_number('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
    sn = day.parse_written_snail_number('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
    sn.reduce()
    assert sn == expected


def test_add():
    text = """[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]"""
    numbers = day.load_snail_numbers(text)
    cur_num = numbers[0]
    for number in numbers[1:]:
        cur_num = day.add(cur_num, number)
        cur_num.reduce()

    expected = day.parse_written_snail_number('[[[[5,0],[7,4]],[5,5]],[6,6]]')
    assert cur_num == expected


def test_add_only_one():
    sn1 = day.parse_written_snail_number('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]')
    sn2 = day.parse_written_snail_number('[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]')
    result = day.add(sn1, sn2)
    result.reduce()
    expected = day.parse_written_snail_number('[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]')
    assert result == expected


def test_add_complex():
    text = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""
    numbers = day.load_snail_numbers(text)
    cur_num = numbers[0]
    for number in numbers[1:]:
        cur_num = day.add(cur_num, number)
        cur_num.reduce()
    expected = day.parse_written_snail_number('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')
    assert cur_num == expected


@pytest.mark.parametrize(
    'in_text, expected',
    [
        ('[[1,2],[[3,4],5]]', 143),
        ('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', 1384),
        ('[[[[1,1],[2,2]],[3,3]],[4,4]]', 445),
        ('[[[[3,0],[5,3]],[4,4]],[5,5]]', 791),
        ('[[[[5,0],[7,4]],[5,5]],[6,6]]', 1137),
        ('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]', 3488)
    ]
)
def test_magnitude_calculation(in_text, expected):
    sn = day.parse_written_snail_number(in_text)
    result = sn.magnitude()
    assert result == expected


def test_solve_part1(mock_input):
    expected = 4140
    result = day.solve_part1(mock_input)
    assert expected == result


@pytest.fixture
def mock_three_pair():
    text = """[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
"""
    return text


def test_solve_part2(mock_three_pair):
    expected = 3993
    result = day.solve_part2(mock_three_pair)
    assert expected == result
