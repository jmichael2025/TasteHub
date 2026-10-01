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

    return render(
        request,
        'recipes/index.html',
        {
            'recipes': recipes
        }
    )


def api_recipes(request):

    search_term = request.GET.get('search', '')

    if search_term:

        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={search_term}"

        response = requests.get(url)
        data = response.json()

        meals = data.get('meals') or []

        display_meals = meals[:6]

    else:

        display_meals = []

        for _ in range(6):

            response = requests.get(
                "https://www.themealdb.com/api/json/v1/1/random.php"
            )

            data = response.json()

            meal = data.get('meals')

            if meal:
                display_meals.append(meal[0])

    return render(
        request,
        'recipes/api_recipes.html',
        {
            'meals': display_meals,
            'search_term': search_term
        }
    )
    

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

@login_required
def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)

        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, 
                  'recipes/edit_recipe.html', 
                  {'form': form, 'recipe': recipe}
                  )

@login_required
def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('my_recipes')

    return render(request, 
                  'recipes/delete_recipe.html', 
                  {'recipe': recipe}
                  )