"""example function for unit tests."""

def sum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    sum_total: float = 0.0
    for value in range(0, len(xs)):
        sum_total += xs[value] 
    return sum_total

sum([1.0, 5.0, 4.0])