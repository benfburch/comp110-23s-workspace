"""Dictionary file."""

__author__: str = "730563626"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values."""
    new_d: dict[str, str] = dict()
    for key in d: 
        if d[key] in new_d:
            raise KeyError("Duplicate key")
        new_d[d[key]] = key
    return new_d


def count(lis: list[str]) -> dict[str, int]:
    """Gives list and returns dict with value and # of times it appeared in the list."""
    d: dict[str, int] = dict()
    for name in lis:
        if name in d:
            d[name] += 1
        if name not in d:
            d[name] = 1
    return d


def favorite_color(d: dict[str, str]) -> str:
    """Takes a dict of names and favorite colors and returns the most popular color."""
    l: list[str] = list()
    for key in d:
        l.append(d[key])
    di: dict[str, int] = count(l)
    most_pop: str = l[0]
    for key in di:
        if di[key] > di[most_pop]:
            most_pop = key
    return most_pop