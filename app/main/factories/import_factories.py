from sqlalchemy.orm import sessionmaker

from app.domain.usecases import Usecase
from app.infra.database import engine
from app.services.usecases.read_file_usecase import (
    ImportReadFileUsecase
)

Session = sessionmaker(bind=engine)


def import_read_file_factory() -> Usecase:
    session = Session()

    return ImportReadFileUsecase(session=session)
