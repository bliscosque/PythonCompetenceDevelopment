#https://docs.python.org/3/library/tk.html
import tkinter
window=tkinter.Tk()
window.title("Hello world!")
window.minsize(width=500,height=300)

my_lbl=tkinter.Label(text="Label", font=("Arial",24,"bold"))
my_lbl.pack() #automatic center on screen

#2 maneiras de alterar uma propriedade
my_lbl["text"]="New text"
my_lbl.config(text="New text 2")

#button
def button_clicked():
    my_lbl["text"]=input.get()

button=tkinter.Button(text="Click me",command=button_clicked)
button.pack()

#Entry
input=tkinter.Entry(width=10)
input.pack()

#last line
window.mainloop()