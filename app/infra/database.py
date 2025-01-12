import os
from sqlalchemy import create_engine

from app.domain.models import Base

# Create an PostgreSQL database
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)

# Create tables based on the models
Base.metadata.create_all(engine)
