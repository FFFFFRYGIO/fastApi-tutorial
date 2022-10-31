from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(bid: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == bid)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {bid} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(bid: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == bid)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {bid} not found")

    blog.update(request)
    db.commit()
    return 'updated'


def show(bid: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == bid).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {bid} is not available")
    return blog
