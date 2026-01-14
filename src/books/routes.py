from typing import List
from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from src.books.schemas import bookModel, singleBook, updateBookModel, BookCreatedModel
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.service import BookService
from src.auth.dependencies import AccessTokenBearer, RoleChecker

book_router = APIRouter()
book_service = BookService()
access_token_bearer = AccessTokenBearer()
role_checker = Depends(RoleChecker(['admin', 'user']))

@book_router.get("/", response_model=List[bookModel], status_code= status.HTTP_200_OK, dependencies=[role_checker])
async def get_all_books(session:AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    print(user_details)
    books = await book_service.get_all_books(session)
    return books



@book_router.get("/{book_uid}", response_model=bookModel, status_code=status.HTTP_200_OK, dependencies=[role_checker])
async def getBook_by_id(book_uid:str, session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    book = await book_service.get_book(book_uid, session)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book does not exist in ID {book_uid}")
    


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=bookModel, dependencies=[role_checker])
async def create_book(book_data:BookCreatedModel, session:AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    new_book = await book_service.create_book(book_data,session)
    return new_book
    # raise HTTPException(status_code = status.HTTP_201_CREATED, detail="New Book is added successfully")


@book_router.patch("/{book_uid}", response_model= bookModel, status_code= status.HTTP_200_OK, dependencies=[role_checker])
async def update_by_id(book_uid:str, book_to_update: updateBookModel, session:AsyncSession=Depends(get_session), user_details=Depends(access_token_bearer)):
    updated_book = await book_service.update_book(book_uid,book_to_update,session)
    if updated_book:
        return updated_book
    else:
        raise HTTPException ( status_code= status.HTTP_404_NOT_FOUND, detail= f"Book does not exist in ID {book_uid}")


@book_router.delete("/{book_uid}",status_code= status.HTTP_204_NO_CONTENT, dependencies=[role_checker])
async def delete_by_id(book_uid:str, session: AsyncSession=Depends(get_session), user_details=Depends(access_token_bearer)):
    book_to_delete = await book_service.delete_book(book_uid, session)
    if book_to_delete is None:
        raise HTTPException ( status_code= status.HTTP_404_NOT_FOUND, detail= f"Book does not exist in ID {book_uid}")
    return {}
        
        

