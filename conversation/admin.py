from django.contrib import admin
from .models import Conversations, ConversationMessages

admin.site.register(Conversations)
admin.site.register(ConversationMessages)