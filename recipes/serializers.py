# flake8: noqa
from collections import defaultdict

from django.contrib.auth.models import User
from rest_framework import serializers

from authors.validators import AuthorRecipeValidator
from tag.models import Tag

from .models import Recipe


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=65)

class TagSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # name = serializers.CharField(max_length=255)
    # slug = serializers.SlugField()
    class Meta:
        model = Tag
        fields = ['id','name','slug']

class RecipeSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=65)
    # description = serializers.CharField(max_length=165)
    class Meta:
        model = Recipe
        fields = [
            'id','title','description','author',
            'category','tags','public','preparation',
            'tags_objects','tags_links','preparation_time',
            'preparation_time_unit', 'servings', 'servings_unit',
            'preparation_steps', 'cover'
            ]

    public = serializers.BooleanField(
        source='is_published',
        read_only=True,    
    )
    preparation = serializers.SerializerMethodField(
        method_name='any_method_name',
        read_only=True,
    )
    category = serializers.StringRelatedField(read_only=True)
    # category = CategorySerializer(many=False)
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all(),
    # )

    # author = serializers.PrimaryKeyRelatedField(
    #     queryset= User.objects.all()
    # )

    # tags = serializers.StringRelatedField(many=True)
    tags_objects = TagSerializer(
        many=True,
        source='tags',
        read_only=True,
    )
    tags_links = serializers.HyperlinkedRelatedField(
        many=True,
        source='tags',
        # queryset=Tag.objects.all(),
        view_name='recipes:recipes_api_v2_tag',
        read_only=True,
    )

    def any_method_name(self,obj):
        return f'{obj.preparation_time} {obj.preparation_time_unit}'
    
    def validate(self, attrs):
        super_validate = super().validate(attrs)
        AuthorRecipeValidator(data=attrs,ErrorClass=serializers.ValidationError)
        return super_validate
    
  