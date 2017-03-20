from django.contrib.auth.forms import AuthenticationForm
from django import forms
from blog.models import Blog

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class PostForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'body',)

class SignUpForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
    email = forms.EmailField(label="Email",max_length=100,
                                widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}))