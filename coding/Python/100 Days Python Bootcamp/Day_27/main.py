from tkinter import *

window = Tk()
window.title('My first GUI programm')
window.minsize(width=500 ,height=300 )


my_label = Label(text='I am here to test')
my_label.pack(side ='top')

input = Entry(width = 10)
input.pack()

def add_label():
        new_text =input.get()
        my_label.config(text=new_text)
        





button = Button(text='Click me' ,command=add_label)
button.pack(side ='left')




window.mainloop()