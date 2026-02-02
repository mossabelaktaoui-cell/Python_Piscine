from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    matches_played = 0

    def __init__(self) -> None:
        self.registered_card = {}
        self.winner = None
        self.loser = None
        self.status = 'deactive'

    def register_card(self, card: TournamentCard) -> str:
        self.status = 'active'
        self.registered_card.update({card.card_id: card})
        return f"""
{card.name} (ID: {card.card_id}):
- Interfaces: {card.interfaces}
- Rating: {card.calculate_rating()}
- Record: {card.record}"""

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.registered_card[card1_id]
        card2 = self.registered_card[card2_id]

        attacker, defender = card1, card2

        while card1.health > 0 and card2.health > 0:
            attacker.attack(defender)
            attacker, defender = defender, attacker

        if card1.health <= 0 and card2.health >= 0:
            self.winner = card2
            self.loser = card1
        elif card2.health <= 0 and card1.health >= 0:
            self.winner = card1
            self.loser = card2

        self.winner.update_wins(1)
        self.loser.update_losses(1)

        TournamentPlatform.matches_played += 1
        return {
            'winner': self.winner.card_id,
            'loser': self.loser.card_id,
            'winner_rating': self.winner.calculate_rating(),
            'loser_rating': self.loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        result = ""
        cards = self.sort_cards()
        leaderboard = []
        i = 1

        for card in cards:
            leaderboard.append(
                f"{i}. {card.name} - "
                f"Rating: "f"{card.calculate_rating()}"
                f" ({card.record})")
            i += 1

        for line in leaderboard:
            result += line + "\n"

        return result

    def generate_tournament_report(self) -> dict:
        ratings = [card.calculate_rating() for card
                   in self.registered_card.values()]
        num = len(ratings)
        avg = sum(ratings) / num if num > 0 else 0
        return {
            'total_cards': num,
            'matches_played': self.matches_played,
            'avg_rating': avg,
            'platform_status': self.status
        }

    def sort_cards(self) -> list:
        cards = list(self.registered_card.values())

        n = len(cards)
        for i in range(n):
            for j in range(i + 1, n):
                if cards[i].calculate_rating() < cards[j].calculate_rating():
                    cards[i], cards[j] = cards[j], cards[i]

        return cards
