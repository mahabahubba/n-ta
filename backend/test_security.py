# backend/test_security.py

from app.core.security import hash_password, verify_password, create_access_token

hashed = hash_password("test123")
print("Password verified:", verify_password("test123", hashed))

token = create_access_token({"sub": "test@example.com"})
print("JWT token:", token)
