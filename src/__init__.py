from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"

app = FastAPI(
    title="Kitty-library",
    description="A REST API form book library web service",
    version= version
)
app.include_router(book_router, prefix=f"/api/{version}/books", tags = ['books'])

@app.get("/")
async def get_root():
    return {"message": "Hello from fastAPI"}