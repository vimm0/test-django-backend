from rest_framework import viewsets

from apps.blog.models import Article
from apps.blog.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
