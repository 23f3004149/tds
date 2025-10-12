import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test that the function returns the longest of multiple streaks."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_zeros_and_negatives():
    """Test that zeros and negative numbers correctly break streaks."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, -1, 6]) == 3
    assert longest_positive_streak([-1, -2, -3]) == 0

def test_all_positive():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_element_list():
    """Test lists with a single element."""
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([0]) == 0
    assert longest_positive_streak([-1]) == 0

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([0, -1, -5, 0]) == 0

def test_streaks_at_beginning_and_end():
    """Test streaks at the beginning and end of the list."""
    assert longest_positive_streak([1, 2, 3, -1, 0, 5, 6]) == 3
    assert longest_positive_streak([1, 2, -1, 0, 5, 6, 7, 8]) == 4