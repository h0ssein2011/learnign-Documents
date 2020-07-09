import tkinter as tk  
m = tk.Tk()

m.title('Counting Seconds')

button = tk.Button(m,text='stop',width = 25 , command=m.destroy)
button.pack()
m.mainloop()


