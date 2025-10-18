# Django Project: CV Generator & Recipe Finder with OpenAI API

This Django-based project contains two apps that leverage OpenAI’s API with a free large language model (LLM) to generate dynamic outputs based on user input:

## 🛠️ Project Overview

- **CV Generator App**  
  Allows users to fill out a form with personal and professional details, then generates a customized CV using an OpenAI-powered LLM.

- **Recipe Finder App**  
  Users provide a list of ingredients, and the app uses OpenAI’s LLM to generate recipe suggestions dynamically.

Both apps interact with the OpenAI API to generate text outputs.

## ⚙️ Features

- Interactive form for CV creation with immediate AI-generated results
- Ingredient-based recipe generation powered by AI
- Django backend handling form submissions, API requests, and response rendering
- Modular apps for easy maintenance and scalability

<!-- ## 📁 Project Structure

myproject/
│
├── cv_generator/ # App for CV creation
│
├── recipe_finder/ # App for recipe generation
│
├── myproject/ # Project settings and URLs
│
├── templates/ # HTML templates for both apps
│
├── static/ # CSS, JS, images
│
├── manage.py # Django management script
└── README.md # Project documentation (this file) -->




## 🚀 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/smaniot96/portalCV.git
cd portalCV
```

2. **Activate virtual environment**

```bash
python -m venv venv
source venv/bin/activate
```

3. **Install requirements**

```bash
pip install -r requirements.txt

```

Create a .env file in the main project folder:
```bash
DEBUG=True
SECRET_KEY = replace_me
ALLOWED_HOSTS=localhost,127.0.0.1
OPENAI_API_KEY=sk-xxxxxxxYOURKEYxxxxxxxx
GROQ_API_KEY= sk-xxxxxxxYOURKEYxxxxxxxx
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Start development server**
```bash
python manage.py runserver
```

6. **PortalCV endpoints**
```bash
/genCV

/recipe_suggester
```





