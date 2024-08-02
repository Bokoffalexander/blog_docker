from .models import Blog
from .serializers import BlogSerializer, BlogSerializerPatch
from rest_framework import serializers
###########
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiExample
from drf_spectacular.utils import inline_serializer
from drf_spectacular.types import OpenApiTypes

############### Ограничения
# Блог - Ограничения на изменить запись, удалить запись
# прописаны в методах PUT и DELETE
###############

########### class - Список юзеров
class ListUsers(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    @extend_schema(
        tags=["GET"],
        summary="Получить список юзеров (без сериализации) (Админ+Token)",
        )
    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
###########

########### class Блог - GET, POST, PUT, DELETE 
class BlogAPIView(APIView):
    ########### GET получить список записей 
    ########### POST добавить запись
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    @extend_schema(
        tags=["GET"],
        summary="Получить весь список постов",
        )
    def get(self, request):
        b = Blog.objects.all()
        serializer = BlogSerializer(b, many=True)
        return Response({'posts': serializer.data})
    
    @extend_schema(
    summary="Отправить пост: {title*, content[not required], is_published*}",
    request=BlogSerializer,
    methods=["POST"]
    )
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response({'post': serializer.data}, status=status.HTTP_201_CREATED)
##############
##############
class BlogAPIView2(APIView):
############## PATCH изменить запись
############## DELETE удалить запись
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    @extend_schema(
    summary="Изменить пост: все поля [not required]",
    request=BlogSerializerPatch,
    methods=["patch"]
    )
    def patch(self, request, *args, **kwargs):
        PK = kwargs.get("pk", None)
        if not PK:
            return Response({"error": "Method PATCH not allowed"})

        try:
            instance = Blog.objects.get(pk=PK)
        except:
            return Response({"error": "Object does not exist"})

        if (instance.owner==request.user) or (request.user.is_staff):
            pass
        else:
            return Response({"error": "You can't PATCH this obj, isn't yours."})

        serializer = BlogSerializerPatch(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data}, status=status.HTTP_202_ACCEPTED)
    
    @extend_schema(
    summary="Удалить пост",
    request=BlogSerializer,
    methods=["DELETE"]
    )
    def delete(self, request, *args, **kwargs):
        PK = kwargs.get("pk", None)
        if not PK:
            return Response({"error": "Method DELETE not allowed"})

        try:
            instance = Blog.objects.get(pk=PK)
        except:
            return Response({"error": "Object does not exist"})

        if (instance.owner==request.user) or (request.user.is_staff):
            pass
        else:
            return Response({"error": "You can't DELETE this obj, isn't yours."})

        instance.delete()
        return Response({"post": "delete post " +str(PK)})
############### КОНЕЦ
