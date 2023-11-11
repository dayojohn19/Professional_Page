from django.contrib import admin

# Register your models here.
from .models import Chat_Messages_Model, Chat_Room_Model

admin.site.register(Chat_Messages_Model)
admin.site.register(Chat_Room_Model)