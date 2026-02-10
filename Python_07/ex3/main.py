from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    deck_info = factory.create_themed_deck(4)
    available_types = {key: value for key, value
                       in deck_info.items() if key != 'deck'}
    print(f"Available types: {available_types}")

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("\nSimulating aggressive turn...")

    hand_display = [card.name for card
                    in engine.players_data['Player 1']['hand']]
    print(f"Hand: {hand_display}")

    print("\nTurn execution:")
    turn_result = engine.simulate_turn()

    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {turn_result}")

    print("\nGame Report:")
    status = engine.get_engine_status()

    print(status)

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
