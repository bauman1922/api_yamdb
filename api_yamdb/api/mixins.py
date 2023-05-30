from rest_framework import mixins, viewsets

from .permissions import IsAdminOrReadOnly


class SimpleViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    pass

    permission_classes = (IsAdminOrReadOnly,)
