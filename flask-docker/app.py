from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values
from routes.API.bets import bets_bp
from routes.API.groups import groups_bp
from routes.API.matches import matches_bp
from routes.API.sports import sports_bp
from routes.API.tournaments import tournaments_bp
from routes.API.users import users_bp
from routes.landing_page import landing_page_bp
from routes.login import login_bp
from routes.register import register_bp
from data_manager import DataManager

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests


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
data_manager = DataManager(Session())

app.register_blueprint(bets_bp)
app.register_blueprint(groups_bp)
app.register_blueprint(matches_bp)
app.register_blueprint(sports_bp)
app.register_blueprint(tournaments_bp)
app.register_blueprint(users_bp)
app.register_blueprint(landing_page_bp)
app.register_blueprint(login_bp)
app.register_blueprint(register_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
