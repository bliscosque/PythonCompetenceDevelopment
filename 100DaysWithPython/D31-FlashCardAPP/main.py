from tkinter import *
import os
BACKGROUND_COLOR = "#B1DDC6"

curPath=os.path.dirname(os.path.realpath(__file__))

window=Tk()
window.title("Thiago's Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=526)
card_front_img=PhotoImage(file=curPath+"/images/card_front.png")
canvas.create_image(400,263,image=card_front_img)
canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
canvas.create_text(400,263,text="word",font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_img=PhotoImage(file=curPath+"/images/wrong.png")
unknown_button=Button(image=cross_img, highlightthickness=0)
unknown_button.grid(row=1,column=0)

check_img=PhotoImage(file=curPath+"/images/right.png")
known_button=Button(image=check_img, highlightthickness=0)
known_button.grid(row=1,column=1)





window.mainloop()