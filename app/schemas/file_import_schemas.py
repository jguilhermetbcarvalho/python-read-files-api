from datetime import date
from typing import Optional
from pydantic import BaseModel
from fastapi import UploadFile



class FileSchema(BaseModel):
    file_import: UploadFile | str
    file_type: str
    company_id: int


class FileResponseSchema(BaseModel):
    message: str
