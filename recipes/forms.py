from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Recipe

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=150,
        required=True,
        label='First Name'
    )

    last_name = forms.CharField(
        max_length=150,
        required=True,
        label='Last Name'
    )

    email = forms.EmailField(
        required=True,
        label='Email address'
    )

    class Meta:
        model = User
        fields = ['first_name', 
                  'last_name', 
                  'username', 
                  'email', 
                  'password1', 
                  'password2'
                  ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control w-100",
            "placeholder": "Choose a username"
        })

        self.fields["first_name"].widget.attrs.update({
            "class": "form-control w-100",
            "placeholder": "Enter your first name"
        })

        self.fields["last_name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Enter your last name"
        })

        self.fields["email"].widget.attrs.update({
            "class": "form-control w-100",
            "placeholder": "Enter your email address"
        })

        self.fields["password1"].widget.attrs.update({
            "class": "form-control w-100",
            "placeholder": "Create a password"
        })

        self.fields["password2"].widget.attrs.update({
            "class": "form-control w-100",
            "placeholder": "Confirm your password"
        })

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 
                  'description', 
                  'ingredients', 
                  'instructions', 
                  'category'
                  ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Enter recipe name"
        })

        self.fields["description"].widget.attrs.update({
            "class": "form-control",
            "rows": 3,
            "placeholder": "Describe your recipe"
        })

        self.fields["ingredients"].widget.attrs.update({
            "class": "form-control",
            "rows": 5,
            "placeholder": "List the ingredients"
        })

        self.fields["instructions"].widget.attrs.update({
            "class": "form-control",
            "rows": 6,
            "placeholder": "Describe how to prepare the recipe"
        })

        self.fields["category"].widget.attrs.update({
            "class": "form-select"
        })

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Enter your username"
        })

        self.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Enter your password"
        })

        