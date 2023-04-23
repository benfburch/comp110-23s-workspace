"""File to define River class."""

__author__: str = "730563626"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Da riva."""
    
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int): 
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check dem IDs."""
        surviving_bears: list[Bear] = []
        surviving_fish: list[Fish] = []
        for x in self.bears:
            if x.age <= 5:
                surviving_bears.append(x)
        for x in self.fish:
            if x.age <= 3:
                surviving_fish.append(x)
        self.bears = surviving_bears
        self.fish = surviving_fish
        return None

    def remove_fish(self, amount: int) -> None:
        """Remove fishies."""
        for x in range(0, amount):
            self.fish.pop(x)
        return None

    def bears_eating(self):
        """Bears eat."""
        for x in self.bears:
            if len(self.fish) >= 5:
                x.eat(3)         
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Checks bears hunger and kills hungry bears."""
        new_list: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_list.append(bear)
        self.bears = new_list
        return None
        
    def repopulate_fish(self):
        """Repop fish."""
        for x in range(0, (len(self.fish) // 2 * 4)):
            self.fish.append(Fish)
        return None
    
    def repopulate_bears(self):
        """Repop bears."""
        for x in range(0, (len(self.bears) // 2)):
            self.bears.append(Bear)
        return None
    
    def view_river(self):
        """Shows river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self): 
        """One week."""
        idx: int = 0
        while idx < 7:
            self.one_river_day()
            idx += 1
        return None