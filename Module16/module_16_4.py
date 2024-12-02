# Домашнее задание по теме "Модели данных Pydantic"

from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field
from typing import List, Annotated


class UserCreate(BaseModel):
    username: str = Field(min_length=5, max_length=20, examples=['UrbanUser'])
    age: int = Field(ge=18, le=120, examples=['24'])


class User(UserCreate):
    id: int = Field(ge=1, examples=['25'])


app = FastAPI()

users = []


@app.get(path='/users', response_model=List[User])
async def get_users():
    return users


@app.post(path='/user/{username}/{age}', response_model=User)
async def post_user(user: UserCreate):
    new_id = max((user.id for user in users), default=0) + 1
    user = User(id=new_id, username=user.username, age=user.age)
    users.append(user)
    return user


@app.put(path='/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id: Annotated[int, Path(ge=1)], updated_user: UserCreate):
    for user in users:
        if user.id == user_id:
            user.username = updated_user.username
            user.age = updated_user.age
            return user
    raise HTTPException(status_code=404, detail='User was not found')


@app.delete(path='/user/{user_id}', response_model=User)
async def delete_user(user_id: Annotated[int, Path(ge=1)]):
    for i, user in enumerate(users):
        if user.id == user_id:
            return users.pop(i)
    raise HTTPException(status_code=404, detail='User was not found')
