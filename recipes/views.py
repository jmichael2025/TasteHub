from django.shortcuts import render
from .models import Recipe
import requests

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def api_recipes(request):
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    data = response.json()
    meal = data['meals'][0]
    return render(request, 'recipes/api_recipes.html', {'meal': meal})