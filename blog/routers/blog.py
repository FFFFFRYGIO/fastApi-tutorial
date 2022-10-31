from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(prefix='/blog', tags=['Blogs'])
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def print_all(db: Session = Depends(get_db),
              current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(bid: int, db: Session = Depends(get_db),
            current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(bid, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(bid: int, request: schemas.Blog, db: Session = Depends(get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(bid, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(bid: int, db: Session = Depends(get_db),
         current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(bid, db)
