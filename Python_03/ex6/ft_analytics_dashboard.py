data = {
    'players': {
        'alice': {
            'level': 41,
            'total_score': 2824,
            'sessions_played': 13,
            'favorite_mode': 'ranked',
            'achievements_count': 5
        },
        'bob': {
            'level': 16,
            'total_score': 4657,
            'sessions_played': 27,
            'favorite_mode': 'ranked',
            'achievements_count': 2
        },
        'charlie': {
            'level': 44,
            'total_score': 9935,
            'sessions_played': 21,
            'favorite_mode': 'ranked',
            'achievements_count': 7
        },
        'diana': {
            'level': 3,
            'total_score': 1488,
            'sessions_played': 21,
            'favorite_mode': 'casual',
            'achievements_count': 4
        },
        'eve': {
            'level': 33,
            'total_score': 1434,
            'sessions_played': 81,
            'favorite_mode': 'casual',
            'achievements_count': 7
        },
        'frank': {
            'level': 15,
            'total_score': 8359,
            'sessions_played': 85,
            'favorite_mode': 'competitive',
            'achievements_count': 1
        }
    },
    'sessions': [
        {'player': 'bob', 'duration_minutes': 94,
         'score': 1831, 'mode': 'competitive',
         'completed': False},
        {'player': 'bob', 'duration_minutes': 32,
         'score': 1478, 'mode': 'casual',
         'completed': True},
        {'player': 'diana', 'duration_minutes': 17,
         'score': 1570, 'mode': 'competitive',
         'completed': False},
        {'player': 'alice', 'duration_minutes': 98,
         'score': 1981, 'mode': 'ranked',
         'completed': True},
        {'player': 'diana', 'duration_minutes': 15,
         'score': 2361, 'mode': 'competitive',
         'completed': False},
        {'player': 'eve', 'duration_minutes': 29,
         'score': 2985, 'mode': 'casual',
         'completed': True},
        {'player': 'frank', 'duration_minutes': 34,
         'score': 1285, 'mode': 'casual',
         'completed': True},
        {'player': 'alice', 'duration_minutes': 53,
         'score': 1238, 'mode': 'competitive',
         'completed': False},
        {'player': 'bob', 'duration_minutes': 52,
         'score': 1555, 'mode': 'casual',
         'completed': False},
        {'player': 'frank', 'duration_minutes': 92,
         'score': 2754, 'mode': 'casual',
         'completed': True},
        {'player': 'eve', 'duration_minutes': 98,
         'score': 1102, 'mode': 'casual',
         'completed': False},
        {'player': 'diana', 'duration_minutes': 39,
         'score': 2721, 'mode': 'ranked',
         'completed': True},
        {'player': 'frank', 'duration_minutes': 46,
         'score': 329, 'mode': 'casual',
         'completed': True},
        {'player': 'charlie', 'duration_minutes': 56,
         'score': 1196, 'mode': 'casual',
         'completed': True},
        {'player': 'eve', 'duration_minutes': 117,
         'score': 1388, 'mode': 'casual',
         'completed': False},
        {'player': 'diana', 'duration_minutes': 118,
         'score': 2754, 'mode': 'competitive',
         'completed': True},
        {'player': 'charlie', 'duration_minutes': 22,
         'score': 1110, 'mode': 'ranked',
         'completed': False},
        {'player': 'frank', 'duration_minutes': 79,
         'score': 1854, 'mode': 'ranked',
         'completed': False},
        {'player': 'charlie', 'duration_minutes': 33,
         'score': 666, 'mode': 'ranked',
         'completed': False},
        {'player': 'alice', 'duration_minutes': 101,
         'score': 292, 'mode': 'casual',
         'completed': True},
        {'player': 'frank', 'duration_minutes': 25,
         'score': 2887, 'mode': 'competitive',
         'completed': True},
        {'player': 'diana', 'duration_minutes': 53,
         'score': 2540, 'mode': 'competitive',
         'completed': False},
        {'player': 'eve', 'duration_minutes': 115,
         'score': 147, 'mode': 'ranked',
         'completed': True},
        {'player': 'frank', 'duration_minutes': 118,
         'score': 2299, 'mode': 'competitive',
         'completed': False},
        {'player': 'alice', 'duration_minutes': 42,
         'score': 1880, 'mode': 'casual',
         'completed': False},
        {'player': 'alice', 'duration_minutes': 97,
         'score': 1178, 'mode': 'ranked',
         'completed': True},
        {'player': 'eve', 'duration_minutes': 18,
         'score': 2661, 'mode': 'competitive',
         'completed': True},
        {'player': 'bob', 'duration_minutes': 52,
         'score': 761, 'mode': 'ranked',
         'completed': True},
        {'player': 'eve', 'duration_minutes': 46,
         'score': 2101, 'mode': 'casual',
         'completed': True},
        {'player': 'charlie', 'duration_minutes': 117,
         'score': 1359, 'mode': 'casual',
         'completed': True}
    ],
    'game_modes': ['casual', 'competitive', 'ranked'],
    'achievements': [
        'first_blood', 'level_master', 'speed_runner', 'treasure_seeker',
        'boss_hunter', 'pixel_perfect', 'combo_king', 'explorer'
    ]
}


