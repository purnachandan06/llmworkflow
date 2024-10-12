from schemas.google_vertex import GoogleVertexChat, GoogleVertexEmbeddings
from helpers.genai_vendors.google_vertex import GoogleVertex

def chat(chat_request: GoogleVertexChat):
    """
    Method to perform chat request
    """
    instance = GoogleVertex()
    return instance.chat(chat_request.message, "gemini-1.5-pro-001")

def embeddings(embeddings_request: GoogleVertexEmbeddings):
    """
    Method to perform embeddings request
    """
    instance = GoogleVertex()
    return instance.embeddings(embeddings_request.message, "amazon.titan-embed-g1-text-02")