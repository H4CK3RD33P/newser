from rest_framework import serializers
from articles.models import Article, Author

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('id',)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ('id',)