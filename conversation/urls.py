from django.urls import path

from .views import new_conversation, inbox, chat


app_name = "conversation"

urlpatterns = [
    path('', inbox, name='inbox'),
    path('<int:id>/', chat, name='chat'),
    path('new/<int:item_id>', new_conversation, name='new'),
]
