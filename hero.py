import random

class Hero:
    """The hero blueprint will be implemented later in the project."""
    def __init__(self, name):
        self.name=name
        self.health = 125
        self.attack_power = 10
        self.armor = 3
        self.criticalHit = 5

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        damage = damage - self.armor + random.randint(0, self.criticalHit)
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0
