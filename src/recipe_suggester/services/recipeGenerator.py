from django.conf import settings
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
def generate_italian_recipe(ingredients: str, mood: str) -> str:
    prompt = (
        f"You are a master Italian chef. Based on these ingredients: {ingredients}, "
        f"and the user's current mood: '{mood}', suggest one delicious Italian recipe. "
        f"Include a title, ingredients list, and step-by-step instructions."
    )
    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
    except Exception as e:
        return f"❌ Error generating text: {e}"

    return response.choices[0].message.content

