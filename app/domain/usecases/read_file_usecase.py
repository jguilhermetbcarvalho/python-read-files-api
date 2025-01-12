from abc import abstractmethod

from app.services.helpers.http import HttpResponse
from app.dto.file_import_dto import FileImportDTO
from .usecase import Usecase


class ImportReadFileContract(Usecase):
    @abstractmethod
    def execute(self, params: FileImportDTO) -> HttpResponse:
        raise NotImplementedError()
