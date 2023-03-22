import datetime

from pydantic import BaseModel, validator


class AnswerCreate(BaseModel):
    content: str

    @validator('content')
    def not_empty(cls, v):
        # print("Answer Content: "+v)
        if not v or not v.strip():
            raise ValueError('Empty values are not allowed.')
        return v


class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True
