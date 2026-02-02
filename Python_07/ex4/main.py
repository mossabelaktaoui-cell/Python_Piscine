from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    card1 = TournamentCard("Blue Dragon", 5, 3, "drg_01", 100, 30, 10)
    card2 = TournamentCard("Shadow Knight", 4, 2, "kni_02", 80, 35, 5)

    print("Registering Tournament Cards...")
    print(platform.register_card(card1))
    print(platform.register_card(card2))

    print("\nCreating tournament match...")
    match_result = platform.create_match("drg_01", "kni_02")
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for player_stats in leaderboard:
        print(player_stats)

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
