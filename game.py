from goblin import Goblin
from hero import Hero
from boss import Boss


ARENA_NAME = "The desolte wasteland"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(hero_damage)

    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")
    Bob= Hero("Bob")
    boss= Boss("Super Mega Boss")


    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    Scribble = Goblin("Scribble")
    
    print(f"{Scribble.name} enters the arena with {Scribble.health} health.")
    
    print("But no hero has answered the call... yet.")

    print(f"{Bob.name} has answered the call")

    battle(Bob, goblin)




if __name__ == "__main__":
    main()
