from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.app import router
from src.infra.db.configs.database import create_db
from src.middlewares.timer import process_timer_request
from src.jobs.write_notification import write_notification

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


@app.middleware("http")
async def process_timer_request(request: Request, next):
    """Middleware."""
    print("Interceptor...")
    response = await next(request)
    print("Interceptou volta...")
    return response


@app.post("/send_email/{email}")
def send_email(email: str, background: BackgroundTasks):
    """Background task."""
    background.add_task(write_notification, email)
    return {"Ok": "Msg sent"}
