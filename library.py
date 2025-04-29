import json
from book import Book

class Library:
    def __init__(self):
        self.books = []
    
    def add_books(self, book:Book):
        self.books.append(book)

    def list_books(self):
        return self.books
    
    def search_books(self, keyword):
        return [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
    
    def remove_books(self, genre):
        self.books= [ book for book in self.books if book.genre != genre]

    def save_to_file(self, filename):
        with open (filename, 'w') as f:
            data = [book.__dict__ for book in self.books]
            json.dump(data, f, indent=4)

    def load_file(self, filename):
        try:
            with open (filename, 'r') as f:
                data = json.load (f)
                self.books = [Book(**book_data) for book_data in data]
        except FileNotFoundError:
            self.books = []
        
