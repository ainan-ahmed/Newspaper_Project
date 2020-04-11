from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser
years= [x for x in range(1940,2021)]
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('date_of_birth','first_name','last_name','email',)
        widgets = {
            'date_of_birth':forms.SelectDateWidget(years=years),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'})
        }

class CustomUserChangeForm(UserChangeForm): 
    
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
