#import pandas as pd

#print(pd.DataFrame)

from fastapi import FastAPI
from app.generator.base import router as base_router
from app.generator.generation import router as generation_router


def start_application() -> FastAPI:
    application = FastAPI()

    application.include_router(base_router)
    application.include_router(generation_router)

    return application

app = start_application()