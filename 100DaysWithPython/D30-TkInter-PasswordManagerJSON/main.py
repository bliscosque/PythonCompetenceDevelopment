import tkinter as tk
# usado para messagebox
from tkinter import messagebox
from random import choice, randint, shuffle
# https://pypi.org/project/pyperclip/
# pip install pyperclip
import pyperclip
import json

# Documentacao dos widgets do Tk: https://tkdocs.com/tutorial/widgets.html
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    ipt_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def addToFile():
    site=ipt_website.get()
    email=ipt_email.get()
    passwd=ipt_pass.get()
    new_data={
        site: {
            "email": email,
            "password": passwd,
        }
    }
    if len(site)==0 or len(email)==0 or len(passwd)==0:
        messagebox.showwarning(title="Error", message="Cannot save due to empty fields")
        return
    isOk=messagebox.askokcancel(title=site, message=f"Save to file?")
    if not isOk: return
    try:
        with open("data.json", "r") as dFile:
            data=json.load(dFile)
    except FileNotFoundError:
        with open("data.json", "w") as dFile:
            json.dump(new_data,dFile, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as dFile:
            json.dump(data,dFile, indent=4)
    finally:
        #limpando os campos
        ipt_website.delete(0,tk.END)
        ipt_pass.delete(0,tk.END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    site=ipt_website.get()
    try:
        with open("data.json", "r") as dFile:
            data=json.load(dFile)
            #print(data[site])
            ipt_pass.delete(0,tk.END)
            ipt_pass.insert(0,data[site]['password'])
            ipt_email.delete(0,tk.END)
            ipt_email.insert(0,data[site]['email'])
    except FileNotFoundError:
        messagebox.showwarning(message="site not found")
    except KeyError:
        messagebox.showwarning(message="site not found")
    
# ---------------------------- UI SETUP ------------------------------- #
window=tk.Tk()
window.title("PasswordManager")
window.config(padx=50,pady=50)

# Mais informacoes sobre canvas: https://tkdocs.com/tutorial/canvas.html
canvas=tk.Canvas(width=200,height=200)
logo_img=tk.PhotoImage(file="./logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

lbl_website=tk.Label(text="Website:")
lbl_website.grid(row=1,column=0)
lbl_email=tk.Label(text="Email/Username:")
lbl_email.grid(row=2,column=0)
lbl_pass=tk.Label(text="Password:")
lbl_pass.grid(row=3,column=0)

ipt_website=tk.Entry(width=20)
ipt_website.grid(row=1,column=1, sticky="EW")
ipt_website.focus()
ipt_email=tk.Entry(width=50)
ipt_email.grid(row=2,column=1,columnspan=2, sticky="EW")
ipt_email.insert(0,"bliscosque@yahoo.com.br") #0: insere no inicio; END: no final
ipt_pass=tk.Entry(width=20)
ipt_pass.grid(row=3,column=1, sticky="EW")

btn_search=tk.Button(text="Search", command=search)
btn_search.grid(column=2,row=1, sticky="EW")
btn_generate=tk.Button(text="Generate Password", command=generate_password)
btn_generate.grid(column=2,row=3, sticky="EW")
btn_add=tk.Button(text="Add", width=36, command=addToFile)
btn_add.grid(column=1,row=4, columnspan=2, sticky="EW")

window.mainloop()