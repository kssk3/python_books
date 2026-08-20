from models import BaseBook


class PaperBook(BaseBook):
    BOOK_TYPE = "단행본"

    def __init__(self, title: str, author: str, isbn: str, page_count: int):
        super().__init__(title, author, isbn)
        self.page_count = page_count

    def to_dict(self) -> dict:
        info = super().to_dict()
        info["페이지 수"] = self.page_count
        return info
