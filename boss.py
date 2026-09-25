from enemy import Enemy


class Boss(Enemy):
    """A stronger enemy with a powered-up attack."""

    def __init__(self, name):
        super().__init__(name, health=300, attack_power=25)

    def attack(self):
        damage = super().attack()
        bonus_damage = 7
        print(f"{self.name} wipes them out!!!!!!")
        return damage + bonus_damage

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage to their health, but is still standing with {self.health} left")
        super().take_damage(damage)

    

    def intro(self):
        print(f"{self.name} enters the aren to crush the hero")