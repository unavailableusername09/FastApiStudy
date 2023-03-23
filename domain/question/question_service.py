from datetime import datetime

from domain.question.question_schema import QuestionCreate

from model import Question
from sqlalchemy.orm import Session


def get_question_list(db: Session, page_index: int = 0):
    _question_list = db.query(Question) \
        .order_by(Question.create_date)

    total = _question_list.count()
    question_list = _question_list.offset(page_index*10).limit(10).all()

    return total, question_list


def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question


def create_question(db: Session, question_create: QuestionCreate):
    db_question = Question(subject=question_create.subject,
                           content=question_create.content,
                           create_date=datetime.now())
    db.add(db_question)
    db.commit()
