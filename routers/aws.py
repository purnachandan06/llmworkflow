from fastapi import APIRouter
import schemas.aws as schema
import services.aws as service

router = APIRouter(prefix="/aws", tags=["aws"])

@router.post("/chat")
def chat_request(chat_request: schema.AwsChat):
    """
    Api to chat using aws bedrock
    """
    return service.chat(chat_request)

@router.post("/embeddings")
def embeddings_request(embedding_request: schema.AwsEmbeddings):
    """
    Api to chat using aws bedrock
    """
    return service.embeddings(embedding_request)
