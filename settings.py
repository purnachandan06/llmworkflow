import os
from dotenv import load_dotenv
from pathlib import Path

env_file_path = Path.cwd() / 'helpers/.env'

load_dotenv(dotenv_path=env_file_path)

class Settings():
    '''
    Class to load env variables
    '''
    #AZURE OPENAI
    AZURE_OPENAI_BASE_URL = os.getenv('AZURE_OPENAI_BASE_URL')
    AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY')
    AZURE_OPENAI_API_VERSION = os.getenv('AZURE_OPENAI_API_VERSION')
    AZURE_OPENAI_EMBEDDINGS_MODEL = os.getenv('AZURE_OPENAI_EMBEDDINGS_MODEL')

    #AWS BEDROCK
    AWS_REGION = os.getenv('AWS_REGION')
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')

    #GOOGLE VERTEX
    GOOGLE_CREDENTAILS_JSON = os.getenv('GOOGLE_CREDENTAILS_JSON')
    
    #QDRANT
    QDRANT_BASE_URL = os.getenv('QDRANT_BASE_URL')
    QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')

settings = Settings()