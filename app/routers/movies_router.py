from fastapi import APIRouter, HTTPException, Body, Path, Query
from ..models.movies_model import Movies
from ..controllers import movies_controller

from datetime import date

router = APIRouter()

@router.get('/')
def show_movies():
    movies = movies_controller.show_movies()
    if not movies:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movies

@router.get("/{movie_id}")
def get_movie(movie_id: str):
    movie = movies_controller.get_movie(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.post("/", status_code=201)
def create_movie(movie: Movies = Body(...)):
    return movies_controller.create_movie(movie)

@router.put("/{movie_id}")
def update_movie( movie_id: str, movie: Movies = Body(...)):
    return movies_controller.update_movie(movie_id, movie)

@router.delete("/{movie_id}")
def delete_movie(movie_id: str):
    movies_controller.delete_movie(movie_id)
    return {"message": "Movie deleted successfully"}
