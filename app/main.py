from fastapi import FastAPI
from app.routes.health_routes import router as health_router
from app.routes.upload_routes import router as upload_router

app = FastAPI()
app.include_router(health_router)

app.include_router(upload_router)

@app.get("/")
def root():
    return {"message": "Image Search Retrieval System"}