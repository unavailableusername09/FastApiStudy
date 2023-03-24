from pydantic import BaseModel, validator, EmailStr


class UserCreate(BaseModel):
    username: str
    password1: str
    password2: str
    email: EmailStr

    @validator('username', 'password1', 'password2', 'email')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Empty values are not allowed.')
        return v

    @validator('password2')
    def passwords_match(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError('Password not match')
        return v
