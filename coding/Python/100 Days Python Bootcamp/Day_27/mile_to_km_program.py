from tkinter import *



window = Tk()
window.title('Mile to KM conversion programm')
window.minsize(width=500 ,height=300 )


Miles_label = Label(text='in Miles')
Miles_label.grid(column=1,row=0)

input = Entry(width = 10)
input.grid(column=1,row=0)

def Mile_to_Km(conversion_rate = 1.60):
    km = int(input.get()) * conversion_rate
    Km_label.config(text=f'{km}')
    
Km_label = Label(text=0) 
Km_label.grid(column=1,row=1)

        

calc_button = Button(text='Calculate' ,command=Mile_to_Km)
calc_button.grid(column=2,row=1)





window.mainloop()