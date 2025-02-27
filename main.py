
# run: uvicorn main:app

import json

from fastapi import FastAPI

# from email import email
from datetime import datetime
from pydantic import BaseModel, TypeAdapter, PositiveInt, ValidationError

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    email: str = 'test@gmail.com'
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]

external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',
    'tastes': {
        'wine': 9,
        'cheese': 7,
        'cabbage': '1',
    },
}

try:
    User(**external_data)
except ValidationError as e:
    print(e.errors())

user_schema = User.model_json_schema()
# print(json.dumps(user_schema, indent=2))

adapter = TypeAdapter(User)
# print(adapter.json_schema())

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World", "user": json.dumps(user_schema)}