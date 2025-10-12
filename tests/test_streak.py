import sys
import os
import pytest

# Add the root directory to the Python path to allow for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test a list with multiple streaks, ensuring the longest one is returned."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_positive_numbers():
    """Test a list containing only positive numbers."""
    assert longest_positive_streak([1, 1, 1, 5, 2]) == 5

def test_zeros_and_negative_numbers():
    """Test a list with only zeros and negative numbers, expecting a streak of 0."""
    assert longest_positive_streak([0, -1, -5, 0, -10]) == 0

def test_single_element_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_element_zero():
    """Test a list with a single zero."""
    assert longest_positive_streak([0]) == 0

def test_single_element_negative():
    """Test a list with a single negative number."""
    assert longest_positive_streak([-5]) == 0

def test_streak_at_the_end():
    """Test a list where the longest streak is at the very end."""
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4, 5]) == 5