import tkinter as tk

def calcular_clicked():
    miles=float(input.get())
    km=miles*1.60934
    lbl_ans["text"]=round(km)

window=tk.Tk()
window.title("Conversor milhas para Km")
window.config(padx=20,pady=20)

input=tk.Entry(width=10)
input.grid(row=0,column=1)

lbl_miles=tk.Label(text="milhas")
lbl_miles.grid(row=0,column=2)

lbl_equals=tk.Label(text="é igual a")
lbl_equals.grid(row=1,column=0)

lbl_ans=tk.Label(text="Km")
lbl_ans.grid(row=1,column=1)

lbl_km=tk.Label(text="Km")
lbl_km.grid(row=1,column=2)

btn=tk.Button(text="Calcular", command=calcular_clicked)
btn.grid(row=2,column=1)

window.mainloop()