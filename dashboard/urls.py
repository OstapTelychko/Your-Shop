from django.urls import path

from .views import user_home

app_name = "dashboard"

urlpatterns = [
    path("", user_home, name="user home")
]