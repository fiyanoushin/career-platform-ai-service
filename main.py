from fastapi import FastAPI
from pydantic import BaseModel
from services.ai_client import analyze_resume

app = FastAPI()

class ResumeRequest(BaseModel):
    resume_text: str

@app.post("/analyze")
def analyze(data: ResumeRequest):
    result = analyze_resume(data.resume_text)
    return result
