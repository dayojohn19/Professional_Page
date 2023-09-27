from django.urls import path, re_path
from . import views
app_name='chats'
urlpatterns = [
    path('',views.lobby),
    # re_path(r'^(?P<room_name>[^/]+)/$', views.enter_room, name='room'),
    path('<str:room_name>/',views.enter_room,name='room'),
    # re_path(r'^(?P<room_name>[^/]+)/$', views.enter_room, name='room'),
]