from django.urls import path
from .views import details, add, remove, edit, search

app_name = "item"

urlpatterns = [
    path('', search, name='search'),
    path('add/', add, name='add'),
    path('<int:id>/', details, name='details'),
    path('<int:id>/remove/', remove, name='remove'),
    path('<int:id>/edit/', edit, name='edit'),
]