import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL = os.getenv("GEMMA_MODEL", "gemma-4-26b-a4b-it")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True) or {}
    task = data.get("task", "summarize")
    text = (data.get("text") or "").strip()
    tone = data.get("tone", "clear and helpful")
    if not text:
        return jsonify({"error": "Please enter some text first."}), 400
    if not API_KEY:
        return jsonify({"error": "GEMINI_API_KEY is missing. Copy .env.example to .env and add your Google AI Studio API key."}), 400
    prompts = {
        "summarize": f"Summarize the following content into concise, useful bullet points. Keep important facts.\n\n{text}",
        "email": f"Turn the following notes into a professional email. Tone: {tone}. Include a subject line.\n\n{text}",
        "tasks": f"Convert the following into an actionable task plan. Provide numbered steps, priorities, and a realistic order.\n\n{text}",
        "rewrite": f"Rewrite the following text to be {tone}. Preserve the meaning and improve clarity.\n\n{text}",
        "ideas": f"Generate 8 practical creative ideas based on this brief. Add a one-line explanation for each.\n\n{text}",
    }
    prompt = prompts.get(task, prompts["summarize"])
    try:
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(model=MODEL, contents=prompt)
        return jsonify({"result": response.text or "The model returned an empty response."})
    except Exception as exc:
        return jsonify({"error": f"AI request failed: {str(exc)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
