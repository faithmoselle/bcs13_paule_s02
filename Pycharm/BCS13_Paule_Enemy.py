class Enemy:
    def __init__(self, hero, level, skill, dam):
        self.hero = hero
        self.level = level
        self.skill = skill
        self.damage = dam

    def display(self):
        return f"Your enemy: {self.hero}\n\tLevel: {self.level}\n\tSkill: {self.skill}\n\tDamage: {self.damage}"

hero1 = Enemy("Captain America", "5", "Shield", "80% Damage")
hero2 = Enemy("Thor", "80", "Lightning Hammer", "80% Damage")
hero3 = Enemy("Black Widow", "100", "Trained Assassin", "100% Damage")

while True:
    enemy = int(input("Marvel Universe\n Welcome Iron Man, kindly chose your enemy!\n\tEnemy 1: Captain America\n\tEnemy "
                      "2: Thor\n\tEnemy 3: Black Widow\n\nYour chosen enemy number: "))
    if enemy == 1:
        print(hero1.display())
        break
    elif enemy == 2:
        print(hero2.display())
        break
    elif enemy == 3:
        print(hero3.display())
        break
    else:
        print("Please enter the number of your chosen enemy 1-3:")