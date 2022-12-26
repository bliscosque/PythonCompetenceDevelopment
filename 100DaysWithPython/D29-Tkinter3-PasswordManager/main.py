import tkinter as tk
# usado para messagebox
from tkinter import messagebox

# Documentacao dos widgets do Tk: https://tkdocs.com/tutorial/widgets.html
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def addToFile():
    site=ipt_website.get()
    email=ipt_email.get()
    passwd=ipt_pass.get()
    if len(site)==0 or len(email)==0 or len(passwd)==0:
        messagebox.showwarning(title="Error", message="Cannot save due to empty fields")
        return
    isOk=messagebox.askokcancel(title=site, message=f"Save to file?")
    if not isOk: return
    with open("data.txt", "a") as dFile:    
        dFile.writelines(f"{site} | {email} | {passwd}\n")
    #limpando os campos
    ipt_website.delete(0,tk.END)
    ipt_pass.delete(0,tk.END)

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

ipt_website=tk.Entry(width=50)
ipt_website.grid(row=1,column=1,columnspan=2, sticky="EW")
ipt_website.focus()
ipt_email=tk.Entry(width=50)
ipt_email.grid(row=2,column=1,columnspan=2, sticky="EW")
ipt_email.insert(0,"bliscosque@yahoo.com.br") #0: insere no inicio; END: no final
ipt_pass=tk.Entry(width=20)
ipt_pass.grid(row=3,column=1, sticky="EW")

btn_generate=tk.Button(text="Generate Password")
btn_generate.grid(column=2,row=3, sticky="EW")
btn_add=tk.Button(text="Add", width=36, command=addToFile)
btn_add.grid(column=1,row=4, columnspan=2, sticky="EW")

window.mainloop()