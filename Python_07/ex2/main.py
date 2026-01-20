from ex2.EliteCard import EliteCard


def main() -> None:
    card = EliteCard("Arcane Warrior", 6, "common")

    combat_result = card.get_combat_stats()
    magic_result = card.get_magic_stats()
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")

    print(f"Attack result: ", end='')
    print(combat_result['attack'])
    print(f"Defend result: ", end='')
    print(combat_result['defense'])

    print("\nMagic phase:")

    print("Spell cast: ", end='')
    print(magic_result['spells_cast'])
    print("Mana channeled: ", end='')
    print(magic_result['mana_channeled'])

    print("\nMultiple interfaces implementation successful!")


if __name__ == "__main__":
    main()
