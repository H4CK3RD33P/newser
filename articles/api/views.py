from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from articles.models import Article

@api_view(['GET','POST'])
def all_articles(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serialzer = ArticleSerializer(articles,many=True)
        return Response(serialzer.data)
    elif request.method == 'POST':
        serialzer = ArticleSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.validated_data, status.HTTP_201_CREATED)
        else:
            return Response(serialzer.validated_data, status.HTTP_400_BAD_REQUEST)