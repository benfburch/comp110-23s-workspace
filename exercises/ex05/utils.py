"""Utils for ex05."""

__author__: str = "730563626"

a_list: list[int] = [10, 20, 30, 40]


def only_evens(i_list: list[int]) -> list:
    """Returns a list of only the even inputs."""
    idx: int = 0
    e_list: list[int] = list()
    while len(i_list) > idx:
        if i_list[idx] % 2 == 0: 
            e_list.append(i_list[idx])
            idx += 1
        else:
            idx += 1
    return e_list


def concat(list1: list[int], list2: list[int]) -> list:
    """Generates a comnbined new list, 1st list before 2nd list."""
    new: list[int] = list()
    idx: int = 0
    while idx < len(list1):
        new.append(list1[idx])
        idx += 1
    idx = 0
    while idx < len(list2):
        new.append(list2[idx])
        idx += 1
    return new


def sub(s_list: list[int], start_idx: int, end_idx: int) -> list:
    """Generates list between start idx and end idx - 1."""
    idx: int = 0
    alt_end: int = 0
    list_s: list[int] = list()
    if start_idx > idx:
        idx = start_idx
    if len(s_list) > end_idx:
        alt_end = end_idx - 1
    else: 
        alt_end = len(s_list) - 1
    while idx <= alt_end:
        list_s.append(s_list[idx])
        idx += 1
    return list_s