from django import forms # type: ignore
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.core.validators import RegexValidator # type: ignore

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'form-control p-[5px] mb-[10px] rounded-[10px] bg-transparent border border-lime-700'
    }))  
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class':'form-control p-[5px] mb-[10px] rounded-[10px] bg-transparent border border-lime-700'
    }))



class SinupForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2' , 'phone_number')  # Add phone_number here

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-control p-[5px] mb-[10px] rounded-[10px] bg-transparent border border-lime-700'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'form-control p-[5px] mb-[10px] rounded-[10px] bg-transparent border border-lime-700'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm your password',
        'class': 'form-control p-[5px] mb-[10px] rounded-[10px] bg-transparent border border-lime-700'
    })) 
    phone_number = forms.CharField(
        max_length=15,
        required=False,  # Make it optional (consistent with your model)
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        widget=forms.TextInput(attrs={
            'placeholder': 'Your phone number',
            'class': 'form-control p-[5px] mb-[10px] rounded-[10px] bg-transparent border border-lime-700'
        })
    )