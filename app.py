from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os

app = Flask(__name__)

# -------- OpenAI Client --------
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are Nick NovaBot 🩵
A strict but kind teacher.

You teach ONLY:
Python, SQL, Statistics, Data Science, Machine Learning, AI.

Always explain:
- very simply
- step by step
- with examples
- with mnemonics
- friendly emojis 🩵✨

If user asks something else, say:
"I teach only Data Science topics 🩵"
"""

# -------- Home --------
@app.route("/")
def home():
    return render_template("index.html")

# -------- Chat --------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "Ask me something 🩵"})

    user_message = data["message"]

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.output_text
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({
            "reply": "Something went wrong 🩵 Please try again.",
            "error": str(e)
        }), 500

# -------- Run --------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)






  
    app.run(host="0.0.0.0", port=port)
