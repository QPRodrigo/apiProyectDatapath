#Pydantic
from sqlalchemy import Column, Integer, String, Date
from pydantic import BaseModel, Field
from ..connection.postgressConnector import DB_MyCollecions
from datetime import date

class InputMovie(DB_MyCollecions): 
    __tablename__ = 'my_movies'
    id = Column(
        Integer, 
        primary_key=True, 
        index=True
    )
    autor = Column(
        String, 
        nullable=False
    )
    description = Column(
        String, 
        nullable=False
    )
    release_date = Column(
        Date, 
        nullable=False
    )

class MovieCreate(BaseModel):
    autor: str = Field(
        ...,
        title="Autor de la película",
        description="El nombre del autor o creador de la película.",
        min_length=1,
        max_length=100  # Asumiendo que quieras un máximo de 100 caracteres para el autor.
    )
    description: str = Field(
        ...,
        title="Descripción de la película",
        description="Una breve descripción o sinopsis de la película."
     )
    release_date: date = Field(
        ...,
        title="Fecha de lanzamiento de la película",
        description="La fecha de lanzamiento oficial de la película."
    )

class OutputMovie(MovieCreate):
    id: int = Field(
        ...,
        title="ID de la película",
        description="El identificador único de la película"
    )

    class Config:
        orm_mode = True