from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().capitalize()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nWebsite: {website}\n"
                                                      f"Email/Username: {email}\nPassword: {password}")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ----------------------- SEARCH FOR WEBSITE -------------------------- #
def search():
    website = website_entry.get().capitalize()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

            email = data[website]['email']
            password = data[website]['password']

            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

    except KeyError:
        if website == "":
            pass
        else:
            messagebox.showerror(title="Oops", message="File not exist")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
lbl1 = Label(text="Website:")
lbl1.grid(row=1, column=0)

lbl2 = Label(text="Email/Username:")
lbl2.grid(row=2, column=0)

lbl3 = Label(text="Password:")
lbl3.grid(row=3, column=0)

# Entries
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "asd@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2)

add_btn = Button(text="Add", width=44, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="w")

search_btn = Button(text="Search", width=14, command=search)
search_btn.grid(row=1, column=2)

window.mainloop()
