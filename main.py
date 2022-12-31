from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip



window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#Password Generator Project

def generate_password():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter=[choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]

    password_list=password_letter+password_numbers+password_symbols

    shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)






#saving files function
def save():
    website=web_entry.get()
    username=email_entry.get()
    Password1=password_entry.get()

    if len(website) == 0 or len(Password1)==0:
        messagebox.showinfo(title='OOPS',message="Please make sure you Entered all fields ")
    else:
        messagebox.askokcancel(title=website,message=f"Details you Entered :\n Email:{username}"
                           f"\nPassword: {Password1}\n is it ok to save")


    with open("demo.txt","a") as file:
        file.write(f"{website} | {username} | {Password1}\n")
        web_entry.delete(0,END)
        password_entry.delete(0, END)

#canvas
canvas=Canvas(height=200,width=200)
rec=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=rec)
canvas.grid(row=0,column=1)

web=Label(text='Website')
web.grid(row=1,column=0)
Username=Label(text='Username')
Username.grid(row=2,column=0)
Pass=Label(text='Password')
Pass.grid(row=3,column=0)


#Entries
web_entry=Entry(width=35)
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'vignesh.vj@vastar.io')
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

#button

generte=Button(text="Generate Password",command=generate_password)
generte.grid(row=3,column=2,columnspan=2)
Add=Button(text='Add',width=36,command=save)
Add.grid(row=4,column=1,columnspan=2)




window.mainloop()