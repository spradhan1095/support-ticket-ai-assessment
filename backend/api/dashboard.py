from fastapi import APIRouter

from services.analytics_service import (
    analytics_service
)

router = APIRouter()


@router.get("/dashboard")
def dashboard():

    return analytics_service.summary()