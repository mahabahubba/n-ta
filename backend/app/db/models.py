from sqlalchemy import Column, Integer, String
from .database import Base

# As per the document requirement we only need email and password for the model
# both email and password are required fields and email must be unique. We also have an id field which is the primary key for the table and is indexed for faster lookups.
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)