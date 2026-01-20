from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        creatures_in_hand = [
            card for card in hand if card.get('type') == 'creature']
        artifacts_in_hand = [
            card for card in hand if card.get('type') == 'artifact']
        spells_in_hand = [
            card for card in hand if card.get('type') == 'spell']
        battlefield = self.prioritize_targets(battlefield)
        if battlefield[0].type == 'artifact':
            played_card = artifacts_in_hand[0]
            priority = {'attack': played_card.attack, 'health': played_card.health}
        elif battlefield[0].type == 'creature':
            played_card = creatures_in_hand[0]
            priority = {'defense': played_card.durability, 'effect': played_card.effect}
        else:
            played_card = spells_in_hand[0]
            priority = {'effect_type': played_card.effect_type}
        result = {
            'strategy': self.get_strategy_name(),
            'played_card': played_card.name,
        }
        result.update(priority)
        return result

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        prioritized = []
        for target in available_targets:
            if target.get('type') == 'creature':
                prioritized.append(target)
        for target in available_targets:
            if target.get('type') == 'spell':
                prioritized.append(target)
        for target in available_targets:
            if target.get('type') == 'artifact':
                prioritized.append(target)
        return prioritized