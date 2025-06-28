# forms.py
from django import forms

class RecipeRequestForm(forms.Form):
    ingredients = forms.CharField(widget=forms.Textarea, help_text="List what's in your fridge")
    mood = forms.CharField(help_text="How are you feeling? (e.g. tired, romantic, sad...)")
