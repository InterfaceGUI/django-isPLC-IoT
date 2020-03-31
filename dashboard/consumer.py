from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
import json

class LiveConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # get name from ws url args
        self.name = self.scope['url_route']['kwargs']['name']
        self.room_group_name = self.scope['url_route']['kwargs']['ID']

        if self.scope['user'] == AnonymousUser():
            raise DenyConnection("Invalid User")

        # Join group group_add('group_name', 'channel_name')
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave group group_discard('group_name', 'channel_name')
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        #text_data_json = json.loads(text_data)
        #message = self.name + ': ' + text_data_json['message']
        #logger.debug('send')


        message = '{"From":"' + self.name + '","context":' + text_data + '}'

        # Send message to room group
        await self.group_send(message)

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def group_send(self, msg, type_='chat_message'):   
        # group_send('group_name', {'type': type, **kwargs})
        # type means what function you want to do
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': type_,
                'message': msg
            }
        )
