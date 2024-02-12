from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str

#creating a method to aunthenticate the user
@app.post('/authenticate')
async def authenticate(user: User):
    return {}