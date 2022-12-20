import tkinter

def button_clicked():
    my_lbl["text"]=input.get()

window=tkinter.Tk()
window.title("Playing around with Tkinter")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

my_lbl=tkinter.Label(text="Label", font=("Arial",24,"bold"))
my_lbl.grid(column=0,row=0) #automatic center on screen

#button
button=tkinter.Button(text="Click me",command=button_clicked)
button.grid(column=1,row=0)

#Entry
input=tkinter.Entry(width=10)
input.grid(column=0,row=1)

#last line
window.mainloop()