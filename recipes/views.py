from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RegisterForm, RecipeForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import requests

@login_required
def dashboard(request):
    return render(request, "recipes/dashboard.html")


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
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('dashboard')
    else:
        form = RecipeForm()
    return render(request, 'recipes/create_recipe.html', {'form': form})

@login_required
def my_recipes(request):
    recipes = Recipe.objects.filter(author=request.user)
    return render(request, 
                  'recipes/my_recipes.html',
                    {'recipes': recipes})

@login_required
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
