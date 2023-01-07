import dataclasses
from fastapi import APIRouter, Depends
from src.core.domain.user.service import UserService
from src.core.domain.user.user import User
from src.main.authentication import get_token_header
from src.presentation.factories.user import make_user_controller

from src.main.logger import logger
from src.presentation.helpers.responses import response_error, response_success

blueprint_name = 'users'

router = APIRouter(
    prefix = f"/{blueprint_name}",
    tags = [blueprint_name],
    dependencies = [Depends(get_token_header)],
    responses = { 404: { "description": "Not found" } },
)

@router.post("/create")
async def create_user(user: User, controller: UserService = Depends(make_user_controller)):
    try:
        response = controller.create(**dataclasses.asdict(user))
        return response_success(response.to_dict())
    except Exception as e:
        logger.error(e)
        return response_error(model = blueprint_name, err = str(e))

@router.get("/")
async def list_users(controller: UserService = Depends(make_user_controller)):
    try:
        response = controller.list()
        return response_success(response)
    except Exception as e:
        logger.error(e)
        return response_error(model = blueprint_name, err = str(e))