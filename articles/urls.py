from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('',views.ArticleListView.as_view(),name='list'),
    path('<uuid:pk>',
         views.ArticleDetailView.as_view(), name='details'),
    path('<uuid:pk>/edit', views.ArticleUpdateView.as_view(), name='edit'),
    path('<uuid:pk>/delete', views.ArticleDeleteView.as_view(), name='delete'),
    path('create',views.ArticleCreateView.as_view(),name = 'create'),   
    
]
