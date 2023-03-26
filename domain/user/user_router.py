from datetime import timedelta, datetime

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.user import user_service, user_schema
from domain.user.user_service import pwd_context

import token_properties

router = APIRouter(
    prefix="/api/user",
)


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    user = user_service.get_existing_user(db, user_create=_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="이미 존재하는 사용자입니다.")
    user_service.create_user(db=db, user_create=_user_create)


@router.post("/login",response_model=user_schema.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: BaseException = Depends(get_db)):
    user = user_service.get_user(db, form_data.username)
    if not user or pwd_context.verify(form_data.password, pwd_context.hash(user.password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    data = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=token_properties.ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, token_properties.SECRET_KEY, algorithm=token_properties.ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
    }
