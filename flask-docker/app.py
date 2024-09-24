from flask import Flask, jsonify
import json

app = Flask(__name__)

# Function to load data from data.json
def load_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data

@app.route("/")
def landing_page():
    return "<h1>Zestake</h1>"

@app.route("/bets", methods=["POST", "GET"])
def bets():
    data = load_data()
    return jsonify(data["bets"])

@app.route("/groups", methods=["POST", "GET"])
def groups():
    data = load_data()
    return jsonify(data["groups"])

@app.route("/matches", methods=["POST", "GET"])
def matches():
    data = load_data()
    return jsonify(data["matches"])

@app.route("/sports", methods=["POST", "GET"])
def sports():
    data = load_data()
    return jsonify(data["sports"])

@app.route("/tournaments", methods=["POST", "GET"])
def tournaments():
    data = load_data()
    return jsonify(data["tournaments"])

@app.route("/users", methods=["POST", "GET"])
def users():
    data = load_data()
    return jsonify(data["users"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
