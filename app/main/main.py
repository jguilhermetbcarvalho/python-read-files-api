# main.py
import os

from dotenv import load_dotenv
from fastapi import FastAPI

from app.main.routes.user_routes import user_router
from app.main.routes.import_routes import import_router

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))


app = FastAPI(
    title='Read Files API',
    description='Serviço backend para leitura de arquivos: pdf, csv, xls, html',
)

app.include_router(user_router)
app.include_router(import_router)
