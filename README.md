# GemmaFlow AI — Less busywork. More brilliant work.

GemmaFlow AI is a clean, friendly AI productivity workspace powered by **Gemma 4**. It helps students, makers, and professionals turn rough input into useful output in seconds.

## Features
- **Quick Summary** — distill long text into key points
- **Email Writer** — transform notes into polished emails
- **Task Planner** — turn goals into prioritized action steps
- **Tone Improver** — rewrite text in a chosen style
- **Idea Spark** — brainstorm practical ideas
- Responsive UI with copy-to-clipboard
- Python Flask backend keeps the API key out of browser JavaScript

## AI model
- **Gemma 4 26B A4B Instruct** (`gemma-4-26b-a4b-it`)
- Accessed through the Google Gen AI Python SDK / Gemini API
- Set `GEMMA_MODEL` in `.env` to use another supported Gemma model.

## Tech stack
Python · Flask · HTML5 · CSS3 · JavaScript · Google Gen AI SDK · Gemma 4

## Run locally

### 1. Requirements
Python 3.10+ and a Google AI Studio API key. Create/get a key at https://aistudio.google.com/apikey

### 2. Install
```bash
# Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### 3. Configure `.env`
Open `.env` and paste your API key:
```env
GEMINI_API_KEY=your_google_ai_studio_api_key_here
GEMMA_MODEL=gemma-4-26b-a4b-it
```

### 4. Start
```bash
python app.py
```
Visit http://127.0.0.1:5000

## Security note
Keep `.env` private. Never commit your API key to GitHub. The Flask backend reads the key from environment variables; the frontend never receives it. For public deployment, configure environment variables in your hosting provider and use HTTPS.

## Project structure
```
GemmaFlow_AI/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Use responsibly
AI-generated output may contain errors. Review it before sending, publishing, or relying on it.
