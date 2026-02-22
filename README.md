

#  AI Career Assistant – AI Service

FastAPI-based microservice responsible for AI processing.

This service handles:

- Resume text analysis
- Skill extraction
- Career path prediction
- Course recommendation logic
- Job matching logic

---

##  Tech Stack

- Python 3.x
- FastAPI
- Uvicorn
- AI/ML models
- External APIs (if applicable)

---

##  Service Architecture

This service is independent and communicates via HTTP with the Django backend.

It runs on:


http://localhost:8001


---

##  Available Endpoints


POST /analyze


(Actual routes may vary based on implementation)

---

##  Environment Variables (.env)

AI_PROVIDER=groq
GROQ_API_KEY=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
GROQ_MODEL=llama-3.1-8b-instant


---

##  Local Setup


python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8001

Service runs at:

http://localhost:8001

Responsibilities

AI processing

ML model execution

Analyzing Resume

