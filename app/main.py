# FastAPI
from fastapi import FastAPI
from .routers import movies_router

#  Instancia de la clase.
app = FastAPI()
app.include_router(movies_router.router, prefix="/movie", tags=["movie"])
@app.get("/")
def home():
   #JSON
   return {"First API": "Congratulation"}
