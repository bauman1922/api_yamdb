from rest_framework import mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .permissions import IsAdminOrReadOnly


class SimpleViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = LimitOffsetPagination
