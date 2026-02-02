from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        if durability > 0:
            self.durability = durability
        else:
            self.durability = 0
        self.effect = effect
        self.type = "artifact"

    def play(self, game_state: dict) -> dict:
        data = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect,
        }
        data.update(game_state)
        return data

    def activate_ability(self) -> dict:
        self.durability -= 1
        data = {
            'artifact': self.name,
            'remaining_durability': self.durability,
            'ability_activated': True
        }
        if self.durability <= 0:
            data['ability_activated'] = False
        return data
