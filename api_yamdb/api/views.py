from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from reviews.models import Title, Review
from .serializers import (ReviewSerializer, CommentSerializer)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        new_queryset = title.reviews.all()
        return new_queryset

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentwViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id, title=title)
        return review.comments.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id, title=title)
        serializer.save(author=self.request.user, review=review)
