import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Chat_Room,Chat_Messages
import time
class ChatConsumer(WebsocketConsumer):

    print('NEWNEWNEW')
    def connect(self):
        self.accept() 
        current_room = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = current_room
        
        # When A user Joins the Room
        self.receive([['A Person Joined','Anonymous'],'Name of Persone'])

        self.chatRoom = Chat_Room.objects.get_or_create(chat_room_name=self.room_group_name)[0]

        #  ... Get Regustered User str(self.scope["user"]) 
        self.chat_message([f'\n You Join the room {current_room}','Unregister User'])
        # 
        print('\n\n Messages: ',self.chatRoom.messages_items)
        print('Message: ',self.chatRoom.chat_room_name)
        for i in self.chatRoom.messages_items:
            self.chat_message([i.sender_chat_message,i.sender_name])
            time.sleep(0.3)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        # Creating or Getting ChatRoom


        # self.send(text_data=json.dumps({
        #     'type':'connection_established',
        #     'message':'You are now Connected!'
        # }))
    def get_chat_room(self):
        pass



    def receive(self, text_data):

        try:
            text_data_json = json.loads(text_data)
            message =  text_data_json['message']
            username =  text_data_json['username']
            print('\n Chat messaged')
            new_chat_message = Chat_Messages()
            new_chat_message.sender_ID = username
            new_chat_message.sender_name = username
            new_chat_message.sender_chat_message = message
            new_chat_message.save()
            new_chat_message.chat_room_model = self.chatRoom
            self.chatRoom.chatroom_messages.add(new_chat_message)
            self.chatRoom.save()
            
            # .objects.create(sender_ID=username,sender_name=username,sender_chat_message=message,chat_room_model=self.chatRoom)
            # new_chat_message.save()
            print('\n CHat Saved')
        except:
            message = text_data[0]
            username = text_data[1]
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username
            }
        )
        # self.send(text_data=json.dumps({
        #     'type':'chat',
        #     'message':message
        # }))
        # pass
    
    def chat_message(self,event):
        print(event)
        print('Event \n\n')
        try:
            message = event['message'][0]
            username = event['message'][1]
        except:
            message = event[0]
            username = event[1]
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'username':username

        }))

    def disconnect(self, close_code):
        print('LEFT\n\n')
        # pass
