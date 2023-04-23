"""File to define Fish class."""

__author__: str = "730563626"


class Fish:
    """Fish class."""

    age: int

    def __init__(self):
        """Init."""
        self.age = 0
        return None
    
    def one_day(self):
        """One day."""
        self.age += 1
        return None