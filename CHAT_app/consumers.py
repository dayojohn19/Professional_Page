import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        current_room = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = current_room
        
        # When A user Joins the Room
        self.receive([['A Person Joined','Anonymous'],'Name of Persone'])
        #  ... Get Regustered User str(self.scope["user"]) 
        self.chat_message([f'\n You Join the room {current_room}','Unregister User'])
        # 
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )


        # self.send(text_data=json.dumps({
        #     'type':'connection_established',
        #     'message':'You are now Connected!'
        # }))

    def receive(self, text_data):

        try:
            text_data_json = json.loads(text_data)
            message =  text_data_json['message']
            username =  text_data_json['username']
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
