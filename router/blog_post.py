from typing import Optional

from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    date: Optional[bool]

@router.post('/new') #-> /blog/new ...
def create_blog(blog: BlogModel):
    return {'data': blog}

@router.post('/new/{id}') #-> multiple params
def create_blog(blog: BlogModel, id: int, version: int=1):
    return {
        'blog': blog,
        'id': id,
        'version': version
    }

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int,
                   comment_id:int = Query(None,
                                          alias='commentId',
                                          deprecated=True,
                                          title='Id of the comment',
                                          description='Some description for comment id')):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
    }
