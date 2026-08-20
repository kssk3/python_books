from models import BaseBook, PaperBook, Ebook

class BookRepository:

    def __init__(self):
        self.books: dict[str, BaseBook] = {}
        self.isbns: set[str] = set()

        self.__seed_books()

    def __seed_books(self) -> None:
        sample_books = [
            # 단행본 7권
            PaperBook(
                "The Art of Loving",
                "Erich Fromm",
                "9780061129735",
                176,
            ),
            PaperBook(
                "To Have or to Be?",
                "Erich Fromm",
                "9780349113432",
                224,
            ),
            PaperBook(
                "The Problems of Philosophy",
                "Bertrand Russell",
                "9780486406749",
                121,
            ),
            PaperBook(
                "A History of Western Philosophy",
                "Bertrand Russell",
                "9780671201586",
                897,
            ),
            PaperBook(
                "Illuminations",
                "Walter Benjamin",
                "9780805202410",
                288,
            ),
            PaperBook(
                "One-Way Street and Other Writings",
                "Walter Benjamin",
                "9781859841976",
                392,
            ),
            PaperBook(
                "Crime and Punishment",
                "Fyodor Dostoyevsky",
                "9780199536368",
                537,
            ),
            # 전자책 3권
            Ebook(
                "Escape from Freedom",
                "Erich Fromm",
                "9781480402560",
            ),
            Ebook(
                "The Brothers Karamazov",
                "Fyodor Dostoyevsky",
                "9780679601814",
            ),
            Ebook(
                "Notes from Underground",
                "Fyodor Dostoyevsky",
                "9781672003605",
            ),
        ]

        for book in sample_books:
            self.save(book)

    def save(self, book: BaseBook) -> BaseBook:
        isbn = book.get_isbn()
        self.books[isbn] = book
        self.isbns.add(isbn)
        return book

    def find_by_isbn(self, isbn: str) -> BaseBook | None:
        return self.books.get(isbn)

    def find_all(self) -> list[BaseBook]:
        return list(self.books.values())

    def exists_by_isbn(self, isbn: str) -> bool:
        return isbn in self.isbns
