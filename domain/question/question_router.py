from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from domain.question import question_schema, question_service
from database import get_db

router = APIRouter(
    prefix="/api/question",
)


@router.get("/list", response_model=question_schema.QuestionList)
def question_list(db: Session = Depends(get_db),
                  page_index: int = 0):
    total, _question_list = question_service.get_question_list(db, page_index=page_index)
    page = {
        'total': total,
        'question_list': _question_list
    }
    print(page)
    return page


@router.get("/detail/{question_id}", response_model=question_schema.Question)
def get_question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_service.get_question(db, question_id=question_id)
    return question


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def create_question(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_service.create_question(db, question_create=_question_create)
