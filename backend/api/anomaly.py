from fastapi import APIRouter

from services.anomaly_detector import (
    anomaly_detector
)

router = APIRouter()


@router.get("/anomalies")
def anomalies():

    results = anomaly_detector.detect()

    return {

        "count": len(results),

        "anomalies": results
    }