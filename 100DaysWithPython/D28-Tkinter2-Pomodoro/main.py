import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    lbl_timer.config(text="Timer")
    lbl_times.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    # 4 sets de 25 min+5min/1 set de 20min
    if reps%8==0:
        lbl_timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps%2==0:
        lbl_timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        lbl_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    sec=count%60
    if sec<10:
        sec=f"0{sec}"
    txt=str(count//60)+":"+str(sec)
    #alterando o texto do canvas... um pouco diferente a sintaxe
    canvas.itemconfig(timer_text,text=txt)
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks="✔"*(reps//2)
        lbl_times.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window=tk.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

#executando algo depois de x ms
# def say_something(p1,p2,p3):
#     print(f"{1} {2} {3}")
# window.after(1000,say_something,1,2,3)


lbl_timer=tk.Label(text="Timer",bg=YELLOW,fg=GREEN, font=(FONT_NAME,40,"bold"))
lbl_timer.grid(row=0,column=1)

#website para paleta de cores
#https://colorhunt.co
canvas=tk.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=tk.PhotoImage(file="./tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


btn_start=tk.Button(text="Start", command=start_timer)
btn_start.grid(column=0,row=2)

btn_reset=tk.Button(text="Reset", command=reset_timer)
btn_reset.grid(column=2,row=2)

lbl_times=tk.Label(bg=YELLOW,fg=GREEN, font=(FONT_NAME,12,"bold"))
lbl_times.grid(row=3,column=1)

window.mainloop()
