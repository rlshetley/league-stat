from api.models import *
from random import randint

def create_hitting(session, player_id, game_id):
    """
    Function to create hitting statistics for a player
    """
    totalAB = randint(3,8)

    hits = randint(0, totalAB)

    runs = randint(0, 4)
    walks = 0
    singles = 0
    doubles = 0
    triples = 0
    home_runs = 0
    if hits > 0:
        tmp = hits
        singles = randint(0, tmp)

        tmp -= singles

        if tmp > 0:
            doubles = randint(0, tmp)

            tmp -= doubles

        if tmp > 0:
            triples = randint(0, tmp)

            tmp -= triples

        if tmp > 0:
            home_runs = randint(0, tmp)

            tmp -= home_runs

    if hits < totalAB:
        walks = randint(0, totalAB - hits)


    item = Game_Player_Hitting_Stats(
        game_id=game_id,
        player_id = player_id,
        at_bats = totalAB,
        hits = hits,
        runs = runs,
        walks = walks,
        singles = singles,
        doubles = doubles,
        triples = triples,
        home_runs = home_runs)

    session.add(item)
    session.commit()

def create_pitching(session, player_id, game_id, innings):
    """
    Function to create pitching statistics for a player
    """
    hits = randint(0, 15)
    strikeouts = randint(0, 15)
    runs = randint(0, 15)
    walks = randint(0, 15)

    item = Game_Player_Pitching_Stats(
        game_id=game_id,
        player_id = player_id,
        strikeOuts = strikeouts,
        hits = hits,
        runs = runs,
        walks = walks,
        innings_pitched = innings)

    session.add(item)
    session.commit()
