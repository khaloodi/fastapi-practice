from typing import Optional, List, Dict

from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: str
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': 'val1'}
    image: Optional[Image] = None #using our custom subtype

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

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int,
                   comment_title: int = Query(None,
                                              title='Id of the comment',
                                              description='Some description for comment title',
                                              alias='commentTitle',
                                              deprecated=True,
                                           ),
                   # content: str = Body('hi how are you')
                   # content: str = Body(...) # could also use Body(Ellipsis); this creates a required parameter
                   content: str = Body(...,
                                       min_length=10,
                                       max_length=50,
                                       regex='^[a-z\s]*$'
                                       ),
                   v: Optional[List[str]] = Query(['1.1','1.2','1.3']),
                   comment_id: int = Path(None, gt=5, le=10)
                   ):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'version': v,
        'comment_id': comment_id
    }

def required_functionality():
    return  {'message': 'Learning FastApi is important!'}
