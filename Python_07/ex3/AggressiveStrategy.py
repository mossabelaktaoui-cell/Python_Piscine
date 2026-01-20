from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        

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