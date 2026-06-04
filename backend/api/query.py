from fastapi import APIRouter
from schemas.schemas import QueryRequest
from services.query_engine import query_engine

router = APIRouter()


@router.post("/query")
def query(req: QueryRequest):

    answer = query_engine.answer_question(
        req.question
    )

    return {
        "answer": answer
    }