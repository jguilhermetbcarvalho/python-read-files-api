from sqlalchemy.orm import sessionmaker

from app.domain.usecases import Usecase
from app.infra.database import engine
from app.services.usecases import (
    CreateUserUsecase,
    UserLoginUsecase,
)

Session = sessionmaker(bind=engine)

def create_user_factory() -> Usecase:
    session = Session()

    return CreateUserUsecase(session=session)

def user_login_factory() -> Usecase:
    session = Session()

    return UserLoginUsecase(session=session)
