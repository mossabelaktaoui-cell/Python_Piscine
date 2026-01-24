from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        used_mana = 0
        hand = self.order_hand(hand)
        battlefield = self.prioritize_targets(battlefield)
        damage_dealt = 0
        cards_played = []
        total_targets_cost = 0
        targets_attacked = []


        for card in hand:
            if card.is_playable(10 - used_mana):
                cards_played.append(card.name)
                used_mana += card.cost
                if hasattr(card, 'attack'):
                    damage_dealt += card.attack
                elif hasattr(card, 'effect_type') and card.effect_type == "damage":
                    damage_dealt += 3

        for card in battlefield:
            if total_targets_cost + card.cost <= used_mana:
                targets_attacked.append(card.name)
                total_targets_cost += card.cost

        result = {
            'cards_played': cards_played,
            'mana_used': used_mana,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt
            }   
        return result

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        creatures = [
          target for target in available_targets if target.type == "creature"]
        spells = [
          target for target in available_targets if target.type == "spell"]
        artifacts = [
          target for target in available_targets if target.type == "artifact"]
        return creatures + spells + artifacts

    def order_hand(self, hand: list) -> list:
        i = 0
        while i < len(hand):
            j = i + 1
            while j < len(hand):
                if hand[i].cost > hand[j].cost:
                    hand[i], hand[j] = hand[j], hand[i]
                j += 1
            i += 1
        
        return hand