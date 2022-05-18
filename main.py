from fastapi import FastAPI

from db.database import engine
from router import blog_get, blog_post, user
from db import models


app = FastAPI()
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/')
def index():
    return {'message': 'Hello world'}

#run database creation, create database if it doesn't exist
models.Base.metadata.create_all(engine)
