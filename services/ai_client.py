import os
import json
from dotenv import load_dotenv

load_dotenv()

AI_PROVIDER = os.getenv("AI_PROVIDER", "groq")
MODEL_NAME = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

if AI_PROVIDER == "groq":
    from groq import Groq
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
else:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_resume(text: str):

    prompt = f"""
    Analyze the resume and return a JSON object with the following fields:
    summary (string),
    strengths (array of strings),
    weaknesses (array of strings),
    missing_keywords (array of strings),
    ats_score (integer between 0 and 100),
    improvement_suggestions (array of strings).

    Resume:
    {text}
    """

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You are a resume analysis engine. Always respond ONLY with valid JSON. No explanations."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            response_format={"type": "json_object"} 
        )

        content = response.choices[0].message.content
        return json.loads(content)

    except Exception as e:
        return {
            "error": "AI processing failed",
            "details": str(e)
        }