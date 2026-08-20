from datetime import datetime as dt


class BaseBook:
    BOOK_TYPE = "도서"

    def __init__(self, title: str, author: str, isbn: str):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_rent = False
        now = dt.now()
        self.__create_at = now
        self.__update_at = now

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def get_isbn(self) -> str:
        return self.__isbn

    def get_book_type(self) -> str:
        return self.BOOK_TYPE

    def get_created_at(self) -> dt:
        return self.__create_at

    def get_update_at(self) -> dt:
        return self.__update_at

    def is_rent(self) -> bool:
        return self.__is_rent

    def is_available(self) -> bool:
        if self.__is_rent:
            return False

        return True

    def rent(self) -> None:
        if self.__is_rent:
            raise ValueError("이미 대여 중인 도서입니다.")
        self.__is_rent = True
        self.__update_at = dt.now()

    def return_book(self) -> None:
        if not self.__is_rent:
            raise ValueError("대여 중인 도서가 아닙니다.")
        self.__is_rent = False
        self.__update_at = dt.now()

    def to_dict(self) -> dict:
        return {
            "도서명": self.get_title(),
            "저자": self.get_author(),
            "ISBN": self.get_isbn(),
            "종류": self.BOOK_TYPE,
            "대여 가능": self.is_available(),
        }

    def __str__(self):
        return f"도서명 : {self.__title}, 저자: {self.__author}, ISBN : {self.__isbn}, {self.BOOK_TYPE}, 대여 상태 {self.__is_rent} 입니다"
