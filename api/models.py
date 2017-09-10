from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, DateTime

from api import db

class Base(db.Model):
    __abstract__ = True

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

class Coach(Base):
    __tablename__ = 'coaches'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

class FamilyMember(Base):
    __tablename__ = 'family_members'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

class League(Base):
    __tablename__ = 'leagues'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

class League_Team(Base):
    __tablename__ = 'league_teams'
    team_id = Column(Integer, primary_key=True)
    league_id = Column(Integer, primary_key=True)

class Player_FamilyMember(Base):
    __tablename__ = 'family_member_players'
    player_id = Column(Integer, primary_key=True)
    family_member_id = Column(Integer, primary_key=True)

class Player_Team(Base):
    __tablename__ = 'player_teams'
    team_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, primary_key=True)

class Coach_Team(Base):
    __tablename__ = 'coach_teams'
    team_id = Column(Integer, primary_key=True)
    coach_id = Column(Integer, primary_key=True)

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    away_team_id = Column(Integer)
    home_team_id = Column(Integer)

    away_score = Column(Integer)
    home_score = Column(Integer)

    game_date = Column(DateTime)

class Game_Player_Hitting_Stats(Base):
    __tablename__ = 'game_player_hitting_stats'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer)
    player_id = Column(Integer)
    at_bats = Column(Integer)
    hits = Column(Integer)
    runs = Column(Integer)
    walks = Column(Integer)
    singles = Column(Integer)
    doubles = Column(Integer)
    triples = Column(Integer)
    home_runs = Column(Integer)

class Game_Player_Pitching_Stats(Base):
    __tablename__ = 'game_player_pitching_stats'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer)
    player_id = Column(Integer)
    strikeOuts = Column(Integer)
    hits = Column(Integer)
    runs = Column(Integer)
    walks = Column(Integer)
    innings_pitched = Column(Integer)
