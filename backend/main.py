from fastapi import FastAPI
from backend.database import init_db
from backend.api.routes import router as activity_router

app = FastAPI(title="MindPlan Backend")

@app.on_event("startup")
def startup():
    init_db()

app.include_router(activity_router)
