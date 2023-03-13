from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
TICK = '✓'
reps = 0
counter_zero = False
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(title_label,text='Timer',fg=RED) 
    check_marks.config(text = "")
    global reps
    reps = 0


    
# ---------------------------- TIMER ME CHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break_sec) 
        title_label.config(title_label,text='Short',fg=RED)   
    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(title_label,text='Long',fg=PINK) 
    else :
        count_down(work_sec)
        title_label.config(title_label,text='Working',fg=GREEN) 
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps
    count_min = math.floor(count /  60)
    count_sec = count % 60
    canvas.itemconfig(timer_text,text=f'{count_min:02d}:{count_sec:02d}')
    if count > 0 :
        global timer
        timer = window.after(1000,count_down,count -1 )
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2 )
        for _ in range(work_sessions):
            marks += TICK
            check_marks.config(text = marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=20,bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

#add image
canvas = Canvas(width=290, height=255,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100,112,image=tomato_img )


timer_text = canvas.create_text(103,130 , text = "00:00",fill='white' ,font=(FONT_NAME , 35 ,'bold'))
canvas.grid(column=1, row=1)



start_button = Button(window, text = "Start",bg='white' ,command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(window, text = "Reset",bg='white',command=reset_timer)
reset_button.grid(column=2, row=2)


check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()