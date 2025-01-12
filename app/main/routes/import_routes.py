from http import HTTPStatus
from fastapi import APIRouter, Request, Response, Form

from app.main.auth import user_context
from app.dto import (
    FileImportDTO
)
from app.schemas import (FileSchema, FileResponseSchema)
from app.main.adapter import fastapi_adapter
from app.main.auth import token_required, admin_required
from app.main.factories import (
    import_read_file_factory
)


import_router = APIRouter(
    prefix='/api/v1',
    responses={
        HTTPStatus.BAD_REQUEST.value: {
            'description': 'Import File Error',
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'File not found',
        }
    },
    tags=['Read files']
)


@import_router.post('/read-file', response_model=FileResponseSchema)
@token_required
@admin_required
def import_read_file(
    request: Request,
    response: Response,
    body: FileSchema = Form(...),
):
    try:
        user_data = user_context.get()
    except:
        user_data = None

    dto = FileImportDTO(
        user_data=user_data,
        file_import=body.file_import,
        file_type=body.file_type,
        company_id=body.company_id,
    )
    return fastapi_adapter(dto, response, import_read_file_factory())
