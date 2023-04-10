"""Define pizza class"""

class Pizza:

    # attributes
    size: str 
    toppings: int
    gluten_free: bool

    def __init__(self, size_input: str, toppings_input: int, gluten_input: bool):
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gluten_input
        # returns self

    def price(self) -> float:
        """Calculate and return cost of pizza."""
        cost: float = 0.0
        if self.size == "large":
            cost = 6.0
        else:
            cost = 5.0
        cost += .75 * self.toppings
        if self.gluten_free:
            cost += 1.0
        return cost
    
    def add_toppings(self, num_toppings: int) -> None:
        """Add a certain number of toppings."""
        self.toppings += num_toppings