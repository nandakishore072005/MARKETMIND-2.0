import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_feasibility(business, location, budget, target, price):

    prompt = f"""
    

    Analyze the viability of opening a {business} in {location}.
    
    Investment Budget: ₹{budget}
    Target Customers: {target}
    Expected Price per Unit: ₹{price}

    Provide a concise and structured report (maximum 300 words) including:
    - Market demand analysis
    - Competition overview
    - Risk assessment
    - SWOT summary
    - Strategic recommendation
    """

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "You are an expert business market analyst."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    print("Groq Full Response:",result)
    if "choices" not in result:
      return f"Groq API Error{result}"
    return result["choices"][0]["message"]["content"]
