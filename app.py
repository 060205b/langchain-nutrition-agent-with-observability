from flask import Flask, render_template, request
from app.lib import get_meal_recommendations  # this should be your core logic

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    age = request.form["age"]
    weight = request.form["weight"]
    preferences = request.form["preferences"]

    meals = get_meal_recommendations(age, weight, preferences)

    return render_template("index.html", meals=meals)

if __name__ == "__main__":
    app.run(debug=True)
