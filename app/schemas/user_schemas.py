from pydantic import BaseModel, EmailStr


class CreateUserSchema(BaseModel):
    fullname: str
    username: EmailStr
    password: str
    is_admin: bool
    scopes: list


class UserLoginSchema(BaseModel):
    username: EmailStr
    password: str


class CreateUserResponseSchema(BaseModel):
    message: str


class UserLoginResponseSchema(BaseModel):
    token: str
