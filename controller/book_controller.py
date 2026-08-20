from service import BookService
import sys


class BookController:
    def __init__(self, book_service: BookService):
        self.service = book_service

    def run(self) -> None:

        start = True

        while start:
            try:
                self.show_start_print()
                result = input()
                match result:
                    case "1":
                        self.choice_book_register()
                    case "2":
                        self.show_result_books()
                    case "3":
                        self.show_registered_book_info()
                    case "4":
                        self.choice_rent_or_return()
                    case "5":
                        print("종료합니다.")
                        sys.exit()
                    case _:
                        print("올바른 메뉴 번호를 입력해주세요. \n")

            except ValueError as error:
                print(f"입력 오류: {error}")

    def show_start_print(self) -> None:
        print("=" * 35)
        print("1. 도서 등록")
        print("2. 도서 목록 조회")
        print("3. 도서 정보")
        print("4. 도서 대여 | 반납")
        print("5. 종료")
        print("=" * 35)

    def choice_book_register(self) -> None:
        info = {
            "title": input("도서명을 입력해주세요: \n").strip(),
            "author": input("저자명을 입력해주세요: \n").strip(),
            "ISBN": input("ISBN 입력해주세요: ex) 9781234567897 \n").strip(),
            "book_type": int(
                input("종류를 선택해 주세요 (1. 단행본 / 2. 전자책) \n").strip()
            ),
        }

        if info["book_type"] == 1:
            page_count = input("페이지 수를 입력해주세요: \n").strip()

            self.__validate_page_input(page_count)
            info["page_count"] = int(page_count)

        self.service.register_book(info)

    def choice_rent_or_return(self) -> None:
        choice = input("1. 도서 대여 / 2. 반납 \n").strip()
        isbn = input("처리할 ISBN을 입력해주세요. \n").strip()

        match choice:
            case "1":
                book = self.service.rent_book(isbn)
                print(f"{book.to_dict()} \n 대여가 완료되었습니다.")
            case "2":
                book = self.service.return_book(isbn)
                print(f"{book.to_dict()} \n 반납이 완료되었습니다.")
            case _:
                print("올바른 메뉴 번호를 입력해주세요. \n")

    def show_registered_book_info(self):
        isbn = input("찾을 도서의 ISBN을 입력하세요: \n")
        find_book = self.service.find_registered_book(isbn)

        print(find_book.to_dict())

    def show_result_books(self):
        book_list = self.service.get_register_books()

        if not book_list:
            print("등록된 도서가 없습니다.")
            return

        for book in book_list:
            print(book.to_dict())

    def __validate_page_input(self, page_count: str) -> None:
        if not page_count.isdigit():
            raise ValueError("올바른 페이지 수를 입력해주세요 \n")

        if int(page_count) <= 0:
            raise ValueError("페이지 수는 1 이상이어야 합니다.")
