import json
from channels.generic.websocket import WebsocketConsumer
import pdb
import uuid

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.pubkey = str(uuid.uuid4())
        
        self.accept()
        
        
    def disconnect(self, close_code):
        pass
    
    def arrange_array(self,userarray):
        
        userarray.sort()
        n = p = len(userarray)
        m = (n//2)+1
        #print(m,n)
        
        for i in range(1,m,2):
            n-=1
            userarray[i],userarray[n] = userarray[n],userarray[i]
           
        if p%2 ==0 and p>3:
            userarray[-1],userarray[-2] = userarray[-2],userarray[-1]
        
        return userarray

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        

        self.send(text_data=json.dumps({
            'message': self.arrange_array(message)
        }))