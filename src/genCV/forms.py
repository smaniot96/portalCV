
from django import forms

class CVGeneratorForm(forms.Form):
    name = forms.CharField()
    job_title = forms.CharField()
    experience = forms.CharField(widget=forms.Textarea)
    job_description = forms.CharField(widget=forms.Textarea)
    generate_type = forms.ChoiceField(choices=[('cv', 'CV'), ('cover', 'Cover Letter')])
