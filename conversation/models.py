from django.contrib.auth.models import User
from django.db import models

from item.models import Items
# Create your models here.


class Conversations(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    item = models.ForeignKey(Items, related_name="conversations", on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="conversations")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Conversations'
        ordering = ("-modified",)



class ConversationMessages(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    conversation = models.ForeignKey(Conversations, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "ConversationMessages"