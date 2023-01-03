from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.datalayer.database.postgres.engine import Base, get_db, engine
from src.main.credentials import Credentials
from src.presentation.routers import users
import sentry_sdk

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
