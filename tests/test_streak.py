# tests/test_streak.py

import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 1, 1]) == 3

def test_mixed_values():
    nums = [2, 3, -1, 5, 6, 7, 0, 4]
    assert longest_positive_streak(nums) == 3

def test_multiple_streaks():
    nums = [1, 2, -1, 3, 4, 0, 5, 6, 7, -2]
    assert longest_positive_streak(nums) == 3

def test_zeros_and_negatives():
    nums = [0, -1, 2, 3, -5, 1]
    assert longest_positive_streak(nums) == 2
