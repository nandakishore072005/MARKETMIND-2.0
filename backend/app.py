from flask import Flask, request, jsonify
from flask_cors import CORS
from services.ai_service import generate_feasibility
import random
import os

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "MarketMind Backend Running 🚀"


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data received"}), 400

    business = data.get("business")
    location = data.get("location")
    budget = data.get("budget")
    target = data.get("target")
    price = data.get("price")

    if not business or not location or not budget:
        return jsonify({"error": "Missing required fields"}), 400

    ai_report = generate_feasibility(business, location, budget, target, price)

    viability_score = random.randint(70, 95)

    return jsonify({
        "report": ai_report,
        "viability_score": viability_score
    })


# 🔥 Production-ready server (Render compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
