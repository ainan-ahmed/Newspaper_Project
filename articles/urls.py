from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('',views.ArticleListView.as_view(),name='list'),
    path('<int:pk>',views.ArticleDetailView.as_view(),name='details'),
    path('<int:pk>/edit',views.ArticleUpdateView.as_view(),name='edit'),
    path('<int:pk>/delete',views.ArticleDeleteView.as_view(),name='delete'),
    path('create',views.ArticleCreateView.as_view(),name = 'create'),
    
]