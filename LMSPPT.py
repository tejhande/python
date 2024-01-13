import datetime


class Book:
    def __init__(self, book_id, title, author, publisher, edition, num_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.edition = edition
        self.num_copies = num_copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author}"

class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.user_id}: {self.name} ({self.email})"

class Order:
    def __init__(self, order_id, book, user, issued_date):
        self.order_id = order_id
        self.book = book
        self.user = user
        self.issued_date = issued_date
        self.returned_date = None
        self.is_returned = False

    def return_book(self, returned_date):
        self.returned_date = returned_date
        self.is_returned = True

    def is_expired(self):
        return (datetime.date.today() - self.issued_date).days > 30

    def get_fine(self):
        if self.is_expired() and not self.is_returned:
            days_overdue = (datetime.date.today() - self.issued_date).days - 30
            return days_overdue * 2 # Assuming a fine of $2 per day overdue
        else:
            return 0

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.orders = []
        self.next_book_id = 1
        self.next_user_id = 1
        self.next_order_id = 1

    def add_book(self, title, author, publisher, edition, num_copies):
        book_id = self.next_book_id
        book = Book(book_id, title, author, publisher, edition, num_copies)
        self.books.append(book)
        self.next_book_id += 1
        return book

    def update_book(self, book_id, title=None, author=None, publisher=None, edition=None, num_copies=None):
        book = self.get_book(book_id)
        if title is not None:
            book.title = title
        if author is not None:
            book.author = author
        if publisher is not None:
            book.publisher = publisher
        if edition is not None:
            book.edition = edition
        if num_copies is not None:
            book.num_copies = num_copies

    def delete_book(self, book_id):
        book = self.get_book(book_id)
        self.books.remove(book)

    def get_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def add_user(self, name, email, password):
        user_id = self.next_user_id
        user = User(user_id, name, email, password)
        self.users.append(user)
        self.next_user_id += 1
        return user

    def get_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def add_order(self, book_id, user_id):
        book = self.get_book(book_id)
        user = self.get_user(user_id)

        if book is None:
            # print(f"Book with)
            pass

# Create a library object
my_library = Library()

# Add a book
my_library.add_book("The Catcher in the Rye", "J.D. Salinger", "Little, Brown and Company", "First Edition", 3)

# Add a user
my_library.add_user("John Smith", "john.smith@example.com", "password")

# Place an order
my_library.add_order(1, 1)
