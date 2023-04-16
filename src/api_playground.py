import re
from team_stats import Teams


def get_active_roster_players_scrabble_scores():

    scrabble_mp = {
        "a": 1,
        "b": 3,
        "c": 3,
        "d": 2,
        "e": 1,
        "f": 4,
        "g": 2,
        "h": 4,
        "i": 1,
        "j": 8,
        "k": 5,
        "l": 1,
        "m": 3,
        "n": 1,
        "o": 1,
        "p": 3,
        "q": 10,
        "r": 1,
        "s": 1,
        "t": 1,
        "u": 1,
        "v": 4,
        "w": 4,
        "x": 8,
        "y": 4,
        "z": 10,
    }

    t = Teams()
    player_scrabble_score_map = {}
    regex = re.compile("[^a-zA-Z]")
    for teams, players in t.get_abv_to_players_map().items():
        for player in players:
            raw_chars = [*regex.sub("", player.lower())]
            scrabble_score = sum(map(lambda x: scrabble_mp[x], raw_chars))
            player_scrabble_score_map[player] = scrabble_score

    print(sorted(player_scrabble_score_map.items(), key=lambda x: x[1], reverse=True))


def main():
    get_active_roster_players_scrabble_scores()


if __name__ == "__main__":
    main()
