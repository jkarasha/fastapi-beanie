import os
import motor.motor_asyncio
from beanie import Document

from fastapi_users.db import BeanieBaseUser
from fastapi_users_db_beanie import BeanieUserDatabase

from .config import settings

DATABASE_URL = settings.DATABASE_URL
DATABASE_NAME = settings.DATABASE_NAME
DB_COLLECTION_NAME = settings.COLLECTION_NAME

client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL, uuidRepresentation="standard")

db = client[DATABASE_NAME]

class User(BeanieBaseUser, Document):
    pass

async def get_user_db():
    yield BeanieUserDatabase(User)