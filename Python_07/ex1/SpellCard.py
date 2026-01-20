from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.type = "spell"
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        data = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect_type,
        }
        data.update(game_state)
        return data

    def resolve_effect(self, targets: list) -> dict:
        data = {
            'effect_type': self.effect_type,
            'targets': [target.name for target in targets],
            'consumed': True
        }
        return data
