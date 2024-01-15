from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from ..serializers import AuthorSerializer

class AuthorViewSet(ReadOnlyModelViewSet):
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        User = get_user_model()
        qs = User.objects.filter(id=self.request.user.id)
        return qs
    
    @action(methods=['get'],detail=False,)
    def me(self, request, *args, **kwargs):
        obj = self.get_queryset().first()
        serializer = self.get_serializer(
            instance = obj
        )
        return Response(serializer.data)