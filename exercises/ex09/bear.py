"""File to define Bear class."""

__author__: str = "730563626"


class Bear:
    """Bear class."""

    age: int 
    hunger_score: int

    def __init__(self):
        """Init."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """One day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Big dawgs gotta eat."""
        self.hunger_score += num_fish
        return None