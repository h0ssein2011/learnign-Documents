# define Book class
class Book:
    def __init__(self,title,author,ISBN,publisher,count_pages):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publisher = publisher
        self.count_pages = count_pages

class Library:
    def __init__(self,list_of_books):
        self.list_of_books = list_of_books
        self.number_of_books = len(list_of_books)
        
    
    def add_book(self,title,author,ISBN,publisher,count_pages):
        new_book = Book(title,author,ISBN,publisher,count_pages)
        self.list_of_books.append(new_book)
    
    def remove_book(self,book):
        self.list_of_books.remove(book)
    
    def search_books(self,title):
        title_list = [book.title for book in self.list_of_books]
        if title in title_list:
            print(f"{title} is Found")
        else:
            print(f'{title} is not in the library')

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.list_of_borrowed = [] 

    def borrow_book(self,title):
        self.list_of_borrowed.append(title)

    def return_book(self,title):
        self.list_of_borrowed.remove(title)

class Admin:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        self.user_names = []
        self.user_emails = []
    
    def add_book(self,Library,title,author,ISBN,publisher,count_pages):
        new_book = Book(title,author,ISBN,publisher,count_pages)
        Library.add_book(new_book)
    
    
    def remove_book(self,Library,book):
        Library.remove_book(book)
    
    def search_books(self,Library,title):
        Library.search_books(title)
    
    def add_user(self,user_name,user_email):
        if user_name not in self.user_names:
            new_user = User(name = user_name,email=user_email)
            self.user_names.append(new_user.name)
            self.user_emails.append(new_user.email)
      
    
    def remove_user(self,user):
        if user.name in self.user_names:
            self.user_names.remove(user.name)
            self.user_emails.remove(user.email)

