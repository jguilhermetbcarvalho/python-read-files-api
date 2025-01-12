from dataclasses import dataclass
from typing import Dict
from fastapi import UploadFile


@dataclass
class FileImportDTO:
    user_data: Dict
    file_import: UploadFile | str
    file_type: str
    company_id: int
