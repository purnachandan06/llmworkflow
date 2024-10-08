from fastapi import APIRouter
from schemas.aws import AwsChat
from services.aws import chat

router = APIRouter(prefix="/aws", tags=["aws"])

@router.post("/chat")
def chat_request(chat_request: AwsChat):
    """
    Api to chat using aws bedrock
    """
    return chat(chat_request)
