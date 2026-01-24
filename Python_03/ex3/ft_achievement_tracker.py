data = {
    'alice': [
        'first_blood', 'pixel_perfect', 'speed_runner', 'first_blood',
        'first_blood'
    ],
    'bob': [
        'level_master', 'boss_hunter', 'treasure_seeker', 'level_master',
        'level_master', 'first_blood'
    ],
    'charlie': [
        'treasure_seeker', 'boss_hunter', 'combo_king', 'first_blood',
        'boss_hunter', 'first_blood', 'boss_hunter', 'first_blood'
    ],
    'diana': [
        'first_blood', 'combo_king', 'level_master', 'treasure_seeker',
        'speed_runner', 'combo_king', 'combo_king', 'level_master'
    ],
    'eve': [
        'level_master', 'treasure_seeker', 'first_blood', 'treasure_seeker',
        'first_blood', 'treasure_seeker'
    ],
    'frank': [
        'explorer', 'boss_hunter', 'first_blood', 'explorer', 'first_blood',
        'boss_hunter'
    ]
}


def display_players_data(data: dict) -> None:
    print("=== Achievement Tracker System ===\n")
    for player, data in data.items():
        print(f"player {player} achievements: {set(data)}")


def achievement_analytics(data: dict) -> None:
    players = list(data.keys())
    common_achievements = set(data[players[0]])
    unique_acheivements = set()
    difference_achievements = set()
    diff_achievements = set()

    for player in data.keys():
        unique_acheivements = unique_acheivements | set(data[player])
        common_achievements = common_achievements & set(data[player])
        diff_achievements = set(data[player])
        for player_ in data.keys():
            if player_ != player:
                diff_achievements = diff_achievements - set(data[player_])
        difference_achievements = difference_achievements | diff_achievements

    if not common_achievements:
        common_achievements = "{}"
    if not unique_acheivements:
        unique_acheivements = "{}"
    if not difference_achievements:
        difference_achievements = "{}"

    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {unique_acheivements}")
    print(f"Total unique achievements: {len(unique_acheivements)}")
    print(f"\nCommon to all players:{common_achievements}")
    print(f"Rare achievements (1 player): {difference_achievements}")


def two_players_common(data: dict, player1: str, player2: str) -> None:
    common = set(data[player1]).intersection(set(data[player2]))
    player1_unique = set(data[player1]).difference(set(data[player2]))
    player2_unique = set(data[player2]).difference(set(data[player1]))

    if not common:
        common = "{}"
    if not player1_unique:
        player1_unique = "{}"
    if not player2_unique:
        player2_unique = "{}"

    print(f"\n{player1.capitalize()} vs {player2.capitalize()}"
          f" common: {common}")
    print(f"{player1.capitalize()} unique: {player1_unique}")
    print(f"{player2.capitalize()} unique: {player2_unique}")


if "__main__" == __name__:
    display_players_data(data)
    achievement_analytics(data)
    two_players_common(data, 'alice', 'bob')
