from ex0.CreatureCard import CreatureCard

def main():
    card1 = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5, "Creature summoned to battlefield")
    card2 = CreatureCard("Goblin Warrior", 3, "Common", 2, 4, "Creature summoned to battlefield")


    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    print(card1.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    playable = card1.is_playable(6)
    print(f"Playable: {playable}")
    if playable:
        print("Play result", end='')
    print(card1.play({}))

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result: ", end='')
    print(card1.attack_target(card2))

    print("\nTesting with insufficient mana (3 available):")
    playable = card1.is_playable(3)
    print(f"Playable: {playable}")

    print("\nAbstract pattern successfully demonstrated!")

if __name__ == "__main__":
    main()