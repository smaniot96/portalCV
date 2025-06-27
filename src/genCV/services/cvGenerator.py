# generator/services/cvGenerator.py

from django.conf import settings
import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_cv_or_cover_letter(name, job_title, experience, job_description, generate_type):
    prompt = (
        f"Generate a {generate_type} for someone named {name}, applying for a position as {job_title}. "
        f"Here is their experience:\n{experience}\n"
        f"Here is the job description:\n{job_description}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']
