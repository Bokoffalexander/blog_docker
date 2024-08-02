from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User

# Для Blog - GET и POST 
class BlogSerializer(serializers.ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(source='owner.id', read_only=True)
    owner = serializers.PrimaryKeyRelatedField(source='owner.username', read_only=True)


    class Meta:
        model = Blog
        fields = "__all__"

# Для Blog - PATCH
class BlogSerializerPatch(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    is_published = serializers.BooleanField(required=False)

    owner_id = serializers.PrimaryKeyRelatedField(source='owner.id', read_only=True)
    owner = serializers.PrimaryKeyRelatedField(source='owner.username', read_only=True)

    class Meta:
        model = Blog
        fields = "__all__"

