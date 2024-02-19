from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..models.model_movies import MovieCreate, OutputMovie
from ..controllers import controller_movies
from ..connection.postgressConnector import SessionLocal

router = APIRouter()

# Dependencia
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get('/all', response_model=List[OutputMovie])
def get_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = controller_movies.get_movies(db, skip=skip, limit=limit)
    return movies

@router.get("/{movie_id}", response_model=OutputMovie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = controller_movies.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@router.post("/", response_model=OutputMovie)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return controller_movies.create_movie(db=db, movie=movie)

@router.put("/{movie_id}", response_model=OutputMovie)
def update_movie_endpoint(movie_id: int, movie: MovieCreate, db: Session = Depends(get_db)):
    updated_movie = controller_movies.update_movie(db=db, movie_id=movie_id, movie_update=movie)
    if updated_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return updated_movie

@router.delete("/{movie_id}", response_model=OutputMovie)
def delete_movie_endpoint(movie_id: int, db: Session = Depends(get_db)):
    deleted_movie = controller_movies.delete_movie(db=db, movie_id=movie_id)
    if deleted_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return deleted_movie