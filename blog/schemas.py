from typing import List, Optional
from pydantic import BaseModel, ConfigDict


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    model_config = ConfigDict(from_attributes=True)


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    model_config = ConfigDict(from_attributes=True)


class ShowUser2(BaseModel):
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser2

    model_config = ConfigDict(from_attributes=True)


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
