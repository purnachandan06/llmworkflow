from fastapi import APIRouter
import schemas.google_vertex as schema
import services.google_vertex as service

router = APIRouter(prefix="/googlevertex", tags=["googlevertex"])

@router.post("/chat")
def chat_request(chat_request: schema.GoogleVertexChat):
    """
    Api to chat using aws bedrock
    """
    return service.chat(chat_request)

@router.post("/embeddings")
def embeddings_request(embedding_request: schema.GoogleVertexEmbeddings):
    """
    Api to chat using aws bedrock
    """
    return service.embeddings(embedding_request)
