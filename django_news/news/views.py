from rest_framework import permissions, viewsets
from rest_framework.generics import CreateAPIView
from .serializers import NewsSerializer, UserSerializer
from .models import News


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NewsSerializer


class UserCreateApiView(CreateAPIView):
    serializer_class = UserSerializer
