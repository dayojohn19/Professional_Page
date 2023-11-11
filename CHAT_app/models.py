
from django.db import models
from django.urls import reverse
# Create your models here.
# from datetime import datetime


class Chat_Room_Model(models.Model):
    admin_ID = models.CharField(max_length=10,blank=True,null=True)
    admin_name = models.CharField(max_length=64,blank=True,null=True)
    chat_room_name = models.CharField(max_length=128)
    chatroom_messages = models.ManyToManyField('CHAT_app.Chat_Messages_Model',blank=True, related_name='chat_model_room')
    @property
    def messages_items(self):
        return self.chatroom_messages.all()
    def __str__(self):
        return f'{self.chat_room_name}, '
class Chat_Messages_Model(models.Model):
    sender_ID = models.CharField(max_length=32)
    sender_name = models.CharField(max_length=32)
    sender_image = models.URLField(blank=True)
    sender_chat_message = models.TextField(blank=True,null=True)
    chat_room_model = models.ForeignKey('CHAT_app.Chat_Room_Model',on_delete=models.CASCADE,null=True)
    message_timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.chat_room_model}: {self.sender_chat_message}'    