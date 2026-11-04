
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
        print(f"{self.enemy} has {self.enemy.hp} hp remianing")
        if self.enemy.is_alive()==True:
            self.enemy.attack(self.hero)
            print(f"{self.hero} has {self.hero.hp} hp remianing")

    def simulate_battle(self) -> None:
        """Plays round until either the hero or the enemy is dead"""
        while self.hero.is_alive()==True and self.enemy.is_alive()==True:
            self.play_round()
        if self.hero.is_alive()==False:
            print(f"{self.hero} has died")
        elif self.enemy.is_alive()==False:
            print(f"{self.enemy} has died")
        