from fastapi import FastAPI, APIRouter
from routers.sample import router as document_router
llmworkflow_router = APIRouter()

llmworkflow_router.include_router(document_router)

def start_app() -> FastAPI:
    '''
    Method to create instace for fastapi to start it
    '''
    fast_app = FastAPI()
    fast_app.include_router(llmworkflow_router)
    return fast_app

app = start_app()