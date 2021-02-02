from rest_framework import serializers
from articles.models import Article, Author

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Article
        exclude = ('id',)

class AuthorSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(read_only=True,many=True,view_name="detail_article")
    class Meta:
        model = Author
        fields = "__all__"

    #def articles(self,instance):
     #   return serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name="detail_article")