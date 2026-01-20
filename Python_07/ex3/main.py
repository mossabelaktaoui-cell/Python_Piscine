from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy 


def main() -> None:
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print("Available types: ", end='')
    print(factory.create_themed_deck(12))

    print("\nSimulating aggressive turn...")


main()