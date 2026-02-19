# This module provides security-related functions, including password hashing and JWT token creation.
import bcrypt
from datetime import datetime, timedelta, timezone
# Importing the jwt module from the jose library for handling JSON Web Tokens (JWT).
from jose import jwt
from app.core.config import settings

# Function to hash a password using bcrypt. It takes a plain text password, encodes it to bytes, and returns the hashed password as a string.
def hash_password(password: str) -> str:
    password_bytes = password[:72].encode("utf-8")
    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

# Function to verify a plain text password against a hashed password. It encodes the plain password to bytes and compares it with the hashed password using bcrypt's checkpw function.
def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_bytes = plain_password[:72].encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(plain_bytes, hashed_bytes)

# Function to create a JWT access token. It takes a dictionary of data and an optional expiration time. It encodes the data into a JWT token using the secret key and algorithm specified in the settings.
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt
