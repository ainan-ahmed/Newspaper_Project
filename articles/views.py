from django.shortcuts import render, redirect
from .forms import ArticleCreateForm, CommentForm
from .models import Category, Article, Comment
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView, DetailView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import FormMixin


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/article_list.html'
    paginate_by = 3


class ArticleDetailView(FormMixin, DetailView):
    model = Article
    template_name = 'articles/article_details.html'
    form_class = CommentForm
    def get_success_url(self):
        #id = self.object.kwargs['id']
        return reverse_lazy('articles:details', args=[self.object.id])
        #return reverse('home')
        #return redirect('article:details',article_id = self.object.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = context['article'].comments.filter(active=True)
        context['comment_form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        new_comment.article = self.object
        new_comment.save()
        return super(ArticleDetailView, self).form_valid(form)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'articles/article_create.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'articles/article_update.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    form_class = ArticleCreateForm
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
