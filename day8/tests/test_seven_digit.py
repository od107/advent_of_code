from day8.seven_digit import *


def test_part1():
    assert seven_digit("day8/data/test_data") == 26
    assert seven_digit("day8/data/real_data") == 532


def test_part2():
    assert total_output("day8/data/test_data") == 61229
    assert total_output("day8/data/real_data") == 1011284