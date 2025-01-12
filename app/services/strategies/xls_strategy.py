from http import HTTPStatus
from app.services.helpers.http import HttpResponse


class XlsStrategy:

    def process(self):
        return HttpResponse(HTTPStatus.ACCEPTED, {"message": "File .xls imported successfully"})

