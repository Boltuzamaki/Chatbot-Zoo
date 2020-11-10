import json
import asyncio
import json
from channels.consumer import AsyncConsumer
import time

chat_num = 0

class ChatConsumer(AsyncConsumer):


    async def websocket_connect(self, event):
        await self.send({
    	"type": "websocket.accept"
    })
        print("Connected", event)






    async def websocket_receive(self, event):
        global chat_num
        chatmap = {"hello": ["what is the problem#", "wanna hear song#", "exit"],
                   "what is the problem" : ["pc not working#", "Hell no"],
                   " wanna hear song":["yes", "no"]
        }

        await self.send({
	    	"type" : "websocket.send",
	    	'text' : event.get('text'),
	})    
        time.sleep(2)
        try:
          
   
          value_dict = chatmap[event["text"]]
          value_dict = " ".join(value_dict)
          print(value_dict)
          print(chat_num)
          await self.send({
	    	"type" : "websocket.send",
	    	'text' : value_dict,
	})  
        except Exception as e:
           print( str(e) )



        
        print("receive", event["text"])

    








    async def websocket_disconnect(self, event):
        print("disconnetced",event)