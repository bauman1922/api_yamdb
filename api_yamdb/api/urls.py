from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, SignUpView, TokenObtainView


router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('api/v1/auth/signup/', SignUpView.as_view()),
    path('api/v1/auth/token/', TokenObtainView.as_view()),
    path("api/v1/", include(router.urls)),
]
