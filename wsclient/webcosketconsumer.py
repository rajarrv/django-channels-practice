
import asyncio
from websockets import connect
import json
import ssl
import pdb

#ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
#localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
#ssl_context.load_verify_locations(localhost_pem)

async def socket_open(uri,mylst):
    #async with connect(uri,ssl=ssl_context) as websocket:
    async with connect(uri) as websocket:
        #pdb.set_trace()
        
        await websocket.send(json.dumps({'message':mylst}))
        data = await websocket.recv()
        return json.loads(data).get('message')
        
a = [[3,5,1],[3,7,9,2,1],[1,2,3,4,5,6],[10,1,15,18]]
for each in a:
    print(asyncio.get_event_loop().run_until_complete(socket_open("ws://localhost:8001/species/",each )))