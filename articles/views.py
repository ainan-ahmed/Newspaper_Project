from django.shortcuts import render,redirect
from .forms import ArticleCreateForm
from .models import Category,Article
from django.views.generic import (ListView,CreateView,
                                  UpdateView,DeleteView,DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name  = 'articles/article_list.html'
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_details.html'
    
class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'articles/article_create.html'
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'articles/article_update.html'
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    form_class = ArticleCreateForm
    success_url = reverse_lazy('home')
    
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)