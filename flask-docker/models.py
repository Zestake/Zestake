from sqlalchemy import create_engine, Column, Integer, String, Date, JSON, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Bet(Base):
    __tablename__ = "Bets"
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey("matches.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    bet = Column(JSON)


class Group(Base):
    __tablename__ = "Groups"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    users = Column(Integer, ForeignKey("users.id"))


class Match(Base):
    __tablename__ = "Matches"
    id = Column(Integer, primary_key=True)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    stage = Column(String)
    contestants = Column(JSON)
    score = Column(JSON)
    delay = Column(Integer)
    start_date = Column(Date)


class Sport(Base):
    __tablename__ = "Sports"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Tournament(Base):
    __tablename__ = "Tournaments"
    id = Column(Integer, primary_key=True)
    groups_id = Column(Integer, ForeignKey("groups.id"))
    sports_id = Column(Integer, ForeignKey("sports.id"))
    name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    match_value_map = Column(JSON)
    visibility_bets = Column(Boolean)


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
