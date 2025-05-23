from schemas.aws import AwsChat, AwsEmbeddings
from helpers.genai_vendors.aws import AwsBedrock

def chat(chat_request: AwsChat):
    """
    Method to perform chat request
    """
    instance = AwsBedrock()
    return instance.chat(chat_request.message, "amazon.titan-tg1-large")

def embeddings(embeddings_request: AwsEmbeddings):
    """
    Method to perform embeddings request
    """
    instance = AwsBedrock()
    return instance.embeddings(embeddings_request.message, "amazon.titan-embed-g1-text-02")