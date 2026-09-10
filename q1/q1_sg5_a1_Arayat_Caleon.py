class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def take_damage(self, dmg):
        self.hp -= dmg

hero1 = Hero("Arthur", 100)
hero2 = Hero("Morgana", 100)
print(f"{hero1.name}'s HP: {hero1.hp}")
print(f"{hero2.name}'s HP: {hero2.hp}")
hero1.take_damage(10)
print(f"{hero1.name}'s HP: {hero1.hp}")
print(f"{hero2.name}'s HP: {hero2.hp}")