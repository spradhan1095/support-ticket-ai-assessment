from fastapi import FastAPI

from api.health import router as health_router
from api.query import router as query_router
from api.anomaly import router as anomaly_router
from api.dashboard import router as dashboard_router

app = FastAPI(
    title="Support Ticket AI System",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(query_router)
app.include_router(anomaly_router)
app.include_router(dashboard_router)