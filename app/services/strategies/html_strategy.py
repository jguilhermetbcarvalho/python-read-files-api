from http import HTTPStatus
from app.services.helpers.http import HttpResponse


class HtmlStrategy:

    def process(self):
        return HttpResponse(HTTPStatus.ACCEPTED, {"message": "File .html imported successfully"})

