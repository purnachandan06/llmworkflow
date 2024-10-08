from schemas.aws import AwsChat
from helpers.genai_vendors.aws import AwsBedrock

def chat(chat_request: AwsChat):
    """
    Method to perform chat request
    """
    instance = AwsBedrock()
    return instance.chat(chat_request.message, "amazon.titan-tg1-large")