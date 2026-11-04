
class Weapon:

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            damage_dice (class): Which dice that should be used for damage calculations
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Rolls a dice for damage"""
        return self.damage_dice.roll()
