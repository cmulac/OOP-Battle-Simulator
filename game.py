from goblin import Goblin
from hero import Hero


ARENA_NAME = "The desolte wasteland"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")
    Bob= Hero("Bob")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    Scribble = Goblin("Scribble")
    
    print(f"{Scribble.name} enters the arena with {Scribble.health} health.")
    
    print("But no hero has answered the call... yet.")

    print(f"{Bob.name} has answered the call")

    BobsAttack = Bob.attack()
    goblin.take_damage(BobsAttack)
    ScribbleAttack = Scribble.attack()
    Bob.take_damage(ScribbleAttack)




if __name__ == "__main__":
    main()
