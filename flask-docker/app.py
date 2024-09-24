from flask import Flask, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Date, JSON, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from dotenv import dotenv_values

app = Flask(__name__)
Base = declarative_base()


def db_connect():
    config = dotenv_values("./.env")
    username = config.get("DATABASE_USERNAME")
    password = config.get("DATABASE_PASSWORD")
    dbname = config.get("DATABASE_NAME")
    port = config.get("DATABASE_PORT")
    host = config.get("DATABASE_HOST")

    engine = create_engine(
        f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}", echo=True
    )
    return engine


engine = db_connect()
Session = sessionmaker(bind=engine)


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


@app.route("/")
def landing_page():
    return "<h1>Zestake</h1>"


def fetch_data(model, keys):
    session = Session()
    try:
        results = session.query(model).all()
        return [{key: getattr(result, key) for key in keys} for result in results]
    except Exception as e:
        return {"error": str(e)}
    finally:
        session.close()


@app.route("/bets", methods=["POST", "GET"])
def bets():
    return jsonify(fetch_data(Bet, ["id", "match_id", "user_id", "bet"]))


@app.route("/groups", methods=["POST", "GET"])
def groups():
    return jsonify(fetch_data(Group, ["id", "name", "users"]))


@app.route("/matches", methods=["POST", "GET"])
def matches():
    return jsonify(
        fetch_data(
            Match,
            [
                "id",
                "tournament_id",
                "stage",
                "contestants",
                "score",
                "delay",
                "start_date",
            ],
        )
    )


@app.route("/sports", methods=["POST", "GET"])
def sports():
    return jsonify(fetch_data(Sport, ["id", "name"]))


@app.route("/tournaments", methods=["POST", "GET"])
def tournaments():
    return jsonify(
        fetch_data(
            Tournament,
            [
                "id",
                "groups_id",
                "sports_id",
                "name",
                "start_date",
                "end_date",
                "match_value_map",
                "visibility_bets",
            ],
        )
    )


@app.route("/users", methods=["POST", "GET"])
def users():
    return jsonify(fetch_data(User, ["id", "username", "password", "email"]))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
