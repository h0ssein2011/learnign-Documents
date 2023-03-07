from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
TICK = '✓'
reps = 0
counter_zero = False

# ---------------------------- TIMER RESET ------------------------------- # 

    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break_sec) 
        canvas.itemconfig(label_text,text='Short break',fg=RED)   
    elif reps % 8 == 0:
        count_down(long_break_sec)
        canvas.itemconfig(label_text,text='Long break',fg=PINK) 
    else :
        count_down(work_sec)
        canvas.itemconfig(label_text,text='Working Time',fg=GREEN) 
    
    

    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count /  60)
    count_sec = count % 60
    canvas.itemconfig(timer_text,text=f'{count_min:02d}:{count_sec:02d}')
    if count > 0 :
        window.after(100,count_down,count -1 )
    else:
        start_timer()
        check_mark.config(text = TICK)


   



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=20,bg=YELLOW)



#add image
canvas = Canvas(width=200, height=255,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100,112,image=tomato_img )
timer_text = canvas.create_text(103,130 , text = "00:00",fill='white' ,font=(FONT_NAME , 35 ,'bold'))
label_text = canvas.create_text(103,20 , text = "Timer",fill=GREEN ,font=(FONT_NAME , 15 ,'bold'))



check_mark = Label(fg=GREEN , bg= YELLOW)


canvas.pack()

start = Button(window, text = "Start",bg='white' ,command=start_timer)
finish = Button(window, text = "Finish",bg='white')
start.pack(side='left')
finish.pack(side='right')




window.mainloop()