from repository import BookRepository
from models import BaseBook



class BookFinder:
    def __init__(self, repo: BookRepository):
        self.repo = repo

    def find_book(self, book_isbn:str) -> BaseBook | None:
        return self.repo.find_by_isbn(book_isbn)
