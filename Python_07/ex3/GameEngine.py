from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.deck = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_cards_created = 0
        self.total_damage = 0
        self.battlefield = []
        self.players_data = {'Player 1': {'hand': [],
                                          'mana': 10},
                             'Player 2': {'hand': [],
                                          'mana': 10}}

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        deck_data = factory.create_themed_deck(40)

        self.deck = deck_data['deck']
        self.total_cards_created = len(self.deck.cards)
        self.deck.shuffle()
        self.strategy = strategy

        for player in self.players_data.keys():
            for _ in range(5):
                self.players_data[player]['hand'].append(self.deck.draw_card())

    def simulate_turn(self) -> dict:
        player_hand = self.players_data['Player 1']['hand']
        if not player_hand:
            return {"status": "No cards to play."}

        turn_result = self.strategy.execute_turn(player_hand, self.battlefield)

        self.turns_simulated += 1
        self.total_damage += turn_result['damage_dealt']
        self.players_data['Player 1']['mana'] -= turn_result['mana_used']

        for card in turn_result['cards_played']:
            if card in player_hand:
                player_hand.remove(card)
                if card.type in ['creature', 'artifact']:
                    self.battlefield.append(card)

        attacking_cards = [card for card in turn_result['cards_played']
                           if card.type in ['creature', 'spell']]
        for card, target in zip(attacking_cards,
                                turn_result['targets_attacked']):
            if target and target in self.battlefield:
                self.apply_damage(card, target)

        self.battlefield = self.clean_battlefield()
        return {
            'cards_played': [card.name for card
                             in turn_result['cards_played']],
            'mana_used': turn_result['mana_used'],
            'targets_attacked': [card.name for card
                                 in turn_result['targets_attacked']],
            'damage_dealt': turn_result['damage_dealt']
        }

    def get_engine_status(self) -> dict:
        status = {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.total_cards_created,
        }
        return status

    def clean_battlefield(self) -> list:
        alive_cards = []

        for card in self.battlefield:
            is_alive = True
            if hasattr(card, 'health') and card.health <= 0:
                is_alive = False
            if hasattr(card, 'durability') and card.durability <= 0:
                is_alive = False

            if is_alive:
                alive_cards.append(card)
            else:
                self.deck.add_card(card)

        return alive_cards

    def apply_damage(self, attacker, target) -> None:
        if attacker.type == 'creature':
            damage = attacker.attack
        else:
            damage = 3

        if hasattr(target, 'health'):
            target.health -= damage
        elif hasattr(target, 'durability'):
            target.durability -= damage
