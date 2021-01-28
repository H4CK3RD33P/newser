from django.urls import path
from .views import all_articles
urlpatterns = [
    path('all/',all_articles,name='all_articles'),
]