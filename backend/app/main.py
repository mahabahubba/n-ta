from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session


from app.db.database import engine
from app.db import models
from app.deps import get_db
from app.crud import user as crud_user
from app.core.security import create_access_token
from app.schemas.user import UserCreate, UserOut
from app.deps import get_current_user



app = FastAPI(title="N-TA Backend")

# Creates the tables automatically based on the models defined in the models.py file.
# Runs when it starts up

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"status": "ok"}


# Endoint for user registration. Accepts the UserCreate schema as inout and returns the Userout.
# If the user alreasdy exists, it raises an HTTPException with a 400 status code and a detail message indicating that the email is already registered. If the user is successfully created, it returns the new user object.
@app.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    new_user = crud_user.create_user(db, email=user.email, password=user.password)
    return new_user


# Endpoint for user login.
# Accepts Usercreate schema as input and return a JSON object witha access token.
# First it authenticates the user using the authenticate user f(x) from the crud_user_module.
# it is fails then provides a 401 status code with error message.
# If successful it creates a token using the create access token f(x)
# The token contains the user's email as the subject (sub) and is returned in a JSON response with the token type specified as "bearer".
@app.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.authenticate_user(db, email=user.email, password=user.password)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/me")
def read_current_user(current_user: UserOut = Depends(get_current_user)):
    return {"id": current_user.id, "email": current_user.email}