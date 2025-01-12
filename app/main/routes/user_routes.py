from http import HTTPStatus

from fastapi import APIRouter, Request, Response

from app.main.auth import token_required, admin_required
from app.schemas import (
    CreateUserSchema,
    CreateUserResponseSchema,
    UserLoginSchema,
    UserLoginResponseSchema,)
from app.main.adapter import fastapi_adapter
from app.main.factories import (
    create_user_factory,
    user_login_factory
)


user_router = APIRouter(
    prefix='/api/v1',
    responses={
        HTTPStatus.BAD_REQUEST.value: {
            'description': 'Register User Error',
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'User not found',
        }
    },
    tags=['Users']
)

@user_router.post('/user', response_model=CreateUserResponseSchema)
@token_required
@admin_required
def create_user(
    body: CreateUserSchema,
    request: Request,
    response: Response
):
    return fastapi_adapter(body, response, create_user_factory())


@user_router.post('/signin', response_model=UserLoginResponseSchema)
def user_login(
    body: UserLoginSchema,
    request: Request,
    response: Response
):
    return fastapi_adapter(body, response, user_login_factory())
