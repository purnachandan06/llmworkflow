from fastapi import FastAPI, APIRouter
from routers.sample import router as sample_router
from routers.aws import router as aws_router

llmworkflow_router = APIRouter()

llmworkflow_router.include_router(sample_router)
llmworkflow_router.include_router(aws_router)

def start_app() -> FastAPI:
    '''
    Method to create instace for fastapi to start it
    '''
    fast_app = FastAPI()
    fast_app.include_router(llmworkflow_router)
    return fast_app

app = start_app()