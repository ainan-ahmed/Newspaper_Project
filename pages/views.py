from django.shortcuts import render
from django.views.generic import (CreateView,DeleteView,DetailView,
                                  UpdateView,ListView,TemplateView,FormView)
from articles.models import Article,Category,Comment
from articles.forms import CommentForm
# Create your views here.
class Home(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'pages/home.html'
    paginate_by = 3
    
    def get_queryset(self):
        temp =  super().get_queryset()
        return temp.order_by('views').reverse()

class About(TemplateView):
    template_name = 'pages/about.html'

class Contact(TemplateView):
    template_name = 'pages/contact.html'
    
class Category(DetailView):
    template_name = 'pages/category.html'
    model = Category



