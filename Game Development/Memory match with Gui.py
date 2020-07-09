import tkinter as tk  
m = tk.Tk()

m.title('Counting Seconds')

# label = tk.Label(text='what is your name? ',foreground='red',background='#FF00FF')
txt =  tk.Entry(text='name', width=24)
txt.insert(0,'Just do it')
button = tk.Button(m,text='Finish',width = 25 , command=m.destroy)

name = txt.get()
print(name)
# label.pack()
button.pack()
txt.pack()

m.mainloop()

