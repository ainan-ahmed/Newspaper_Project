from django.shortcuts import render
from django.views.generic import (CreateView,DeleteView,DetailView,
                                  UpdateView,ListView,TemplateView)
from articles.models import Article
# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    