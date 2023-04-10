"""Function name zip."""

__author__: str = "730563626"

def zip(list_str: list[str], list_int: list[int]) -> dict[str, int]:
    """Returns a dict."""
    fav_sports: dict[str, int] = dict() 
    if len(list_str) != len(list_int):
        return fav_sports
    idx: int = 0
    for key in list_str:
        fav_sports[key] = list_int[idx]
        idx += 1
    return fav_sports


print(zip(["soccer", "basketball", "baseball"], [3, 5, 6]))