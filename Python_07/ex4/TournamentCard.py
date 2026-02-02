from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: int, card_id, health, attack_power, defense):
        super().__init__(name, cost, rarity)
        self.health = health
        self.defense = defense
        self.attack_power = attack_power
        self.card_id = card_id
        self.wins = 0
        self.losses = 0
        self.interfaces = ['Card', 'Combatable', 'Rankable']
        self.record = f"{self.wins}-{self.losses}"

    def play(self, game_state: dict) -> dict:
        data = {
            "card_played": self.name,
            "mana_used": self.cost,
            "interfaces": self.interfaces,
            "rate": self.calculate_rating(),
            "record": self.record
        }
        data.update(game_state)
        return data

    def attack(self, target: 'TournamentCard') -> dict:
        target.defend(self.attack_power)
        data = {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack_power
        }
        return data

    def defend(self, incoming_damage: int) -> dict:
        if self.defense >= incoming_damage:
            self.defense -= incoming_damage
            return {
                "incoming_damage": incoming_damage,
                "damage_taken": 0,
                "shield_remaining": self.defense
            }
        else:
            damage_taken = incoming_damage - self.defense
            self.defense = 0

            if damage_taken > self.health:
                self.health = 0
            else:
                self.health -= damage_taken

            return {
                "incoming_damage": incoming_damage,
                "damage_taken": damage_taken,
                "remaining_health": self.health
            }

    def get_combat_stats(self) -> dict:
        return {
            'card_played': self.name,
            'attack': self.attack_power_power,
            'health': self.health
        }

    def calculate_rating(self) -> int:
        return 1200 + (self.wins * 30) - (self.losses * 15)

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.record = f"{self.wins}-{self.losses}"

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.record = f"{self.wins}-{self.losses}"

    def get_rank_info(self) -> dict:
        return {
            'card_played': self.name,
            'card_id': self.card_id,
            'wins': self.wins,
            'losses': self.losses,
            'rating': self.calculate_rating(),
            'record': self.record
        }
