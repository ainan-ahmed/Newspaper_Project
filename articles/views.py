from django.shortcuts import render, redirect
from .forms import ArticleCreateForm, CommentForm, SearchForm
from .models import Category, Article, Comment
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView, DetailView, FormView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import FormMixin
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from common.decorators import ajax_required
from django.core.paginator import (Paginator, EmptyPage, 
                                   PageNotAnInteger)

@ajax_required
@login_required
@require_POST
def react(request):
    article_id = request.POST.get('id')
    action = request.POST.get('action')
    if article_id and action:
        try:
            article = Article.objects.get(id=article_id)
            if action == "like":
                article.users_like.add(request.user)
            else:
                article.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})    
        except:
            pass    
    return JsonResponse({'status':'error'})

def article_list_with_ajax_pagination(request):
    articles = Article.published_article.all()
    paginator = Paginator(articles, 1)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        articles = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # If the request is AJAX and the page is out of range
            # return an empty page
            return HttpResponse('')
        # If page is out of range deliver last page of results
        articles = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                        'pages/list_ajax.html',
                        {'articles': articles})
    return render(request,
                    'pages/home.html',
                    {'articles': articles})

    
    

def article_search(request):
    form = SearchForm()
    query = None
    result = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            search_vector = SearchVector('title', weight='A') + \
                SearchVector('body', weight='A') + \
                SearchVector('author', weight='A')
            query = form.cleaned_data['query']
            search_query = SearchQuery(query)
            result = Article.published_article.annotate(
                search=search_vector, rank=SearchRank(search_vector, search_query)).filter(rank__gte=0.3) \
                .order_by('-rank')

    return render(request, 'articles/search.html', {'form': form, 'query': query, 'result': result})


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
        return reverse_lazy('articles:details', args=[self.object.id])
    
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
