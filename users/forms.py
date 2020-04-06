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
        }

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
