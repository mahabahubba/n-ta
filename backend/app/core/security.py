# This file contains the security utilities for the application, including password hashing and JWT token management.
import pwd
import time
from passlib.context import CryptContext
# datatime module provides classes for manipulating dates and times.
from datetime import datetime, timedelta, timezone
# jose is a JS Object Signing and Encryption library that provides functions for encoding and decoding JWT tokens.
from jose import jwt


from app.core.config import settings

# pwd context create an instantce of the CryptContext class, which is used to handle password hashing and verification.
pwd_context = CryptContext(
    # bycrypt is a password hasing function that slows down brute-force attackes making hashing a computationally expensive.
    schemes=["bcrypt"],
    # deprecated="auto" means that the library will automatically handle any deprecation warnings related to the hashing schemes used.
    deprecated="auto"
)

# This function takes a plain text password as input and returns a hashed version of the password using the pwd_context instance.
def hash_password(password: str) -> str:
    password = password[:72]
    return pwd_context.hash(password)

# This function takes a plain text password and a hashed password as input and returns a boolean indicating whether the plain text password matches the hashed password.
def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_password = plain_password[:72]
    return pwd_context.verify(plain_password, hashed_password)

# This function creates a JWT access token with the provided data and an optional expiration time. If no expiration time is provided, it defaults to the value specified in the settings.
def create_access_token(data:dict, expires_delta: timedelta | None = None):
    # to encode is a copy of the input data dict, which will be modified to include the expiration time before becoming the payload of the JWT token.
    # Also to avoid mutating the original dict being passed through the function.
    to_encode = data.copy()
    # If there is an expiration time use the expiration time provided 
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
        # Otherwise use the default expiration time we have in our setting file.
    else:
        # Create cariable to add onto the expiration time of the token.
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        # using the original data we crated a copy of, we can add the expiration time.
    to_encode.update({"exp": expire})
    # Encode the data with the seret key and algorithm specified in the settings file to create the JWT token.
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM)
    # Return the encoded JWT token as a string.
    return encoded_jwt