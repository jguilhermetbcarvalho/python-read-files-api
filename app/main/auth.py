from functools import wraps
from http import HTTPStatus
import contextvars
import inspect
from fastapi import Request, HTTPException

import jwt
from sqlalchemy.orm import sessionmaker

from app.infra.database import engine
from app.infra.repositories import UserRepository
from app.services.helpers.helpers import SECRET_KEY

Session = sessionmaker(bind=engine) # pylint: disable=invalid-name
user_context = contextvars.ContextVar("user_context") # pylint: disable=invalid-name

def token_required(func):
    @wraps(func)
    async def decorated(request: Request, *args, **kwargs):

        response: object = kwargs.get('response', None)

        try:
            headers = request.headers
            if "Authorization" not in headers:
                raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Token not provided")

            token = headers.get('Authorization').split("Bearer ")[1]
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

            user_repository = UserRepository(Session())
            is_admin = user_repository.check_user_is_admin(data['user_id'])

            user_context.set({"user_id": data["user_id"], "is_admin": is_admin})
            # kwargs["user_data"] = {"user_id": data["user_id"], "is_admin": is_admin}

            if inspect.iscoroutinefunction(func):
                return await func(request=request, *args, **kwargs)
            else:
                return func(request=request, *args, **kwargs)

        except jwt.ExpiredSignatureError:
            response.status_code = HTTPStatus.UNAUTHORIZED  # type: ignore
            return response
        except jwt.InvalidTokenError:
            response.status_code = HTTPStatus.UNAUTHORIZED  # type: ignore
            return response

    return decorated


def admin_required(func):
    @wraps(func)
    async def decorated(*args, **kwargs):
        user_data = user_context.get()
        if not user_data or not user_data.get("is_admin"):
            raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="Admin privileges required")

        if inspect.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        else:
            return func(*args, **kwargs)

    return decorated
