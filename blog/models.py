from datetime import datetime
from uuid import UUID

from fastapi import FastAPI

from pydantic import BaseModel



app = FastAPI()


class ConfigModel(BaseModel):
    _id: UUID
    status: bool
    date_created: datetime
    date_updated: datetime


class User(ConfigModel):
    email: str
    username: str
    password : str


class Category(ConfigModel):
    name: str


class Image(ConfigModel):
    url: str
    name: str

class Article(ConfigModel):
    tiltle: str
    description: str | None = None
    image: Image | None = None
    author: User
    category: Category


class Comment(ConfigModel):
    username: str
    description: str | None = None
    author: User
    article: Article
