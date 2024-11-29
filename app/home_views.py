from app import app
from flask import render_template, jsonify
import requests
import json
import jsonpickle


@app.route("/")
@app.route("/home")
def home():
    return render_template("home/home.html")


@app.route("/goals")
def goals():
    return render_template("home/goals.html")


@app.route("/website")
def website():
    return render_template("home/website.html")


@app.route("/game")
def game():
    return render_template("home/index.html")


@app.route("/chuck")
def chuck():
    return render_template("home/chuck.html")


@app.route("/api/jokes/random")
def joke():
    f = r"https://api.chucknorris.io/jokes/random/"

    data = requests.get(f)
    chuck_joke = json.loads(data.text)
    return chuck_joke


@app.route("/api/jokes/category/<category>")
def category_joke(category):
    f = r"https://api.chucknorris.io/jokes/random?category=" + category

    data = requests.get(f)
    chuck_joke = json.loads(data.text)
    return chuck_joke


@app.route("/api/jokes/search/<search_term>")
def search_joke(search_term):
    ff = r"https://api.chucknorris.io/jokes/search?query=" + search_term

    data = requests.get(ff)
    chuck_joke = data.json()
    return chuck_joke
