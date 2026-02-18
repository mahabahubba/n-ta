# pydantic is a data validation library to define the models or schemas for the application.
from pydantic import BaseModel, EmailStr

# Creates a new user which include an email and password. In the model they cannot be nullable.
# Data is sent for registration and login
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# This model is used to return user info without the password hash when we want to return user data in the response.
class UserOut(BaseModel):
    id: int
    email: EmailStr

    # orm_mode is set to True to allow the model to work with SQLAlchemy models and return data in a JSON format.
    class Config:
        orm_mode = True
