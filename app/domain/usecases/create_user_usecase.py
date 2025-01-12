from abc import abstractmethod

from app.services.helpers.http import HttpResponse
from app.dto import UserDTO
from app.domain.usecases.usecase import Usecase


class CreateUserContract(Usecase):
    @abstractmethod
    def execute(self, params: UserDTO) -> HttpResponse:
        raise NotImplementedError()
