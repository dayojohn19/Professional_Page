import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        current_room = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = current_room
        self.receive([['Person Joined','Anonymous'],'Name of Persone'])
        self.chat_message([f'\n You Join the room {current_room}',str(self.scope["user"])])
        # 
        print('\n User Connected to a room', self.room_group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )


    def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message =  text_data_json['message']
            username =  text_data_json['username']
        except:
            message = text_data[0]
            username = text_data[1]
        print('\n Data Processd-------------: ',message,username)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username
            }
        )
    
    def chat_message(self,event):
        try:
            message = event['message'][0]
            username = event['message'][1]

        except:
            message = event[0]
            username = event[1]
            print('Faile')
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'username':username

        }))

    def disconnect(self, close_code):
        print('LEFT\n\n')
        # pass
