from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Donor


class CreateUserForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'ex.: vemba', 'class':'form-control', 'name':'username'
    }))

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'exemplo@mail.com', 'class':'form-control', 'name':'email'
    }))

    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': '8 ou mais digitos', 'class':'form-control', 'name':'password1', 'minlength':8
    }))

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': '8 ou mais digitos', 'class':'form-control', 'name':'password2', 'minlength':8
    }))

    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'ex.: Alfredo Vemba', 'class':'form-control', 'name':'name'
    }))
    
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'ex.: 942738273', 'class':'form-control', 'name':'phone'
    }))

    district = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'ex.: 1 de Maio', 'class':'form-control', 'name':'district'
    }))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone', 'name', 'district']

class DonorForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'ex.: Alfredo Vemba', 'class':'form-control', 'name':'name'
    }))
    
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'ex.: 942738273', 'class':'form-control', 'name':'phone'
    }))

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'exemplo@mail.com', 'class':'form-control', 'name':'email'
    }))
    
    district = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'ex.: 1 de Maio', 'class':'form-control', 'name':'district'
    }))
    
    picture = forms.CharField(required=True, widget=forms.FileInput(attrs={
        'placeholder': 'alterar foto', 'class':'form-control', 'name':'picture'
    }))


    class Meta:
        model = Donor
        fields = ('name', 'phone', 'email', 'group', 'province', 'municipe', 'district', 'picture')

