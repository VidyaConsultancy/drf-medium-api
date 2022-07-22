from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({ "message": "Articles list", "code": 200, "success": True, "articles": serializer.data })

    def post(self, request):
        article_data = request.data.get('article')
        serializer = ArticleSerializer(data=article_data)
        # if serializer.is_valid(raise_exception=True):
        if serializer.is_valid():
            article_saved = serializer.save()
            return Response({ "message": "Article created successfully", "code": 200, "success": True, "data": article_saved.title }, status=201)

    def put(self, request, pk):
        articles = Article.objects.all()
        saved_article = get_object_or_404(articles, pk=pk)
        article_data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=article_data, partial=True)
        if serializer.is_valid():
            article_updated = serializer.save()
            return Response({ "message": "Article updated successfully", "code": 200, "success": True, "data": article_updated.title })

    def delete(self, request, pk):
        articles = Article.objects.all()
        saved_article = get_object_or_404(articles, pk=pk)
        saved_article.delete()
        return Response({ "message": "Article with {} id is deleted successfully".format(pk)}, status=204)