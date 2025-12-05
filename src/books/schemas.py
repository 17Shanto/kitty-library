from pydantic import BaseModel
class bookModel(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class singleBook(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class updateBookModel( BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int