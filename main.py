from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- SEARCH FILE --------------------------------------
def find_password():
    website_search = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning message", message="No data file found")
    else:
        if website_search in data:
            messagebox.showinfo(title="Search Results", message=f"website: {website_search}\npassword: "
                                                                f"{data[website_search]['password']}"
                                                                f"\nEmail:{data[website_search]['email']}")
        else:
            messagebox.showinfo(title="No data Found", message=f"{website_search} was not found in the file.")

# ---------------------------- PASSWORD GENERATOR -------------------------------


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Creates letters, symbols and numbers list using list comprehension
    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list

    # Shuffles the password list to get a list of characters, numbers and letters in no specific order
    random.shuffle(password_list)

    password = "".join(password_list)

    # Inserts the generated password into the appropriate field
    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # Acquire the input from respective fields
    website_data = website_input.get()
    eu_input_data = eu_input.get()
    password = pass_input.get()
    new_data = {
        website_data: {
            "email": eu_input_data,
            "password": password,
        }
    }

    # Checks if fields are empty
    if len(website_data) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="You need to input the website and the password in order for "
                                                        "the data to be saved.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            pass_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", fg="black", bg="white", font=("arial", 10, "bold"), highlightthickness=0)
website_label.grid(column=0, row=1)
eu_label = Label(text="Email/Username:", fg="black", bg="white", font=("arial", 10, "bold"), highlightthickness=0)
eu_label.grid(column=0, row=2)
pass_label = Label(text=" Password:", fg="black", bg="white", font=("arial", 10, "bold"), highlightthickness=0)
pass_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=24)
website_input.grid(column=1, row=1)
website_input.focus()
eu_input = Entry(width=40)
eu_input.grid(column=1, row=2, columnspan=2)
eu_input.insert(0, "constantin.penisoara@yahoo.com")
pass_input = Entry(width=24)
pass_input.grid(column=1, row=3)


# Buttons
pass_button = Button(width=15, text="Generate Password", font=("arial", 10, "bold"), bg="white", pady=0,
                     command=generate_password)
pass_button.grid(column=2, row=3)
add_button = Button(width=43, text="Add", font=("arial", 10, "bold"), fg="black", bg="white", highlightthickness=0,
                    command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(width=15, text="Search", font=("arial", 10, "bold"), bg="white", pady=0, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()
