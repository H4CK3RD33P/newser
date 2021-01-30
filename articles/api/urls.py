from django.urls import path
from .views import all_articles
from .views import detail_article
urlpatterns = [
    path('all/',all_articles,name='all_articles'),
    path('all/<int:pk>/',detail_article,name='detail_article'),
]