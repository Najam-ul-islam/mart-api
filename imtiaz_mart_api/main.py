from fastapi import FastAPI
from datetime import timedelta
from imtiaz_mart_api.auth_service.auth import create_access_token, decode_access_token
 

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Docker compose with FastAPI"}

@app.get("/get_token")
def get_token(name: str):
    access_token_expiry_time = timedelta(minutes=1)
    generated_token = create_access_token(subject=name, expires_delta=access_token_expiry_time)
    return {"access token": generated_token}
@app.get("/verify_token")
def verify_token(token: str):
    verified_token = decode_access_token(token)
    return verified_token