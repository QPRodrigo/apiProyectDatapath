movies_db = {}

def show_movies():
    return movies_db

def get_movie(movie_id: str):
    return movies_db.get(movie_id)

def create_movie(movie):
    movies_db[movie.id] = movie.dict()
    return movie

def update_movie(movie_id: str, movie):
    movies_db[movie_id] = movie.dict()
    return movie

def delete_movie(movie_id: str):
    del movies_db[movie_id]
