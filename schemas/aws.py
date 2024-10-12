from pydantic import BaseModel, Field

class AwsChat(BaseModel):
    """
    Pydantic model for AWS chat
    """
    message: str = Field(min_length=3)


class AwsEmbeddings(BaseModel):
    """
    Pydantic model for AWS embeddings
    """
    message: str = Field(min_length=3)