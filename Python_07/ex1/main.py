from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    deck = Deck()

    card1 = SpellCard(name="Lightning Bolt",
                      cost=3,
                      rarity="Common",
                      effect_type="damage")

    card2 = ArtifactCard(name="Mana Crystal",
                         cost=2,
                         rarity="Common",
                         durability=5,
                         effect="Permanent: +1 mana per turn")

    card3 = CreatureCard(name="Fire Dragon",
                         cost=5,
                         rarity="Legendary",
                         attack=7,
                         health=5,
                         effect="Creature summoned to battlefield")

    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    for card in (card1, card2, card3):
        deck.add_card(card)

    print("Deck stats:", end='')
    print(deck.get_deck_stats())

    print("\nDrawing and playing cards:")

    print("\nDrew: ", end='')
    print(f"{card1.name} ({card1.type})")
    print("Play result:", end='')
    print(card1.play({}))

    print("\nDrew: ", end='')
    print(f"{card2.name} ({card2.type})")
    print("Play result:", end='')
    print(card2.play({}))

    print("\nDrew: ", end='')
    print(f"{card3.name} ({card3.type})")
    print("Play result:", end='')
    print(card3.play({}))

    print("\nPolymorphism in action: Same interface, "
          "different card behaviors!")


if __name__ == "__main__":
    main()
