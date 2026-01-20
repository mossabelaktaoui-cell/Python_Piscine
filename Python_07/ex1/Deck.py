from ex0.Card import Card
from random import choice


class Deck:
    cards = []
    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        new_cards = []
        is_removed = False
        for card in self.cards:
            if card.name != card_name:
                new_cards.append(card)
            else:
                is_removed = True
        self.cards = new_cards
        return is_removed

    def shuffle(self) -> None:
        indexes = list(range(len(self.cards)))
        new_cards = self.cards.copy()
        for card in self.cards:
            rand_index = choice(indexes)
            indexes.remove(rand_index)
            new_cards[rand_index] = card
        self.cards = new_cards

    def draw_card(self) -> Card:
        drawed_card = self.cards[0]
        self.remove_card(drawed_card.name)
        return drawed_card

    def get_deck_stats(self) -> dict:
        creature_number = len([card for card in self.cards if card.type == 'creature'])
        spell_number = len([card for card in self.cards if card.type == 'spell'])
        artifact_number = len([card for card in self.cards if card.type == 'artifact'])
        total_cost = sum([card.cost for card in self.cards])
        avg_cost = total_cost / len(self.cards)
        deck_stats = {
            'total_cards': len(self.cards),
            'creatures': creature_number,
            'spells': spell_number,
            'artifacts': artifact_number,
            'avg_cost': f"{avg_cost:.1f}"
        }
        return deck_stats