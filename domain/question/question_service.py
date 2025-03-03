from datetime import datetime

from domain.question.question_schema import QuestionCreate

from model import Question
from sqlalchemy.orm import Session


def get_question_list(db: Session, skip: int = 0, limit: int = 10):
    _question_list = db.query(Question).order_by(Question.create_date)
    operators = [op.id for op in _question_list]
    print(operators)


    total = _question_list.count()
    question_list = _question_list.offset(skip).limit(limit).all()

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
