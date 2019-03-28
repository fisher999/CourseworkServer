from django import forms

class RegisterForm(forms.Form):
    login = forms.CharField(label="login", max_length=100)
    password = forms.CharField(label="password", max_length=100)