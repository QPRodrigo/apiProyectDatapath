#Pydantic
from pydantic import BaseModel, Field
from datetime import date

class Movies(BaseModel): # Movies parameters
    id: str = Field(
        ...,
        title="ID de la película",
        description="El identificador único de la película, entre 1 y 50 caracteres.",
        min_length=1,
    )
    autor: str = Field(
        ...,
        title="Autor de la película",
        description="El nombre del autor o creador de la película.",
        min_length=1,
        max_length=100  # Asumiendo que quieras un máximo de 100 caracteres para el autor.
    )
    descripcion: str = Field(
        ...,
        title="Descripción de la película",
        description="Una breve descripción o sinopsis de la película.",
        min_length=1,
        max_length=500  # Asumiendo un máximo de 500 caracteres para la descripción.
    )
    release_date: date = Field(
        ...,
        title="Fecha de lanzamiento de la película",
        description="La fecha de lanzamiento oficial de la película."
    )