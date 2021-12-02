from django.urls import path
from .views import AboutUserAPIView


urlpatterns = [
    path("about_user/", AboutUserAPIView.as_view(), name="about_user"),
]