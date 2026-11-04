
class Battle:

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
        if self.enemy.is_alive()==True:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Plays round until either the hero or the enemy is dead"""
        while self.hero.is_alive()==True and self.enemy.is_alive()==True:
            self.play_round()
        