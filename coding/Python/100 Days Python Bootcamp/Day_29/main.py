import string
from tkinter import *
from tkinter import messagebox
import random




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(length = 10):
    # Define a string of characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(chars) for i in range(length))
    password_entry.delete(0,END)
    password_entry.insert(0,string= password)
    
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0  or len(password) == 0:
        messagebox.showinfo(title="Opps",message="Please dont leave blank eny entry")
    else :

        is_ok = messagebox.askokcancel(title='Confirmation' , 
                           message=f'these are the details of the information :{website} \n {email} \n {password}')
        if is_ok:
            with open('data.txt','a') as  f:
                
                f.write(f'{website} | {email} | {password}')
                website_entry.delete(0,END)
                password_entry.delete(0,END)

                f.write('\n')
        



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('password manager')
window.config(padx=50, pady=50)

#add image
canvas = Canvas(width=200, height=200,highlightthickness=0)
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
email_entry.insert(0,'hossein@gmail.com')
email_entry.grid(column=1, row=2,columnspan=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

gen_pass = Button(window, text = "Generate Password" ,command=generate_password)
gen_pass.grid(column=2, row=3)


add_button = Button(window, text = "Add",bg='white',width=36,command=save)
add_button.grid(column=1, row=4,columnspan=2)




window.mainloop()