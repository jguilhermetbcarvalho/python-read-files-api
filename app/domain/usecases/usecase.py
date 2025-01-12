from abc import ABC, abstractmethod
from typing import Any, Optional

from pydantic import BaseModel

from app.services.helpers.http import HttpResponse

NOT_IMPLEMENTED_ERROR = 'This contract method must be implemented'


class BaseClassConfig:
    from_attributes = True
    populate_by_name = True
    arbitrary_types_allowed = True


class InputData(BaseModel):
    class Config (BaseClassConfig):
        pass


class Usecase(ABC):
    @abstractmethod
    def execute(self, *args: Optional[Any]) -> HttpResponse:
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)
