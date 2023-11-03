import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from datetime import datetime
import time
class ChatConsumer(WebsocketConsumer):
    
    print('NEWNEWNEW')
    def connect(self):
        print("""
        ----------------------------------------
        ----------------------------------------
        CONNECTING
        ----------------------------------------
        ----------------------------------------

        """)
        from .models import Chat_Room_Model,Chat_Messages_Model
        self.accept() 
        current_room = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = current_room
        
        # When A user Joins the Room
        self.receive([['A Person Joined','Anonymous'],'Name of Persone'])
        try:
            print('\n\nTrying to fetch old room')
            self.chatRoom = Chat_Room_Model.objects.get(chat_room_name=self.room_group_name)
            print('\n\n Room Fetched')
        except:
            print('\n\n Creating Room')
            self.chatRoom = Chat_Room_Model.objects.create(admin_ID=self.room_group_name,admin_name=self.room_group_name,chat_room_name=self.room_group_name)
            self.chatRoom.save()
            print('\n\n Created: ',self.room_group_name)
        print('\n\n\n\n Created OR FOUND ROOM NAME \n\n')
        #  ... Get Regustered User str(self.scope["user"]) 
        self.chat_message([f'\n You Join the room {current_room}','Unregister User'])
        # 
        print('\n\n Messages: ',self.chatRoom.messages_items)
        print('Message: ',self.chatRoom.chat_room_name)
        for i in self.chatRoom.messages_items:
            self.send(text_data=json.dumps({
                'type':'chat',
                'message':i.sender_chat_message,
                'username':i.sender_name,
                'message_timestamp':datetime.fromisoformat(i.message_timestamp).strftime("%I:%M%p %d%b%Y")
                # 'message_timestamp':i.message_timestamp

            },default=str,sort_keys=True))            
            # self.chat_message([i.sender_chat_message,i.sender_name])
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
        print("""
        ----------------------------------------
        ----------------------------------------
        RECEIVING
        ----------------------------------------
        ----------------------------------------

        """)
        try:
            text_data_json = json.loads(text_data)
            message =  text_data_json['message']
            username =  text_data_json['username']
            print('\n Chat messaged')
            from .models import Chat_Messages_Model
            new_chat_message = Chat_Messages_Model()
            new_chat_message.sender_ID = username
            new_chat_message.sender_name = username
            new_chat_message.sender_chat_message = message[0]
            new_chat_message.save()
            new_chat_message.chat_room_model = self.chatRoom
            self.chatRoom.chatroom_messages.add(new_chat_message)
            self.chatRoom.save()
            message_timestamp = datetime.fromisoformat(message_timestamp).strftime("%I:%M%p %d%b%Y")
            # .objects.create(sender_ID=username,sender_name=username,sender_chat_message=message,chat_room_model=self.chatRoom)
            # new_chat_message.save()
            print('\n CHat Saved')
        except:
            message = text_data[0]
            username = text_data[1]
            message_timestamp = datetime.now().strftime("%I:%M%p %d%b%Y")
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username,
                'message_timestamp':message_timestamp
                # 'message_timestamp':message_timestamp
            }
        )
        # self.send(text_data=json.dumps({
        #     'type':'chat',
        #     'message':message
        # }))
        # pass
    
    def chat_message(self,event):
        print("""
        ----------------------------------------
        ----------------------------------------
        Chat MESSAGING
        ----------------------------------------
        ----------------------------------------

        """)        
        try:
            message = event['message'][0]
            username = event['message'][1]
            from .models import Chat_Messages_Model
            new_chat_message = Chat_Messages_Model()
            new_chat_message.sender_ID = username
            new_chat_message.sender_name = username
            new_chat_message.sender_chat_message = message
            new_chat_message.save()
            new_chat_message.chat_room_model = self.chatRoom
            self.chatRoom.chatroom_messages.add(new_chat_message)
            self.chatRoom.save()            

            self.send(text_data=json.dumps({
                'type':'chat',
                'message':message,
                'username':username,
                # 'message_timestamp':new_chat_message.message_timestamp
                'message_timestamp': datetime.fromisoformat(new_chat_message.message_timestamp).strftime("%I:%M%p %d%b%Y")
            },default=str,sort_keys=True))

        except:
            message = event[0]
            username = event[1]
            self.send(text_data=json.dumps({
                'type':'chat',
                'message':message,
                'username':username,
                'message_timestamp':datetime.now.strftime("%I:%M%p %d%b%Y")
            }))

    def disconnect(self, close_code):
        print('LEFT\n\n')
        # pass
