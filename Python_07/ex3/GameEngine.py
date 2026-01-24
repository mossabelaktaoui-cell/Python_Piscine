from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex1.Deck import Deck
from ex3.FantasyCardFactory import FantasyCardFactory as Fan


class GameEngine:
    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        player1 = factory.create_themed_deck(10)
        player2 = factory.create_themed_deck(10)



class GameEngine:
    players_hand = [[], [], [], [], []]
    deck = None
    battlefield = []
    strategy = None

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:

        deck_data = factory.create_themed_deck(40)

        self.strategy = strategy
        self.deck = deck_data['deck']
        self.deck.shuffle()

        for player_index in range(len(self.players_hand)):
            for _ in range(5):
                self.players_hand[player_index].append(self.deck.draw_card())

        for _ in range(5):
            self.battlefield.append(self.deck.draw_card())

    def simulate_turn(self) -> dict:
        if not self.players_hand[0] or not self.battlefield:
            return {"status": "No cards to play or no targets available."}

        turn_result = self.strategy.execute_turn(self.players_hand[0],
                                                 self.battlefield)
        played_card = turn_result['played_card']
        target = turn_result['target']
        damage_dealt = turn_result['damage_dealt']

        self.players_hand[0].remove(played_card)
        if played_card.type in ['creature', 'artifact']:
            self.battlefield.append(played_card)

        if target in self.battlefield:
            if hasattr(target, 'health'):
                target.health -= damage_dealt
                if target.health <= 0:
                    self.battlefield.remove(target)
                    self.deck.add_card(target)
            elif hasattr(target, 'durability'):
                target.durability -= damage_dealt
                if target.durability <= 0:
                    self.battlefield.remove(target)
                    self.deck.add_card(target)

        return turn_result


    def get_engine_status(self) -> dict:
        status = {
            'players_hand': [[card.name for card in hand] for hand in self.players_hand],
            'battlefield': [card.name for card in self.battlefield]
        }
        status.update(self.deck.get_deck_stats())
        return status
