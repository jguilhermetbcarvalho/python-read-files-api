from http import HTTPStatus
from app.services.helpers.http import HttpResponse


class CsvStrategy:

    def process(self):
        return HttpResponse(HTTPStatus.ACCEPTED, {"message": "File .csv imported successfully"})
