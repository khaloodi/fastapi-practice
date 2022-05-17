from enum import Enum
from typing import Optional, Dict
from fastapi import APIRouter, status, Response, Depends

from router.blog_post import required_functionality

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

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
@router.get('/all',
         summary='Retrieve all blogs',
         description='This api call simulates fetching all blogs',
         response_description='The list of available blogs'
         )
def get_blogs(page=1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)): #page_size is now an optional parameter with default value of none
    # todo Query Parameters
    #  any function parameters not part of the path
    return {'message': f'All {page_size} blogs on page {page}', 'req' : req_parameter}

#QUERY + PATH parameters combined
@router.get('/{id}/comments/{comment_id}', tags=['comment']) #tags categorize operations, can have multiple categories
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None,  req_parameter: dict = Depends(required_functionality)):
    """
    Simulates retrieving a comment of a blog
    -  **id**: mandatory path parameter
    -  **comment_id**: mandatory path parameter
    -  **valid**: optional query parameter
    -  **username**: optional query parameter
    """
    return {'message': f'Blog id {id}, comment id {comment_id}, valid {valid}, username {username}'}

# todo Predefined values with Enum
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{type}')
def blog_type(type: BlogType, req_parameter: dict = Depends(required_functionality)):
    return {'message': f'Blog type: {type}'}

# @app.get('/blog/{id}')
# def get_blog(id: int): #fast api's way of enforcing type
#     return {'message': f'Blog with id: {id}'}
@router.get('/{id}', status_code = status.HTTP_200_OK)
def get_blog(id: int, response: Response, req_parameter: dict = Depends(required_functionality)):
    if id > 5:

        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id: {id}'}