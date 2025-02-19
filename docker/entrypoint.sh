#!/bin/bash
cd /home/app \
&& export PYTHONDONTWRITEBYTECODE=1 \
&& poetry install \
&& poetry run uvicorn app.main.main:app --host=0.0.0.0 --port=8012 --reload
