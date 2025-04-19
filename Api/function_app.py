# from azure.messaging.webpubsubservice import WebPubSubServiceClient

from fastapi import FastAPI
from dto.question import QuestionRequest
from azure.messaging.webpubsubservice.aio import WebPubSubServiceClient
from azure.core.credentials import AzureKeyCredential
from fastapi.middleware.cors import CORSMiddleware

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

pubsub_client = WebPubSubServiceClient(endpoint=os.environ["PUBSUB_CONNECTION_URL"], hub=os.environ["PUBSUB_HUB"], credential=AzureKeyCredential(os.environ["PUBSUB_KEY"]))

# 질문 API
# PubSub 토큰 발급 API

@fast_app.get('/channel-id')
async def get_channel_id():
        return{"channel_id": str(uuid.uuid4())}

@fast_app.post('/question')
async def send_question(request: QuestionRequest):
        return request

@fast_app.get("/pubsub/token")
async def read_root(channel_id: str):
        return await pubsub_client.get_client_access_token(groups=[channel_id], minutes_to_expire=5, roles=['webpubsub.joinLeaveGroup.' + channel_id])