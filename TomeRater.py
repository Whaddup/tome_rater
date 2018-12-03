class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Email address has now been updated to: ", self.email)

    def __repr__(self):
        return "User: " + str(self.name) + "," + " Email: " + str(self.email) + ", Books Read: " + str(self.books)

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        counter = 0
        for rating in self.books.values():
            counter += rating
        return counter / len(self.books)


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("ISBN now updated to", self.isbn)

    def add_rating(self, rating):
        if 0 <= rating and rating <= 4:
            self.ratings.append(rating)
            print("Rating of", rating, "added")
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        counter = 0
        for rating in self.ratings:
            counter += rating
        return counter / len(self.ratings)

    def __repr__(self):
        return "Title: " + str(self.title) + ", ISBN: " + str(self.isbn) + ", Rating:" + str(self.ratings)

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " " + self.author + " " + str(self.isbn)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + " " + self.subject + " " + self.level + " " + str(self.isbn)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        newBook = Book(title, isbn)
        return newBook

    def create_novel(self, title, author, isbn):
        newNovel = Fiction(title, author, isbn)
        return newNovel

    def create_non_fiction(self, title, subject, level, isbn):
        newNonFiction = Non_Fiction(title, subject, level, isbn)
        return newNonFiction

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email", email)

    def add_user(self, name, email, user_books = None):
        userObj = User(name, email)
        self.users[email] = userObj

        for book in self.books:
            if book != None:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for keys in self.books:
            print(keys)

    def print_users(self):
        for keys in self.users:
            print(keys)

    def get_most_read_book(self):
        self.counter = 0
        self.title = ""
        for key, value in self.books.items():
            if value > self.counter:
                self.counter = value
                self.title = key
        return self.title


    def highest_rated_book(self):
         for title in self.books.keys():
             avg_rate = title.get_average_rating()
             self.books[title] = avg_rate
         max_rating = max(self.books.values())
         for key, value in self.books.items():
             if value == max_rating:
                 return key

    def most_positive_user(self):
         m_pos = {}
         for name in self.users.values():
             avg_rate = name.get_average_rating()
             m_pos[name] = avg_rate
         max_rating = max(m_pos.values())
         for key, value in m_pos.items():
             if value == max_rating:
                 return key

    def __repr__(self):
        return str(self.users) + str(self.books)
