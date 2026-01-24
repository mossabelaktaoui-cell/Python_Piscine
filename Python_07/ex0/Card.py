from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        super().__init__()
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        pass

    def get_card_info(self) -> Dict:
        data = {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
        }
        return data

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        return False
