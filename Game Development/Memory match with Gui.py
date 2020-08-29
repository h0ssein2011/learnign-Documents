import tkinter as tk  
m = tk.Tk()

m.title('Counting Seconds')

# label = tk.Label(text='what is your name? ',foreground='red',background='#FF00FF')
txt =  tk.Entry(text='name', width=24)
txt.insert(0,'Just do it')
txt.pack()
button = tk.Button(m,text='Finish',width = 25 , command=m.destroy)

name = txt.get()
print(name)
# label.pack()
button.pack()


m.mainloop()



import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()




# simple temprature calculator
import tkinter as tk
def faranhite_to_celcious():
    faranhite = ent_temoarture.get()
    celcious = (5/9) * (float(faranhite) - 32)
    lbl_result['text'] = f"{round(celcious, 2)} \N{DEGREE CELSIUS}"


window = tk.Tk()

window.title('simple temprature calculator')
frm_entry = tk.Frame(master = window)
ent_temoarture = tk.Entry(master=frm_entry , width=10)
lbm_label = tk.Label(master = frm_entry , text="\N{DEGREE FAHRENHEIT}")


ent_temoarture.grid(row = 0 , column=0 ,sticky='e')
lbm_label.grid(row = 0 , column=1 ,sticky='w')

btn_convert =tk.Button(master = window , 
                       text="\N{RIGHTWARDS BLACK ARROW}",
                       command=faranhite_to_celcious)
lbl_result = tk.Label(master=window , text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0,column=0 ,padx=100)
btn_convert.grid(row=0,column=1 ,pady=10)
lbl_result.grid(row=0,column=2 ,padx=10)

window.mainloop()




from tkinter import *

from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("./Pics/1.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
    def load_image(self):
        
        
root = Tk()
app = Window(root)
root.wm_title("")
root.geometry("400x320")
root.mainloop()


