from flask import Flask, request, jsonify
from flask_cors import CORS
from services.ai_service import generate_feasibility
import random

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "MarketMind Backend Running 🚀"

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    business = data.get("business")
    location = data.get("location")
    budget = data.get("budget")
    target = data.get("target")
    price = data.get("price")

    ai_report = generate_feasibility(business, location, budget, target, price)

    viability_score = random.randint(70, 95)

    return jsonify({
        "report": ai_report,
        "viability_score": viability_score
    })

if __name__ == "__main__":
    app.run(debug=True)
