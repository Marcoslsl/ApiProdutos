from fastapi import FastAPI
from src.main.routes import router
from src.infra.db.configs.database import create_db

create_db()

app = FastAPI()
app.include_router(router)
