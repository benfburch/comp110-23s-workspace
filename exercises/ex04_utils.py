"""list utility functions."""

__author__: str = "730563626"


def all(int_list: list[int], all_int: int) -> bool: 
    """Returns a bool indicating whether all the ints in the list are the same as the given int."""
    all_idx: int = 0
    if len(int_list) == 0:
        return False
    while len(int_list) > all_idx: 
        if int_list[all_idx] == all_int: 
            all_idx += 1
        else:
            return False
    return True 


def max(int_list: list[int]) -> int: 
    """Returns largest int."""
    max_idx: int = 1
    high_value: int = int_list[0] 
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    while len(int_list) > max_idx:
        if high_value < int_list[max_idx]:
            high_value = int_list[max_idx]
        max_idx += 1 
    return high_value


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Returns True if every element at every index is equal."""
    equal_idx: int = 0
    if len(list_1) != len(list_2):
        return False
    while equal_idx < len(list_1):
        if list_1[equal_idx] == list_2[equal_idx]:
            equal_idx += 1
        else:
            return False
    return True