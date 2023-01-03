import os
from enum import Enum
from dotenv import load_dotenv

load_dotenv()

class Credentials(Enum):
    X_TOKEN = os.getenv('X_TOKEN')
    SENTRY_URI = os.getenv('SENTRY_URI')