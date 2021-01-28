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

@api_view(['GET','PUT','DELETE'])
def detail_article(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response({"error":{
            "code":404,
            "message": "Article not found!"
        }}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
