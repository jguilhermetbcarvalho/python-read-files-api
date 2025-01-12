from http import HTTPStatus
import bcrypt

from app.domain.usecases.user_login_usecase import UserLoginContract
from app.dto import UserLoginDTO
from app.infra.repositories import UserRepository
from app.services.helpers import create_token
from app.services.helpers.http.http import HttpResponse


class UserLoginUsecase(UserLoginContract):

    def __init__(
        self,
        session
    ) -> None:
        self.session = session
        self.user_repository = UserRepository(self.session)

    def _verify_password(self, insert_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(insert_password.encode('utf-8'), hashed_password.encode('utf-8'))

    def execute(self, params: UserLoginDTO) -> HttpResponse:
        username = params.username
        password = params.password

        if not username or not password:
            return HttpResponse(HTTPStatus.BAD_REQUEST, {'message': 'Username and password are required'})

        existing_user = self.user_repository.get_user_by_username(username=username)

        if not existing_user:
            return HttpResponse(HTTPStatus.UNAUTHORIZED)

        if self._verify_password(password, existing_user.password):
            token = create_token(existing_user.id)
            return HttpResponse(HTTPStatus.OK, {'token': token})

        return HttpResponse(HTTPStatus.UNAUTHORIZED)
