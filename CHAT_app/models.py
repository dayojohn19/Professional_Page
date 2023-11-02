from django.db import models
from django.urls import reverse
# Create your models here.
from datetime import datetime


class Chat_Room(models.Model):
    admin_ID = models.CharField(max_length=10)
    admin_name = models.CharField(max_length=64)
    chat_room_name = models.CharField(max_length=128)
    chatroom_messages = models.ManyToManyField('CHAT_app.Chat_Messages',blank=True, related_name='chat_model_room')
    @property
    def messages_items(self):
        return self.chatroom_messages.all()

class Chat_Messages(models.Model):
    sender_ID = models.CharField(max_length=32)
    sender_name = models.CharField(max_length=32)
    sender_image = models.URLField(blank=True)
    sender_chat_message = models.TextField(blank=True)
    chat_room_model = models.ForeignKey('CHAT_app.Chat_Room',on_delete=models.CASCADE,null=True)
    message_timestamp = models.DateTimeField(auto_now_add=True)