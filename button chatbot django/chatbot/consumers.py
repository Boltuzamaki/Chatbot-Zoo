import json
import asyncio
import json
from channels.consumer import AsyncConsumer
import time

class ChatConsumer(AsyncConsumer):
   

    async def websocket_connect(self, event):
        await self.send({
    	"type": "websocket.accept"
    })
        print("Connected", event)

    async def websocket_receive(self, event):
        chatmap = {"hello": ["what is the proble#", "wanna hear song#", "exit"]}

        await self.send({
	    	"type" : "websocket.send",
	    	'text' : event.get('text'),
	})  
        try:
           value_dict = chatmap[event["text"]]
           
           value_dict = " ".join(value_dict)
           print(value_dict)
           await self.send({
	    	"type" : "websocket.send",
	    	'text' : value_dict,
	})  
        except Exception as e:
           print( str(e) )


        
        print("receive", event["text"])

    async def websocket_disconnect(self, event):
        print("disconnetced",event)