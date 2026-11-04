import random

class Dice:
    """Represents a dice"""

    def __init__(self, sides: int = 6) -> None:
        """
        Initialise the Dice

        Arg:
            sides: number of sides on the dice (default = 6)
        """
        self.sides = max(sides, 2)

    def roll(self) -> int:
        """Rolls the dice"""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Representation of dice object"""
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Rolls a d20 by calling roll()"""
        d20 = Dice(sides=20)
        return d20.roll()
    