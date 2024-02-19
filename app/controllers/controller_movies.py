from sqlalchemy.orm import Session
from ..models.model_movies import  InputMovie, MovieCreate
from typing import List

def get_movies(db: Session, skip: int = 0, limit: int = 100) -> List[InputMovie]:
    return db.query(InputMovie).offset(skip).limit(limit).all()

def get_movie(db: Session, movie_id: int):
    return db.query(InputMovie).filter(InputMovie.id == movie_id).first()

def create_movie(db: Session, movie: MovieCreate):
    db_movie = InputMovie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def update_movie(db: Session, movie_id: int, movie_update: MovieCreate):
    db_movie = db.query(InputMovie).filter(InputMovie.id == movie_id).first()
    if not db_movie:
        return None
    update_data = movie_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_movie, key, value)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def delete_movie(db: Session, movie_id: int):
    db_movie = db.query(InputMovie).filter(InputMovie.id == movie_id).first()
    if not db_movie:
        return None
    db.delete(db_movie)
    db.commit()
    return db_movie

