import isbnlib


class InputParser:

    def __init__(self) -> None:
        self = self

    def input_string_parser(self, input: str, field_name: str | None) -> str:
        if input is None:
            print("값을 넣어주세요")
        result = input.strip()

        if not result:
            raise ValueError(f"{field_name}은(는) 필수 입력값입니다.")

        return result

    def input_parser_isbn(self, input_isbn: str) -> str:
        isbn = isbnlib.to_isbn13(input_isbn)
        self.__validate_isbn13(isbn)

        return isbn

    def __validate_isbn13(self, isbn: str) -> None:
        if not isbnlib.is_isbn13(isbn):
            raise ValueError("유효하지 않은 ISBN-13입니다.")
