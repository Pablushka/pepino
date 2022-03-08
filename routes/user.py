from fastapi import APIRouter
from schemas.user import  userEntity, usersEntity
from models.user import User
from config.db import db_connection
from bson import ObjectId

user = APIRouter()

@user.get("/test")
async def hello():
  return {"mensaje": "Hola mundo!"}

@user.get('/users')
async def list_all_users():
  return usersEntity(db_connection.pepino.users.find())

@user.post('/user')
async def create_user(user: User):
  new_user = dict(user)

  result = db_connection.pepino.users.insert_one(new_user)
  id = result.inserted_id

  user = db_connection.pepino.users.find_one({"_id": ObjectId(id)})

  return  userEntity(user)



