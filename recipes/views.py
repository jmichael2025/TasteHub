from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipe_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
