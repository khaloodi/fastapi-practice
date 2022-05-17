from fastapi import APIRouter

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

@router.post('/new') #-> /blog/new ...
def create_blog():
    return