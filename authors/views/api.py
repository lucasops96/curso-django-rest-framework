from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import AuthorSerializer

class AuthorViewSet(ReadOnlyModelViewSet):
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        User = get_user_model()
        qs = User.objects.filter(id=self.request.user.id)
        return qs
    