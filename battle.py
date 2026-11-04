
from character import Character


class Battle:
    """Represents a Battle in the RPG"""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Initialise the Character

        Args:
            hero (Character): The hero character
            enemy (Character): The enemy character
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """
        Plays a round where the hero attacks the enemy,
        and, if still alive, the enemy attacks the hero
        """
        self.hero.attack(self.enemy)
        print(f"{self.enemy.name} has {self.enemy.hp} hp remaining")
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)
            print(f"{self.hero.name} has {self.hero.hp} hp remaining")

    def simulate_battle(self) -> None:
        """Plays round until either the hero or the enemy is dead"""
        while (self.hero.is_alive) and (self.enemy.is_alive):
            self.play_round()
        if not self.hero.is_alive:
            print(f"{self.hero.name} has died")
        elif not self.enemy.is_alive:
            print(f"{self.enemy.name} has died")
        
