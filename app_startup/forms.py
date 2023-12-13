from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Startup


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')



class startup(forms.ModelForm):
    StartupName=forms.CharField(label='StartupName', widget=forms.TextInput(attrs={'class':'form-control'}) )
    firm = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    firm = forms.ChoiceField(choices=[('Tech', 'Technology'), ('marketing', 'Marketing'), ('firm', 'Financial technology'), ('Design', 'Design'),], widget=forms.Select())

    Description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    socialmedialink = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Funding_Status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  
    class Meta:
        model = Startup

        fields = ['StartupName', 'firm', 'Description','Address','email','socialmedialink','Funding_Status',]
        firm = forms.ChoiceField(choices=[('tech', 'Tech'), ('marketing', 'Marketing'), ('firm', 'Financial technology'), ('Design', 'Design'),], widget=forms.Select())





       
