from models import BaseBook

class Ebook(BaseBook):
    BOOK_TYPE = "전자책"
    
    def __init__(self, title:str, author:str, isbn):
        super().__init__(title, author, isbn)
        
    