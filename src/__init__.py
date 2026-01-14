from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routers import auth_router
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.review.routes import review_router

@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is starting...")
    await init_db()
    yield
    print("Server is stopped !!")


version = "v1"
app = FastAPI(
    title="Kitty-library",
    description="A REST API form book library web service",
    version= version,
    lifespan= life_span
    
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags = ['books'])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags = ['auth'] )
app.include_router(review_router, prefix=f"/api/{version}/reviews", tags = ['reviews'] )


@app.get("/")
async def get_root():
    return {"message": "Hello from fastAPI"}