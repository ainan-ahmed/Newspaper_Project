from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,DeleteView,DetailView,UpdateView,ListView
# Create your views here.
from .forms import CustomUserChangeForm,CustomUserCreationForm

class Register(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'users/register.html'

class Login(CreateView):
    print('helo')
    
