# flake8: noqa
from rest_framework import serializers
from django.contrib.auth.models import User

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=65)

class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugField()

class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=65)
    description = serializers.CharField(max_length=165)
    public = serializers.BooleanField(source='is_published')
    preparation = serializers.SerializerMethodField(method_name='any_method_name')

    category = serializers.StringRelatedField()
    # category = CategorySerializer(many=False)
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all(),
    # )

    author = serializers.PrimaryKeyRelatedField(
        queryset= User.objects.all()
    )

    tags = TagSerializer(many=True)
    # tags = serializers.StringRelatedField(many=True)

    def any_method_name(self,obj):
        return f'{obj.preparation_time} {obj.preparation_time_unit}'