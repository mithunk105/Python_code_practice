from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pwd_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)
    alpha_list = []

    alpha_list += [choice(letters) for _ in range(1, nr_letters + 1)]
    alpha_list += [choice(symbols) for _ in range(1, nr_symbols + 1)]
    alpha_list += [choice(numbers) for _ in range(1, nr_numbers + 1)]

    shuffle(alpha_list)
    pwd = "".join(alpha_list)
    pwd_entry.insert(0, pwd)
    pyperclip.copy(pwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_file():

    web = web_entry.get()
    email = email_entry.get()
    pwd = pwd_entry.get()
    if web == "" or pwd == "":
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email}\n"
                                                          f"Password: {pwd}")

        if is_ok:
            with open("data_list.txt", mode="a") as data_file:
                data_file.write(f"{web} | {email} | {pwd}\n")

            web_entry.delete(0, END)
            pwd_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

web_lable = Label(text="Website: ")
web_lable.grid(row=1, column=0)

email_lable = Label(text="Email/Username: ")
email_lable.grid(row=2, column=0)

email_lable = Label(text="Password: ")
email_lable.grid(row=3, column=0)

button = Button(text="Generate", width=12, command=pwd_gen)
button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, command=save_file)
add_button.grid(row=4, column=1, columnspan=2)

web_entry = Entry(width=50)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=50)
email_entry.insert(0, "mithun@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

pwd_entry = Entry(width=34)
pwd_entry.grid(row=3, column=1)

window.mainloop()
