from django.urls import path

from .views import ContactSuccessView, ContactView

app_name = 'contact'

urlpatterns = [
    path('api/v1/auth/signup/', ContactView.as_view(), name="contact"),
    path('success/', ContactSuccessView.as_view(), name="success"),
]
