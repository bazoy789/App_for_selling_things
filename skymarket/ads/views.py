from rest_framework import pagination, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated

from .filters import MyModelFilter
from .models import Ad, Comment
from .permissions import IsStuff, IsOwner
from .serializers import AdSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    serializer_class = AdSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_class = MyModelFilter

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=["get"])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    default_permission = [AllowAny]
    permissions = {
        "retrieve": [IsAuthenticated],
        "update": [IsAuthenticated, IsStuff | IsOwner],
        "partial_update": [IsAuthenticated, IsStuff | IsOwner],
        "destroy": [IsAuthenticated, IsStuff | IsOwner],
    }

    def get_permission(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    default_permission = [AllowAny]

    permissions = {
        "list": [IsAuthenticated],
        "update": [IsAuthenticated, IsStuff | IsOwner],
        "partial_update": [IsAuthenticated, IsStuff | IsOwner],
        "destroy": [IsAuthenticated, IsStuff | IsOwner],
    }

    def get_queryset(self):
        ad_instance = get_object_or_404(Ad, id=self.kwargs["ad.pk"])
        return ad_instance.comment_set.all()

    def get_permission(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]
