from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django import forms
from django.contrib.auth.models import User 
from .models import Post


class UserSignUpForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name'}
         
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                   'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.TextInput(attrs={'class':'form-control'}),

                   
                   }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label= 'username', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label= 'password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','password']
        labels = {"username": 'UserName' , "password":'Password'}


class AdPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title' , 'desc']
        labels = {'title':'Title', 'desc':'descriptions'}
        widgets = {'title':forms.Textarea(attrs={'class':'form-control'})}
        widgets = {'desc':forms.Textarea(attrs={'class':'form-control'})}