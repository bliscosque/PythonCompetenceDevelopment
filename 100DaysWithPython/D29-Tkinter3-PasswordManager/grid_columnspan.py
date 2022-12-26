from tkinter import *

window = Tk()

r = Label(bg="red", width=20, height=5)
r.grid(row=0, column=0)

g = Label(bg="green", width=20, height=5)
g.grid(row=1, column=1)

b = Label(bg="blue", width=40, height=5)
b.grid(row=2, column=0, columnspan=2) # faz um span para 2 colunas (ocupando coluna 0 e 1)


window.mainloop()