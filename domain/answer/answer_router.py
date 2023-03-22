from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.answer import answer_schema, answer_service
from domain.question import question_service

router = APIRouter(
    prefix="/api/answer",
)


@router.post("/create/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def answer_create(question_id: int,
                  _answer_create: answer_schema.AnswerCreate,
                  db: Session = Depends(get_db)):
    question = question_service.get_question(db, question_id=question_id)

    if not question:
        raise HTTPException(status_code=404, detail="Question Not Found")
    answer_service.create_answer(db, question=question, answer_create=_answer_create)
