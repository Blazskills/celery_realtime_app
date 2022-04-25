from channels.generic.websocket import AsyncWebsocketConsumer



class JokersConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('jokes', self.channel_name) # add channel to group   
        await self.accept()
        
    async def disconnect(self):
        await self.channel_layer.group_discard('jokes', self.channel_name) # remove channel from group
        
        
    async def send_jokes(self, event):
        text_message =  event['text']
        await self.send(text_message)