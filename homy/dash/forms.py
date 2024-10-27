from django import forms # type: ignore
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.models import User # type: ignore

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'form-control py-2'
    }))  
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class':'form-control'
    }))



class SinupForm(UserCreationForm ):

    class Meta:
        model = User
        fields=('username','password1','password2')


    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'form-control py-2'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password',
        'class':'form-control py-2'
    })) 
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'confirm your password',
        'class':'form-control py-2'

    }))   