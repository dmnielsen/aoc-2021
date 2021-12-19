import pytest

from aoc2021 import day_16 as day


@pytest.fixture
def mock_input():
    return


@pytest.mark.parametrize(
    'hex_str, expected',
    [
        ('D2FE28', '110100101111111000101000'),
        ('38006F45291200', '00111000000000000110111101000101001010010001001000000000'),
        ('EE00D40C823060', '11101110000000001101010000001100100000100011000001100000')

    ]

)
def text_hex_to_binary(hex_str, expected):
    result = day.hex_to_binary(hex_str)
    assert result == expected


@pytest.mark.parametrize(
    'message, expected',
    [
        ('D2FE28', 6),
        ('38006F45291200', 9),
        ('EE00D40C823060', 14),
        ('8A004A801A8002F478', 16),
        ('620080001611562C8802118E34', 12),
        ('C0015000016115A2E0802F182340', 23),
        ('A0016C880162017C3686B18A3D4780', 31)
     ]
)
def test_solve_part1(message, expected):
    result = day.solve_part1(message)
    assert expected == result


def test_solve_part2(mock_input):
    expected = None
    result = day.solve_part2(mock_input)
    assert expected == result
