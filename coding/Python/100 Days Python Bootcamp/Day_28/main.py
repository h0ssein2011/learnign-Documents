from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = '✓'

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=20,bg=YELLOW)


#add image
canvas = Canvas(width=200, height=255,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100,112,image=tomato_img )
canvas.create_text(103,130 , text = "00:00",fill='white' ,font=(FONT_NAME , 35 ,'bold'))
canvas.create_text(103,20 , text = "Timer",fill=GREEN ,font=(FONT_NAME , 35 ,'bold'))
canvas.create_text(103,280 , text = TICK,fill=GREEN ,font=(FONT_NAME , 20 ,'bold'))


canvas.pack()

start = Button(window, text = "Start",bg='white')
finish = Button(window, text = "Finish",bg='white')
start.pack(side='left')
finish.pack(side='right')




window.mainloop()