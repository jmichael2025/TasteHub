from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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