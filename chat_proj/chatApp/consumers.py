# Create asynchronous app func here
import json
from channels.generic.websocket import AsyncWebsocketConsumer

# Similar to a class-view inside of "views.py"
class ChatRoomConsumer(AsyncWebsocketConsumer):
    # websocket connection func (async func); hand-shaking stage; we also need to send a msg to websocket "connect"
    async def connect(self):
        # return await super().connect()
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Construct/ create a new chat group, 
        # and behind the scene, this group will be utilizing the consumer "ChatRoomConsumer"
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )

        # The backend server is also need to accept the connection, by accepting an incoming socket; before the handshaking stage is completed
        await self.accept()     # In this LOC, the websocket connects


        # *** (Start) It is commented after up & running the chat functionality, NEED FOR INITIAL SETUP

        # after accepting the connection, the msg can be received/ send back and forth to the backend & client; NB: thus the "self.channel_layer.group_send()" func need to be placed after the "self.accept" func
        # as soon as we're inside the connect func, we're going to send a msg to the grp {probably my thought, from the client's end to the WS server}
        # generating/ sending msg into the room_group (backend)

        # await self.channel_layer.group_send(
        #     self.room_group_name,   # what group to send the msg to; then we define what msg we want to send
        #     {
        #         'type': 'tester_message',
        #         'tester': 'Testing Message after connecting to the chatroom!',
        #     }
        # )

        # *** (End) It is commented after up & running the chat functionality, NEED FOR INITIAL SETUP



    # *** (Start) It is commented after up & running the chat functionality, NEED FOR INITIAL SETUP

    # collect the msg func, which sent to the client's end the moment s/he connected to this WS
    # after receiving msg from the backend room_group, sent msg to the front-end via WS
    # NB: This "tester_message(self, event)" func is defined in the "await self.channel_layer.group_send()" above inside the "'type': 'tester_message',"

    # async def tester_message(self, event):
    #     tester = event['tester']    # colleting the value from the key "tester" from the "self.channel_layer.group_send()" func

    #     # sending the value from the "tester" here to the "#user-hello" div inside the "chat_room.html"
    #     # The json.dumps() method encodes any Python object into JSON formatted String.
    #     await self.send(text_data=json.dumps({
    #         'tester': tester,
    #     }))
    
    # *** (End) It is commented after up & running the chat functionality, NEED FOR INITIAL SETUP



    # websocket connection close func (async func)
    async def disconnect(self, close_code):
        # discard the group
        await self.channel_layer.group_discard(
            self.room_group_name,   # which group to discard
            self.channel_name
        )
    

    # handling msgs that are sent from the front-end
    # after handling the msg, then sent them inside the room_group 
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)  # json.loads() is used to parse a valid JSON string and convert it into a Python Dictionary.
        message = text_data_json['message']     # accesing the python dictionary; collected from the frontend js ("js/ws_msg_from_frontend.js")
        username = text_data_json['username']   # collected from the frontend js ("js/ws_msg_from_frontend.js")


        # now send the msg to the front-end again, so that everyone in the group can see this msg
        await self.channel_layer.group_send(
            self.room_group_name,   # what group to send the msg to; then we define what msg we want to send
            {
                'type': 'chat_message',
                'message': message,
                'username_grp_send': username,
            }
        )

    # after receiving msg from the backend room_group, sent msg to the front-end via WS
    async def chat_message(self, event):
        message = event['message']
        username_passed_from_grp_send = event['username_grp_send']
        # Sends a reply back down the WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username_backend': username_passed_from_grp_send,
        }))

