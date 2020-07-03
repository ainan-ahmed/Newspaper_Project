from django.shortcuts import render
from django.views.generic import (CreateView,DeleteView,DetailView,
                                  UpdateView,ListView,TemplateView,FormView)
from articles.models import Article,Category,Comment
from articles.forms import CommentForm
from taggit.models import Tag
# Create your views here.
class Home(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'pages/home.html'
    paginate_by = 3
    queryset = Article.published_article.all()
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
    paginate_by = 2
class Tagged(DetailView):
    template_name = 'pages/tag.html'
    model = Tag 
    paginate_by = 2
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #tmp = Tag.objects.filter(pk=self.kwargs['slug'])
        context['articles'] = Article.published_article.filter(
            tags__id=self.kwargs['pk'])
        return context
def tag(request,tag_slug = None):
    pass



