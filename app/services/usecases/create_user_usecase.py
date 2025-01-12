from http import HTTPStatus
import bcrypt

from app.domain.usecases.create_user_usecase import CreateUserContract
from app.dto import UserDTO
from app.infra.repositories import UserRepository
from app.services.helpers.http.http import HttpResponse


class CreateUserUsecase(CreateUserContract):

    def __init__(
        self,
        session
    ) -> None:
        self.session = session
        self.user_repository = UserRepository(self.session)

    def _hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def execute(self, params: UserDTO) -> HttpResponse:
        fullname = params.fullname
        username = params.username
        password = self._hash_password(params.password)
        params.password = password

        if not fullname or not username or not password:
            return HttpResponse(HTTPStatus.BAD_REQUEST, {'message': 'Fullname, Username and password are required'})

        existing_user = self.user_repository.verify_user(username)
        if existing_user:
            return HttpResponse(HTTPStatus.BAD_REQUEST, {'message': 'Username already exists'})

        self.user_repository.create_user(params)


        return HttpResponse(HTTPStatus.CREATED, {'message': 'User created successfully'})
