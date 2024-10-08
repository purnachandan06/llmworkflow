from pydantic import BaseModel, Field

class AwsChat(BaseModel):
    """
    Pydantic model for AWS chat
    """
    message: str = Field(min_length=3)
