from fastapi import FastAPI
import uvicorn
from llmworkflow import app
from settings import settings

api = FastAPI()

api.mount(path="/api",app= app, name="llmworkflow")

if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=8000)