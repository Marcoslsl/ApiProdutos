from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.app import router
from src.infra.db.configs.database import create_db

create_db()

app = FastAPI()
app.include_router(router)

origins = ["http://localhost:5500"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
