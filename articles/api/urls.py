from django.urls import path
from .views import *
urlpatterns = [
    path('articles/',all_articles,name='all_articles'),
    path('articles/<int:pk>/',detail_article,name='detail_article'),
    path('authors',all_authors,name='all_authors'),
    path('authors/<int:pk>/',detail_author,name='detail_author'),
]