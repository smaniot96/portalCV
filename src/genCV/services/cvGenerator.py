# generator/services/cvGenerator.py

from django.conf import settings
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def generate_cv_or_cover_letter(name, job_title, experience, job_description, generate_type):
    prompt = (
        f"Generate a {generate_type} for someone named {name}, applying for a position as {job_title}. "
        f"Here is their experience:\n{experience}\n"
        f"Here is the job description:\n{job_description}"
    )

    try:
        chat_completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"❌ Error generating text: {e}"