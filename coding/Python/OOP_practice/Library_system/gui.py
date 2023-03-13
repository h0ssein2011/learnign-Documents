from tkinter import *
from main import Admin,Library,Book
from data_system import read_books_data,read_user_data

library = Library(read_books_data())


# user_list = read_user_data()

window = Tk()
window.title('Library Management System')
window.geometry('1400x1700')

window.config(padx=100, pady=20)

wc_label = Label(window, text='Welcome to the Library!')
wc_label.grid(row=1,column=1)


admin = Admin(name='John Doe', email='johndoe@example.com', password='password')

def add_book_by_admin():
    title_entry = Entry(window)
    title_entry.grid(row=2, column=1)  
    title = title_entry.get()  
    
    author_entry = Entry(window)
    author_entry.grid(row=2, column=1)
    author = author_entry.get()

    ISBN_entry = Entry(window)
    ISBN_entry.grid(row=3, column=1)    
    ISBN = ISBN_entry.get()
    
    publisher_entry = Entry(window)
    publisher_entry.grid(row=4, column=1)    
    publisher = publisher_entry.get()
    
    count_pages_entry = Entry(window)
    count_pages_entry.grid(row=5, column=1)
    count_pages = count_pages_entry.get()

    new_book = Book(title, author, ISBN, publisher, count_pages)
    admin.add_book(new_book)
    

add_bk_btn = Button(window, text='Add a new Book',command=add_book_by_admin)
add_bk_btn.grid(row=2,column=1)

window.mainloop()
