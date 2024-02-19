# FastAPI
from fastapi import FastAPI
from .routers import router_movies

#  Instancia de la clase.
app = FastAPI()
app.include_router(router_movies.router, prefix="/movie", tags=["movie"])
@app.get("/")
def home():
   #JSON
   return {"First API": "Congratulation"}
