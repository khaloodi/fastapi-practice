from enum import Enum
from typing import Optional

from fastapi import FastAPI, status, Response

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello world'}

# @app.get('/blog/all')
# def get_blogs():
#     return {'message': f'All blogs'}

# DEFAULT VALUES
# @app.get('/blog/all')
# def get_blogs(page=1, page_size=10): #notice params are not in path above
#     # todo Query Parameters
#     #  any function parameters not part of the path
#     return {'message': f'All {page_size} blogs on page {page}'}

#OPTIONAL PARAMETERS
@app.get('/blog/all',
         tags=['blog'],
         summary='Retrieve all blogs',
         description='This api call simulates fetching all blogs',
         response_description='The list of available blogs'
         )
def get_blogs(page=1, page_size: Optional[int]=None): #page_size is now an optional parameter with default value of none
    # todo Query Parameters
    #  any function parameters not part of the path
    return {'message': f'All {page_size} blogs on page {page}'}

#QUERY + PATH parameters combined
@app.get('/blog/{id}/comments/{comment_id}', tags=['blog', 'comment']) #tags categorize operations, can have multiple categories
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog
    -  **id**: mandatory path parameter
    -  **comment_id**: mandatory path parameter
    -  **valid**: optional query parameter
    -  **username**: optional query parameter
    """
    return {'message': f'Blog id {id}, comment id {comment_id}, valid {valid}, username {username}'}

# @app.get('/blog/{id}')
# def get_blog(id: int): #fast api's way of enforcing type
#     return {'message': f'Blog with id: {id}'}
@app.get('/blog/{id}', status_code = status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response: Response):
    if id > 5:

        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id: {id}'}

# todo Predefined values with Enum
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}', tags=['blog'])
def blog_type(type: BlogType):
    return {'message': f'Blog type: {type}'}

# In terminal to run app in browser: uvicorn main:app --reload