# define Book class
class Book:
    def __init__(self,title,author,ISBN,publisher,count_pages):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publisher = publisher
        self.count_pages = count_pages

class Library:
    def __init__(self,list_of_books,number_of_books):
        self.list_of_books = []
        self.number_of_books = 0
        
    
    def add_book(self,title):
        self.list_of_books.append(title)
        self.number_of_books += 1
    
    def remove_book(self,title):
        self.list_of_books.remove(title)
        self.number_of_books -= 1
    
    def search_books(self,title):
        if title in self.list_of_books:
            print("Found")
        else:
            print(f'{title} is not in the library')

class User:
    def __init__(self,name,email,list_of_borrowed):
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
        self.library = Library()
        self.user_names = []
        self.user_emails = []
    
    def add_book(self,title):
        self.library.list_of_books.append(title)
        self.library.number_of_books += 1
    
    def remove_book(self,title):
        self.library.list_of_books.append(title)
        self.library.number_of_books -= 1
    
    def search_books(self,title):
        if title in self.library.list_of_books:
            print("Found")
        else:
            print(f'{title} is not in the library')
    
    def add_user(self,user_name,user_email):
        self.user_names.append(user_name)
        self.user_emails.append(user_email)
    
    def remove_user(self,user_name,user_email):
        self.user_names.remove(user_name)
        self.user_emails.remove(user_email)

