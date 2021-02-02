from rest_framework import serializers
from articles.models import Article, Author

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Article
        exclude = ('id',)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ('id',)