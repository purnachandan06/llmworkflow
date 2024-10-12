import boto3
from langchain_aws import BedrockLLM, BedrockEmbeddings
from helpers.genai_vendors.genaivendor import GenAiVendor
from settings import settings

class AwsBedrock(GenAiVendor):
    """
    Class to define the implementations for Aws bedrock service
    """
    def __init__(self):
        self.credentails = {
            "region": settings.AWS_REGION,
            "accesskey": settings.AWS_ACCESS_KEY,
            "secretkey": settings.AWS_SECRET_KEY
        }
        self.boto3client = boto3.client("bedrock-runtime",
                                        region_name=self.credentails['region'],
                                        aws_access_key_id=self.credentails['accesskey'],
                                        aws_secret_access_key=self.credentails['secretkey'])

    def chat(self, message: str, model: str):
        """
        Method to perform chat request
        """
        instance = BedrockLLM(client=self.boto3client,
                              model_id=model)
        #messages = [("system","You are a helpful assistant that translates English to French. Translate the user sentence."),
        #            ("human", message)]
        response_message = instance.invoke(input = message)
        return response_message

    def embeddings(self, message: str, model: str):
        """
        Method to perform embeddings request
        """
        instance = BedrockEmbeddings(client=self.boto3client,
                                     model_id=model)
        response_message = instance.embed_query(message)

        return {
            "embeddings": response_message
        }
