from main import Book, User
import json

##### read Books data 

def read_books_data():

    with open('books_data.json','r') as f:
        data = json.load(f)
    book_list = []
    for book_data in data:
        new_book = Book(**book_data)
        book_list.append(new_book)
    
    return book_list


def read_user_data():

    with open('user_data.json','r') as f:
        data = json.load(f)
    user_list = []
    for user_data in data:
        new_user = User(**user_data)
        user_list.append(new_user)
    
    return user_list
    

    





# print(Books[0].title,Books[0].author,Books[0].ISBN)