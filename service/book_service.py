from repository import BookRepository
from utils import InputParser, BookFinder

from models import BaseBook, PaperBook, Ebook


class BookService:

    def __init__(self, repo: BookRepository, parser: InputParser, finder: BookFinder):
        self.repo = repo
        self.parser = parser
        self.finder = finder

    def register_book(self, info: dict) -> BaseBook:
        title = self.parser.input_string_parser(info["title"], "도서명")
        author = self.parser.input_string_parser(info["author"], "저자")
        isbn = self.parser.input_parser_isbn(info["ISBN"])
        self.__validate_isbn(isbn)

        book = self.create_book(info)
        saved_book = self.repo.save(book)
        return saved_book

    def find_registered_book(self, isbn: str) -> BaseBook:
        parse_isbn = self.parser.input_parser_isbn(isbn)
        find_book = self.finder.find_book(parse_isbn)

        if find_book is None:
            raise ValueError(f"{isbn}에 대한 정보가 없습니다.")

        return find_book

    def get_register_books(self) -> list[BaseBook]:
        return self.repo.find_all()

    def create_book(self, info: dict) -> BaseBook:
        if info["book_type"] == 1:
            return PaperBook(
                info["title"], info["author"], info["ISBN"], info["page_count"]
            )
        elif info["book_type"] == 2:
            return Ebook(info["title"], info["author"], info["ISBN"])
        else:
            raise ValueError("올바른 종류를 입력해주세요.")

    def rent_book(self, isbn: str) -> BaseBook:
        book = self.find_registered_book(isbn)
        book.rent()
        return book

    def return_book(self, isbn: str) -> BaseBook:
        book = self.find_registered_book(isbn)
        book.return_book()
        return book

    def __validate_isbn(self, isbn: str) -> None:
        if not isbn.isdigit() or len(isbn) != 13:
            raise ValueError("13자리 숫자값 입력하세요.")

        if self.repo.exists_by_isbn(isbn):
            raise ValueError("이미 등록된 ISBN입니다.")
