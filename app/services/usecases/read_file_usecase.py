from http import HTTPStatus

from app.domain.usecases.read_file_usecase import ImportReadFileContract
from app.dto.file_import_dto import FileImportDTO
from app.services.helpers.http.http import HttpResponse
from app.services.strategies import CsvStrategy, HtmlStrategy, XlsStrategy


class ImportReadFileUsecase(ImportReadFileContract):

    strategies = {
        'csv': CsvStrategy,
        'html': HtmlStrategy,
        'xls': XlsStrategy
    }

    def __init__(
        self,
        session
    ) -> None:
        self.session = session


    def execute(self, params: FileImportDTO) -> HttpResponse:

        if params.file_type not in self.strategies:
            return HttpResponse(HTTPStatus.BAD_REQUEST, {'message': 'Invalid file type'})

        strategy = self.strategies[params.file_type]()

        return strategy.process()
