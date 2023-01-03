from fastapi import FastAPI
from src.main.configuration import configure_cors, configure_db, \
                                    configure_routers, configure_sentry

app = FastAPI()

def create_application() -> FastAPI:

    configure_sentry()

    application = FastAPI()

    configure_routers(application)
    configure_cors(application)
    configure_db()

    return application

core_module = create_application()