def list_comprehension_example() -> None:
    doubled_scores = []
    active_players = []

    high_score_players = [player for player in data['players']
                          if data['players'][player]['total_score'] > 2000]

    i = 0
    while i < len(data['sessions']) - 1:
        score1 = data['sessions'][i]['score']
        j = i + 1
        while j < len(data['sessions']):
            score2 = data['sessions'][j]['score']
            if score1 == score2 and score1 not in doubled_scores:
                doubled_scores.append(score1)
            j += 1
        i += 1

    i = 0
    while i < len(data['sessions']):
        if data['sessions'][i]['player'] not in active_players:
            active_players.append(data['sessions'][i]['player'])
        i += 1

    print("\n=== List Comprehension Examples ===")
    print(f"High scores (>2000): {high_score_players}")
    print(f"Scores doubled: {doubled_scores}")
    print(f"Active players: {active_players}")


def dict_comprehension_example() -> None:
    score_categories = {'high': 0, 'medium': 0, 'low': 0}
    achievement_counts = {}

    player_score = {player: data['players'][player]['total_score']
                    for player in data['players'].keys()}

    high = 0
    medium = 0
    low = 0
    for player in data['players'].keys():
        score = data['players'][player]['total_score']
        if score > 2000:
            high += 1
        elif score > 1000:
            medium += 1
        else:
            low += 1
    score_categories['high'] = high
    score_categories['medium'] = medium
    score_categories['low'] = low

    for player in data['players'].keys():
        player_data = data['players'][player]
        achievement_counts[player] = player_data['achievements_count']

    print("\n=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_score}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")


def set_comprehension_example() -> None:
    unique_players = []
    i = 0
    while i < len(data['sessions']):
        unique_players.append(data['sessions'][i]['player'])
        i += 1

    unique_achievements = []
    i = 0
    while i < len(data['achievements']):
        unique_achievements.append(data['achievements'][i])
        i += 1
    unique_achievements = set(unique_achievements)

    active_regions = []
    i = 0
    while i < len(data['sessions']):
        region = data['sessions'][i].get('mode')
        if region == 'ranked':
            active_regions.append('central')
        elif region == 'casual':
            active_regions.append('north')
        elif region == 'competitive':
            active_regions.append('east')
        i += 1
    active_regions = set(active_regions)

    unique_players_set = set(unique_players)
    print("\n=== Set Comprehension Examples ===")
    print(f"Unique players: {unique_players_set}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")


def combined_analysis() -> None:
    total_players = len(data['players'].keys())
    total_unique_achievements = len(data['achievements'])
    average_score = 0
    for player in data['players'].keys():
        average_score += data['players'][player]['total_score']
    average_score /= total_players

    players_points = {}
    for player in data['players'].keys():
        p = data['players'][player]
        players_points[player] = (
            p['total_score'] * p['achievements_count']
        )
    top_point = max(players_points.values())
    for player, points in players_points.items():
        if points == top_point:
            top_player = player

    print("\n=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score:.1f}")
    print(f"Top player by points: {top_player} "
          f"({data['players'][top_player]['total_score']} score, "
          f"{data['players'][top_player]['achievements_count']} achievements)")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    list_comprehension_example()
    dict_comprehension_example()
    set_comprehension_example()
    combined_analysis()
