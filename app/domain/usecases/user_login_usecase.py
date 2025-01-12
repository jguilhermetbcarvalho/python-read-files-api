from abc import abstractmethod

from app.services.helpers.http import HttpResponse
from app.dto import UserLoginDTO
from app.domain.usecases.usecase import Usecase


class UserLoginContract(Usecase):
    @abstractmethod
    def execute(self, params: UserLoginDTO) -> HttpResponse:
        raise NotImplementedError()
