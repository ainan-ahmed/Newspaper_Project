from django.urls import path
from . import views
from .sitemaps import ArticleSitemap
from .feeds import LatestArticlesFeed
from django.contrib.sitemaps.views import sitemap
app_name = 'articles'

sitemaps = {
    'articles': ArticleSitemap,
}
urlpatterns = [
    path('',views.ArticleListView.as_view(),name='list'),
    path('<uuid:pk>',
         views.ArticleDetailView.as_view(), name='details'),
    path('<uuid:pk>/edit', views.ArticleUpdateView.as_view(), name='edit'),
    path('<uuid:pk>/delete', views.ArticleDeleteView.as_view(), name='delete'),
    path('create',views.ArticleCreateView.as_view(),name = 'create'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('feed', LatestArticlesFeed(), name="feed"),
    path('search', views.article_search,name = "search"),
    path('react', views.react, name ="react")
    
]
