
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(os.getcwd())

from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from api.models import *
import names
import requests
import json
import time
import datetime
from random import randint,randrange
from datetime import timedelta, datetime
from game_stats import *

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

engine = create_engine('sqlite+pysqlite:///leagueStat.sqllite3', echo=True)

Session = sessionmaker()

Session.configure(bind=engine)

session = Session()

session.query(Player).delete()
session.query(Coach).delete()
session.query(FamilyMember).delete()
session.query(Team).delete()
session.query(League).delete()
session.query(Player_FamilyMember).delete()
session.query(Player_Team).delete()
session.query(Coach_Team).delete()
session.query(League_Team).delete()
session.query(Game).delete()
session.query(Game_Player_Hitting_Stats).delete()
session.query(Game_Player_Pitching_Stats).delete()

for count in range(1,100):
    player = Player(first_name=names.get_first_name(), last_name=names.get_last_name())
    session.add(player)
    session.commit()

for count in range(1,100):
    player = Coach(first_name=names.get_first_name(), last_name=names.get_last_name())
    session.add(player)
    session.commit()

for count in range(1,100):
    player = FamilyMember(first_name=names.get_first_name(), last_name=names.get_last_name())
    session.add(player)
    session.commit()

r = requests.get('https://erikberg.com/mlb/teams.json')

data = r.json()

for item in data:
    team = Team(name=item['last_name'])
    session.add(team)
    session.commit()

for item in ['Fall', 'Summer A', 'Fall B', 'Summer B']:
    team = League(name=item)
    session.add(team)
    session.commit()



players = session.query(Player).all()
coaches = session.query(Coach).all()
families = session.query(FamilyMember).all()

for player, fam in zip(players[0::3], families[0::4]):
    check = session.query(Player_FamilyMember).filter(and_(Player_FamilyMember.family_member_id==fam.id, Player_FamilyMember.player_id==player.id)).first()

    if check is None:
        item = Player_FamilyMember(family_member_id=fam.id, player_id=player.id)
        session.add(item)
        session.commit()

for player, fam in zip(players[0::4], families[0::3]):
    check = session.query(Player_FamilyMember).filter(and_(Player_FamilyMember.family_member_id==fam.id, Player_FamilyMember.player_id==player.id)).first()

    if check is None:
        item = Player_FamilyMember(family_member_id=fam.id, player_id=player.id)
        session.add(item)
        session.commit()

for player, fam in zip(players[0::10], families[0::10]):
    check = session.query(Player_FamilyMember).filter(and_(Player_FamilyMember.family_member_id==fam.id, Player_FamilyMember.player_id==player.id)).first()

    if check is None:
        item = Player_FamilyMember(family_member_id=fam.id, player_id=player.id)
        session.add(item)
        session.commit()

# 10 teams in each league
teams = session.query(Team).all()

leagues = session.query(League).all()

league = leagues[0]
coach_count = 0
player_count = 0

for team in teams[0:9]:
    team.league_id=league.id
    session.commit()

    item = Coach_Team(team_id=team.id, coach_id=coaches[coach_count].id)
    session.add(item)
    session.commit()

    coach_count += 1

    for player in players[player_count:player_count+10]:
        item = Player_Team(team_id=team.id, player_id=player.id)
        session.add(item)
        session.commit()

    player_count += 10


league = leagues[1]
player_count = 0
league_first = []
for team in teams[10:19]:
    col = {}
    col['team_id'] = team.id
    col['team'] = team

    team.league_id=league.id
    session.commit()

    item = Coach_Team(team_id=team.id, coach_id=coaches[coach_count].id)
    session.add(item)
    session.commit()

    coach_count += 1

    league_players = []
    for player in players[player_count:player_count+10]:
        item = Player_Team(team_id=team.id, player_id=player.id)
        session.add(item)
        session.commit()
        league_players.append(player)

    col['players'] = league_players
    player_count += 10

    league_first.append(col)

rdint = 0

for team in league_first:
    for opp in league_first:
        if opp['team_id'] != team['team_id']:
            d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')

            home_team_id=team['team_id']
            away_team_id=opp['team_id']

            if rdint % 2 == 0:
                away_team_id=team['team_id']
                home_team_id=opp['team_id']

            gd = random_date(d1, d2)
            game = Game(away_score=randint(0,15), home_score=randint(0,15), away_team_id=away_team_id, home_team_id=home_team_id, game_date=gd)
            session.add(game)
            session.commit()

            for pl in col['players']:
                create_hitting(session, pl.id, game.id)


            rnd_ind = randint(0, len(col['players']) - 1)

            create_pitching(session, col['players'][rnd_ind].id, game.id, 9)


# Creating new league
league = leagues[2]
player_count = 0

for team in teams[20:29]:

    team.league_id=league.id
    session.commit()

    item = Coach_Team(team_id=team.id, coach_id=coaches[coach_count].id)
    session.add(item)
    session.commit()

    coach_count += 1

    for player in players[player_count:player_count+10]:
        item = Player_Team(team_id=team.id, player_id=player.id)
        session.add(item)
        session.commit()

    player_count += 10
