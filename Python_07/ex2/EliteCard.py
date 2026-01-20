from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)
        self.type = "elite"

    def play(self, game_state: dict) -> dict:
        data = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect_type,
        }
        data.update(game_state)
        return data

    def attack(self, target) -> dict:
        data = {
            'attacker': self.name,
            'target': target,
            'damage': 5,
            'combat_type': 'melee'
        }
        return data

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        data = {
            'caster': self.name,
            'spell': spell_name,
            'targets': [target for target in targets],
            'mana_used': 4
        }
        return data

    def defend(self, incoming_damage: int) -> dict:
        data = {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': 5 - incoming_damage,
            'still_alive': True
        }
        return data

    def channel_mana(self, amount: int) -> dict:
        data = {'channeled': amount,
                'total_mana': 7}
        return data

    def get_combat_stats(self) -> dict:
        data = {
            'attack': self.attack("Enemy"),
            'defense': self.defend(2)
        }
        return data

    def get_magic_stats(self) -> dict:
        data = {
            'spells_cast': self.cast_spell("Fireball", ['Enemy1', 'Enemy2']),
            'mana_channeled': self.channel_mana(3)
        }
        return data
