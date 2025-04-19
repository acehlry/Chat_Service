from pydantic import BaseModel

# 직렬화가 필요
# --> BaseModel 상속
class QuestionRequest(BaseModel):
    channel_id: str
    content: str