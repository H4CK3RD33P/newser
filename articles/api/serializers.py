from rest_framework import serializers
from articles.models import Article, Author

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Article
        exclude = ('id',)

    def validate(self,data):
        if data['title']==data['description']:
            raise serializers.ValidationError("Title and description must be different")
        else:
            return data

class AuthorSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(read_only=True,many=True,view_name="detail_article")
    class Meta:
        model = Author
        fields = "__all__"

    def validate(self,data):
        if data['first_name']==data['last_name']:
            raise serializers.ValidationError("First and last name must be different")
        else:
            return data