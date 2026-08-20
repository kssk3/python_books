from controller.book_controller import BookController
from service.book_service import BookService
from repository.book_repository import BookRepository

from utils.book_finder import BookFinder
from utils.input_parser import InputParser


def main():
    repo = BookRepository()
    parser = InputParser()
    finder = BookFinder(repo)

    service = BookService(repo=repo, parser=parser, finder=finder)
    controller = BookController(book_service=service)
    controller.run()


if __name__ == "__main__":
    main()
