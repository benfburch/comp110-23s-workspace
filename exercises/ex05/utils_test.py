"""Test fucntions for utils."""

__author__: str = "730563626"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_evens_remainder_mod() -> None:
    """Tests only_evens by adding values of list and using % to see if = to 0."""
    test_list: list[int] = only_evens([2, 3, 6, 77])
    assert sum(test_list) % 2 == 0


def test_evens() -> None:
    """Gives a list of values and retuns them."""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_even_empty() -> None:
    """Gives empty list and returns it."""
    assert only_evens([]) == []


def test_sub_basic1() -> None:
    """Generates list between start idx and end idx - 1."""
    assert sub([1, 2, 3, 4, 5, 6, 7], 2, 6) == [3, 4, 5, 6]


def test_sub_invalid_idx_values() -> None:
    """Generates list between start idx and end idx - 1 where the idx's are out of range."""
    assert sub([20, 30, 50, 70, 90, 900, 40], -3, 20) == [20, 30, 50, 70, 90, 900, 40]


def test_sub_empty_list() -> None:
    """Generates empty list with sub program."""
    assert sub([], 2, 4) == []


def test_concat_basic() -> None:
    """Generates a comnbined new list, 1st list before 2nd list."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_negatives() -> None:
    """Generates a comnbined new list, 1st list before 2nd list, with negatives in the lists."""
    assert concat([-6, -5, 7], [9, -1, 7]) == [-6, -5, 7, 9, -1, 7]


def test_concat_with_two_empty() -> None:
    """Makes a combined list with two empty lists."""
    assert concat([], []) == []