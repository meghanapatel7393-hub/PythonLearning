from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    image: str | None = None

    class Config:
        from_attributes = True  # SQLAlchemy → Pydantic


class LoginSchema(BaseModel):
    email: str
    password: str

# from pydantic import BaseModel, EmailStr

# class UserCreate(BaseModel):
#     name: str
#     email: EmailStr
#     password: str

# class UserOut(BaseModel):
#     id: int
#     name: str
#     email: EmailStr

#     class Config:
#         orm_mode = True

# from pydantic import BaseModel

# class UserCreate(BaseModel):
#     name: str
#     email: str
#     password: str

# class Token(BaseModel):
#     access_token: str
#     token_type: str
