from fastapi import APIRouter
from backend.models.activity_model import get_all_activities

router = APIRouter()

@router.get("/activities")
def fetch_activities():
    return {"activities": get_all_activities()}
