import tkinter
window=tkinter.Tk()
window.title("Hello world!")
window.minsize(width=500,height=300)

my_lbl=tkinter.Label(text="Label", font=("Arial",24,"bold"))
my_lbl.pack() #automatic center on screen
#last line
window.mainloop()