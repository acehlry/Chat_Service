# from azure.messaging.webpubsubservice import WebPubSubServiceClient

from fastapi import FastAPI
from dto.question import QuestionRequest
from azure.messaging.webpubsubservice.aio import WebPubSubServiceClient
from azure.core.credentials import AzureKeyCredential
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage # 메시지를 보낸때 해당 클래스로 감싸 보내야함

import json
import azure.functions as func
import os
import uuid

fast_app = FastAPI()
fast_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
)
app = func.AsgiFunctionApp(app = fast_app, http_auth_level = func.AuthLevel.ANONYMOUS)

db_client = AsyncIOMotorClient(os.environ["DB_CONNECTION_URL"])
pubsub_client = WebPubSubServiceClient(endpoint=os.environ["PUBSUB_CONNECTION_URL"], hub=os.environ["PUBSUB_HUB"], credential=AzureKeyCredential(os.environ["PUBSUB_KEY"]))
servicebus_client = ServiceBusClient.from_connection_string(conn_str=os.environ["SERVICEBUS_CONNECTION_URL"], logging_enable=True)

db = db_client['mygpt']

@fast_app.get('/channel-id')
async def get_channel_id():
        return{"channel_id": str(uuid.uuid4())}

@fast_app.post('/question')
async def send_question(request: QuestionRequest):
        question_data = {
                "type":"question",
                "channel_id": request.channel_id,
                "content" : request.content
        }
        
        result = await db.messages.insert_one(question_data)
        question_data['_id'] = str(question_data['_id'])
        
        async with servicebus_client:
                sender = servicebus_client.get_queue_sender(queue_name="process-request-queue")
    
                async with sender:
                        message = ServiceBusMessage(json.dumps(question_data))
                        await sender.send_messages(message)
        
        return str(result.inserted_id)

@fast_app.get("/pubsub/token")
async def read_root(channel_id: str):
        return await pubsub_client.get_client_access_token(groups=[channel_id], minutes_to_expire=5, roles=['webpubsub.joinLeaveGroup.' + channel_id])