from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home.as_view(),name = 'home'),
    path('about',views.About.as_view(),name = 'about'),
    path('contact',views.Contact.as_view(),name = 'contact'),
    path('categories/<int:pk>',views.Category.as_view(),name = 'category'),
   # path('tags/<slug:tag_slug>/',views.tag,name = 'tag'),
    path('tags/<int:pk>', views.Tagged.as_view(), name='tag'),
]
