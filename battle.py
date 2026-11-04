
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

    def play_round(self):
        self.hero.attack(self.enemy)
        if self.enemy.is_alive()==True:
            self.enemy.attack(self.hero)

    def simulate_battle(self):
        while self.hero.is_alive()==True and self.enemy.is_alive()==True:
            self.play_round()