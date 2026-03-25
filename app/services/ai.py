import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def generate_quest(level):
    prompt = f"Create a DnD quest for level {level}"
    return model.generate_content(prompt).text