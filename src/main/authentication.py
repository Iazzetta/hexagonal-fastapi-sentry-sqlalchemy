from fastapi import HTTPException, Header

from src.main.credentials import Credentials

async def get_token_header(x_token: str = Header()):
    if x_token != Credentials.X_TOKEN.value:
        raise HTTPException(status_code=400, detail="X-Token header invalid")