from pydantic import BaseModel
from typing import List, Dict, Any


# Query Request
class QueryRequest(BaseModel):
    question: str


# Query Response
class QueryResponse(BaseModel):
    answer: str


# Health Check
class HealthResponse(BaseModel):
    status: str


# Dashboard Response
class DashboardResponse(BaseModel):
    total_tickets: int
    open_tickets: int
    resolved_tickets: int
    escalated_tickets: int
    avg_rating: float


# Anomaly Response
class AnomalyItem(BaseModel):
    ticket_id: str
    reason: str


class AnomalyResponse(BaseModel):
    count: int
    anomalies: List[Dict[str, Any]]