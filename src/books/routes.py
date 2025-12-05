from typing import List
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from src.books.book_data import books
from src.books.schemas import bookModel, singleBook, updateBookModel

book_router = APIRouter()

@book_router.get("/", response_model=List[bookModel], status_code= status.HTTP_200_OK )
async def get_books():
    return books

@book_router.get("/{bookId}", response_model=singleBook, status_code=status.HTTP_200_OK)
async def getBook_by_id(bookId:int):
    for book in books:
        if(book["id"] == bookId):
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book does not exist in ID {bookId}")

@book_router.post("/", response_model=bookModel)
async def create_book(book:bookModel):
    new_book = book.model_dump()
    books.append(new_book)
    raise HTTPException(status_code = status.HTTP_201_CREATED, detail="New Book is added successfully")

@book_router.patch("/{bookId}", response_model= updateBookModel, status_code= status.HTTP_200_OK)
async def update_by_id(bookId:int, book_to_update: updateBookModel):
    for book in books:
        if(book['id'] == bookId):
            book['title'] = book_to_update.title
            book['author'] = book_to_update.author
            book['publisher'] = book_to_update.publisher
            book ['page_count'] = book_to_update.page_count
            return book
    
    raise HTTPException ( status_code= status.HTTP_404_NOT_FOUND, detail= f"Book does not exist in ID {bookId}")

@book_router.delete("/{bookId}",status_code= status.HTTP_204_NO_CONTENT)
async def delete_by_id(bookId:int):
    for book in books:
        if(book['id'] == bookId):
            books.remove(book)
            return {}
    raise HTTPException ( status_code= status.HTTP_404_NOT_FOUND, detail= f"Book does not exist in ID {bookId}")
        

