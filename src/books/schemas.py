from pydantic import BaseModel
from datetime import datetime,date
from typing import List
from src.review.schemas import ReviewModel
import uuid


class bookModel(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime
    
class BookDetailModel(bookModel):
    reviews: List[ReviewModel]

class BookCreatedModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str

class singleBook(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str

class updateBookModel( BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int