from typing import Dict
from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int, effect: str):
        super().__init__(name, cost, rarity)
        self.type = "creature"
        if attack >= 0:
            self.attack = attack
        else:
            self.attack = 0
        if health >= 0:
            self.health = health
        else:
            self.health = 0
        self.effect = effect

    def get_card_info(self) -> Dict:
        data = super().get_card_info()
        data.update({'type': self.type,
                     'attack': self.attack,
                     'health': self.health,
                     'effect': self.effect})
        return data

    def play(self, game_state: Dict) -> Dict:
        data = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }
        data.update(game_state)
        return data

    def attack_target(self, target) -> Dict:
        data = {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack,
            'combat_resolved': False
        }
        target.health -= self.attack
        if target.health <= 0:
            data['combat_resolved'] = True
        return data
