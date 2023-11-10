# flake8: noqa
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from tag.models import Tag
from ..models import Recipe
from ..serializers import RecipeSerializer, TagSerializer

class RecipeAPIv2Pagination(PageNumberPagination):
    page_size = 3

class RecipeAPIv2List(ListCreateAPIView):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2Pagination
    # def get(self, request):
    #     recipes = Recipe.objects.get_published()[:10]
    #     serializer = RecipeSerializer(
    #         instance=recipes,
    #         many=True,
    #         context={'request':request}
    #     )
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = RecipeSerializer(
    #         data=request.data
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(
    #         serializer.data,
    #         status=status.HTTP_201_CREATED
    #     )


class RecipeAPIv2Detail(APIView):
    def get_recipe(self,pk):
        recipe = get_object_or_404(
            Recipe.objects.all(),
            pk=pk
        )
        return recipe
    
    def get(self, request, pk):
        recipe = self.get_recipe(pk)
        serializer = RecipeSerializer(
            instance=recipe, 
            many=False,
            context={'request':request}
        )
        return Response(serializer.data) 

    def patch(self, request, pk):
        recipe = self.get_recipe(pk)
        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            many=False,
            context={'request':request},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        recipe = self.get_recipe(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(http_method_names=['get','post'])
# def recipe_api_list(request):
#     if request.method == 'GET':
#         recipes = Recipe.objects.get_published()[:10]
#         serializer = RecipeSerializer(
#             instance=recipes,
#             many=True,
#             context={'request':request}
#         )
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = RecipeSerializer(
#             data=request.data
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(
#             serializer.data,
#             status=status.HTTP_201_CREATED
#         )

        

# @api_view(http_method_names=['get','patch','delete'])
# def recipe_api_detail(request,pk):
#     recipe = get_object_or_404(
#         Recipe.objects.get_published(),
#         pk=pk
#     ) 

#     if request.method == 'GET':
#         serializer = RecipeSerializer(
#             instance=recipe, 
#             many=False,
#             context={'request':request}
#         )
#         return Response(serializer.data) 
    
#     elif request.method == 'PATCH':
#         serializer = RecipeSerializer(
#             instance=recipe,
#             data=request.data,
#             many=False,
#             context={'request':request},
#             partial=True,
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         recipe.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#     # recipe = Recipe.objects.get_published().filter(pk=pk).first()
#     # if recipe:
#     #     serializer = RecipeSerializer(instance=recipe, many=False)
#     #     return Response(serializer.data)
#     # else:
#     #     return Response({
#     #         "detail":"Eita, nada encontrado"
#     #     },status=status.HTTP_418_IM_A_TEAPOT)


@api_view()
def tag_api_detail(request,pk):
    tag = get_object_or_404(
        Tag.objects.all(),
        pk=pk
    )

    serializer = TagSerializer(instance=tag,many=False)

    return Response(serializer.data)