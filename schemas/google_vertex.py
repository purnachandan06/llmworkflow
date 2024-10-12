from pydantic import BaseModel, Field

class GoogleVertexChat(BaseModel):
    """
    Pydantic model for GoogleVertex chat
    """
    message: str = Field(min_length=3)


class GoogleVertexEmbeddings(BaseModel):
    """
    Pydantic model for GoogleVertex embeddings
    """
    message: str = Field(min_length=3)