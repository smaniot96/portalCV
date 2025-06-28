from django.shortcuts import render
from recipe_suggester.forms import RecipeRequestForm
from recipe_suggester.services.recipeGenerator import generate_italian_recipe

def suggest_recipe_view(request):
    recipe = None
    if request.method == "POST":
        form = RecipeRequestForm(request.POST)
        if form.is_valid():
            ingredients = form.cleaned_data['ingredients']
            mood = form.cleaned_data['mood']
            recipe = generate_italian_recipe(ingredients, mood)
    else:
        form = RecipeRequestForm()

    return render(request, "recipe_suggester/suggest.html", {
        "form": form,
        "recipe": recipe
    })