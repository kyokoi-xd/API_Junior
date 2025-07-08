from fastapi import FastAPI
from app.routers import auth


app = FastAPI(
    title="FastAPI Authentication Example",
    version="0.1.0"
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.get("/", tags=["health"])
def read_root():
    return {"message": "Welcome to the FastAPI Authentication Example!"}