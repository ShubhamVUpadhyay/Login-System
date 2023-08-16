from .models import Userinfo
from django import forms
from django.contrib.auth.models import User

class UserinfoForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),help_text=None)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta():
        model=User
        fields=('username','password','email')
        

