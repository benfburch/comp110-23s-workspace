"""Dictionary tests file."""

__author__: str = "730563626"


from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import count
from exercises.ex07.dictionary import favorite_color
import pytest


def test_invert() -> None:
    """Checks with basic list of letters."""
    test_dict: dict[str, str] = invert({"a": "z", "b": "y", "c": "x"})
    assert test_dict == {"z": "a", "y": "b", "x": "c"}


def test_invert_nums() -> None:
    """Checks with basic list of letters and numbers as strings."""
    test_dict: dict[str, str] = invert({"a": "1", "2": "y", "4": "x"})
    assert test_dict == {"1": "a", "y": "2", "x": "4"}


def test_invert_key_error() -> None:
    """Checks to see if the KeyError was raised."""
    with pytest.raises(KeyError):
        my_dictionary = {"a": "z", "b": "y", "c": "z"}
        invert(my_dictionary)


def test_count() -> None:
    """Checks with basic list."""
    test_list: list[str] = ["blue", "red", "blue"]
    assert count(test_list) == {"blue": 2, "red": 1}


def test_count_2() -> None:
    """Checks with basic list."""
    test_list: list[str] = ["blue", "red", "yellow"]
    assert count(test_list) == {"blue": 1, "red": 1, "yellow": 1}


def test_count_dups() -> None:
    """Checks when there are multiple duplicate colors."""
    test_list: list[str] = ["blue", "red", "blue", "blue", "red", "blue", "yellow"]
    assert count(test_list) == {"blue": 4, "red": 2, "yellow": 1}


def test_favorite_color() -> None:
    """Checks with basic dict of names and colors."""
    test_dict: dict[str, str] = {"John": "blue", "Mark": "yellow", "Chris": "yellow"}
    assert favorite_color(test_dict) == "yellow"


def test_favorite_color_no_fav() -> None:
    """Checks when there is no favorite color to make sure it outputs the first color in the dict."""
    test_dict: dict[str, str] = {"John": "red", "Mark": "yellow", "Chris": "blue"}
    assert favorite_color(test_dict) == "red"


def test_favorite_color2() -> None:
    """Checks with basic dict of names and colors."""
    test_dict: dict[str, str] = {"John": "blue", "Mark": "red", "Chris": "yellow", "Ben": "blue"}
    assert favorite_color(test_dict) == "blue"