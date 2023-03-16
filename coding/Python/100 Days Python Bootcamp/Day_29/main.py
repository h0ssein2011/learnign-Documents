from tkinter import *

window = Tk()
window.title('password manager')
window.config(padx=50, pady=50)






# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

#add image
canvas = Canvas(width=300, height=200,highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img )
canvas.grid(column=1, row=0)


website_label = Label(text="Website")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1,columnspan=2)


email_label = Label(text="Email/username")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2,columnspan=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

gen_pass = Button(window, text = "Generate Password")
gen_pass.grid(column=2, row=3)


add_button = Button(window, text = "Add",bg='white',width=36)
add_button.grid(column=1, row=4,columnspan=2)




window.mainloop()