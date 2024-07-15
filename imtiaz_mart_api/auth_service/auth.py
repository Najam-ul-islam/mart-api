from jose import jwt, JWTError
from datetime import datetime, timedelta


ALGORITHM = "HS256"
SECRET_KEY = "secret key"

def create_access_token(subject: str, expires_delta: timedelta) -> str:
    expire  = datetime.now() + expires_delta
    to_encode = {"sub": str(subject), "exp": expire}
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def decode_access_token(access_token: str):
    try:
        decoded_token = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token
    except JWTError:
        return {"error": JWTError}
