from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput({
        "placeholder":"Your user name"
    }))

    password = forms.CharField(widget=forms.PasswordInput({
        "placeholder":"Password"
    }))



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    username = forms.CharField(widget=forms.TextInput({
        "placeholder":"Your user name"
    }))

    email = forms.CharField(widget=forms.EmailInput({
        "placeholder":"Your email"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput({
        "placeholder":"Password"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput({
        "placeholder":"Repeat password"
    }))
