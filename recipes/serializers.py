# flake8: noqa
from rest_framework import serializers

class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=65)
    description = serializers.CharField(max_length=165)
    public = serializers.BooleanField(source='is_published')
    preparation = serializers.SerializerMethodField()

    def get_preparation(self,obj):
        return f'{obj.preparation_time} {obj.preparation_time_unit}'