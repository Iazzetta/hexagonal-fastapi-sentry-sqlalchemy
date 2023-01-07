from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.main.credentials import Credentials
from src.ports.http.routers import users
import sentry_sdk

from src.repository.sqlalchemy.engine import Base, engine, get_db

def configure_sentry() -> None:
    sentry_sdk.init(
        dsn=Credentials.SENTRY_URI.value,
        traces_sample_rate=1.0,
    )

def configure_routers(application: FastAPI) -> None:
    application.include_router(users.router)

def configure_cors(application: FastAPI) -> None:
    origins = ["*"]
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=origins,
        allow_headers=origins,
    )

def configure_db() -> None:
    Base.metadata.bind = get_db()
    Base.metadata.create_all(engine)
