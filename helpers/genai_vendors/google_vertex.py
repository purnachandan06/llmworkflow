from ast import literal_eval
from langchain_google_vertexai import VertexAI
from google.oauth2.service_account import Credentials
from helpers.genai_vendors.genaivendor import GenAiVendor
from settings import settings

class GoogleVertex(GenAiVendor):
    """
    Class to define the implementations for Google Vertex service
    """
    def __init__(self):
        self.credentials = literal_eval(settings.GOOGLE_CREDENTAILS_JSON.replace("\n", "\\n"))

    def chat(self, message: str, model: str):
        """
        Method to perform chat request
        """
        creds = Credentials.from_service_account_info(self.credentials)
        instance = VertexAI(model_name=model,
                                project= self.credentials['project_id'],
                                credentials = creds,
                                max_retries=0)
        response = instance.invoke(input = message)
        return response

    def embeddings(self, message: str, model: str):
        """
        Method to perform embeddings request
        """
        pass