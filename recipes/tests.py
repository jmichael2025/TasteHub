
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Category, Recipe


class RecipeModelTest(TestCase):


    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )

        self.category = Category.objects.create(
            name="Dinner"
        )

        self.recipe = Recipe.objects.create(
            name="Test Chicken Curry",
            description="A simple test recipe.",
            ingredients="Chicken, curry powder, onion",
            instructions="Cook the ingredients together.",
            category=self.category,
            author=self.user
        )

    def test_recipe_is_created_correctly(self):
        self.assertEqual(self.recipe.name, "Test Chicken Curry")
        self.assertEqual(self.recipe.category.name, "Dinner")
        self.assertEqual(self.recipe.author.username, "testuser")


class HomePageTest(TestCase):
    

    def test_home_page_loads(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/index.html")


class AuthenticationTest(TestCase):
    

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )

    def test_login_works(self):
        
        response = self.client.post(
            "/accounts/login/",
            {
                "username": "testuser",
                "password": "TestPassword123!"
            }
        )

        self.assertEqual(response.status_code, 302)

    def test_dashboard_requires_login(self):
        response = self.client.get("/dashboard/")

        self.assertEqual(response.status_code, 302)


class RecipeViewTest(TestCase):
    

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!"
        )

        self.category = Category.objects.create(
            name="Dinner"
        )

    def test_recipe_creation(self):
        
        self.client.login(
            username="testuser",
            password="TestPassword123!"
        )

        response = self.client.post(
            "/create-recipe/",
            {
                "name": "Test Pasta",
                "description": "A test pasta recipe.",
                "ingredients": "Pasta, tomato sauce",
                "instructions": "Cook the pasta and add the sauce.",
                "category": self.category.id
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Recipe.objects.filter(name="Test Pasta").exists()
        )
