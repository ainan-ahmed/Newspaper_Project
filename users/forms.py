from django import forms
#from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
#from .models import CustomUser
years = [x for x in range(1940, 2021)]


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=20, required=True, label='First Name', widget=forms.TextInput(
        attrs={'placeholder': 'Enter your First Name'}))
    last_name = forms.CharField(max_length=20, required=True, label='Last Name', widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Last Name'}))
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=years))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.save()
        return user

# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields + ('date_of_birth','first_name','last_name','email',)
#         widgets = {
#             'date_of_birth':forms.SelectDateWidget(years=years),
#             'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
#             'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
#             'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
#             'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}),
#             'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}),
#             'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'})
#         }

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = UserChangeForm.Meta.fields
