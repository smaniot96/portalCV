from django import forms

class CVGeneratorForm(forms.Form):
    # --- Basic Info ---
    name = forms.CharField(label="Full Name", max_length=100)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone", max_length=50, required=False)
    linkedin = forms.URLField(label="LinkedIn URL", required=False)
    github = forms.URLField(label="GitHub URL", required=False)
    google_scholar = forms.URLField(label="Google Scholar URL", required=False)

    # --- Summary / Job Title ---
    job_title = forms.CharField(label="Current Job Title", max_length=200, required=False)

    # --- Work Experience ---
    work_experience = forms.CharField(
        label="Work Experience",
        widget=forms.Textarea(attrs={"rows": 6, "placeholder": "Example:\n2021–2025: Researcher, University of Nottingham, UK\n- Analyzed 15 TB of data\n- Published in Nature\n- Supervised students"}),
        help_text="List each experience with years, role, organization, and bullet points."
    )

    # --- Education ---
    education = forms.CharField(
        label="Education",
        widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Example:\nPhD in Mathematical Physics, University of Nottingham (2021–2025)\nMSc Theoretical Physics, Trieste (2018–2020, 110/110 cum laude)"}),
        help_text="List degrees, institutions, and years.",
        required=False
    )

    # --- Certificates ---
    certificates = forms.CharField(
        label="Certificates",
        widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Example:\nIBM Data Science Specialization (Coursera, 2025–ongoing)\nMeta Back-End Developer Specialization (Coursera, 2025)"}),
        required=False
    )

    # --- Languages ---
    languages = forms.CharField(
        label="Languages",
        widget=forms.Textarea(attrs={"rows": 2, "placeholder": "Example: Italian (native), English (C2), Spanish (B1)"}),
    )

    # --- Publications ---
    publications = forms.CharField(
        label="Publications",
        widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Example:\n2024 – Rotating curved spacetime signatures from a giant quantum vortex, Nature"}),
        required=False
    )

    # --- Type (for selecting template or format) ---
    Type = forms.ChoiceField(
        choices=[('cv', 'CV')],
        label="Document Type"
    )