from fastapi import FastAPI
from app.routers import user_router

app = FastAPI(
    title= "Demo API Users Sistema",
    description= "Primera API con FastAPI, PostgreSQL",
    version= "1.0.0",
    summary= "Esta API se encarga de traer y crear todos los usuarios de mi base de datos"
)

app.include_router(user_router.router)


@app.get("/")
def root():
    return {"message":"API funcionando correctamente"}