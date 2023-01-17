from tkinter import *
from tkinter import ttk
from datetime import date
import json

global my_data_list
my_data_list=[]

window=Tk()
window.title("Daily selection")
window.geometry("700x500")

trv=ttk.Treeview(window, columns=(1,2,3,4,5,6,7,8), show="headings",height=16)
trv.grid(column=0,row=0)
trv.heading(1,text="Action", anchor="w")
trv.heading(2,text="ID", anchor="center")
trv.heading(3,text="Task Name", anchor="center")
trv.heading(4,text="Hours spend", anchor="center")
trv.heading(5,text="% completed", anchor="center")
trv.heading(6,text="Start Date", anchor="center")
trv.heading(7,text="Finish Date", anchor="center")
trv.heading(7,text="Include?", anchor="center")

trv.column("#1",anchor="w",width=100,stretch=False)
trv.column("#2",anchor="w",width=100,stretch=False)
trv.column("#3",anchor="w",width=100,stretch=True)
trv.column("#4",anchor="w",width=100,stretch=True)
trv.column("#5",anchor="w",width=100,stretch=True)
trv.column("#6",anchor="w",width=100,stretch=True)
trv.column("#7",anchor="w",width=100,stretch=True)

def load_json():
    global my_data_list
    try:
        with open("C:\\Thiago\\organizer\\tasks.json","r") as dFile:
            my_data_list=json.load(dFile)
    except FileNotFoundError:
        with open("C:\\Thiago\\organizer\\tasks.json","w") as dFile:
            pass
    except:
        pass
    print("File has been read")

def remove_all_from_trv():
    for item in trv.get_children(): trv.delete(item)

def load_trv_with_json():
    global my_data_list
    remove_all_from_trv()
    rowIdx=1
    for key in my_data_list:
        uuid=key["uuid"]
        tName=key["name"]
        hours=key["hours"]
        perc_completed=key["percentage"]
        sDate=key["sDate"]
        fDate=key["fDate"]
        trv.insert('',index='end',iid=rowIdx,text="",
            values=(uuid,tName,hours,perc_completed,sDate,fDate,'N'))
        rowIdx+=1

def trvClicked(event):
    for selected_item in trv.selection():
        item = trv.item(selected_item)
        record = item['values']
        #print(record)
        if (record[-1]=='N'): record[-1]='Y'
        else: record[-1]='N'
        trv.item(selected_item,values=record)
        

trv.bind("<<TreeviewSelect>>",trvClicked)

def saveTodayList():
    today=date.today().strftime("%Y-%m-%d")
    print(today)
    daily={
        "date":today,
        "items": []
    }
    for item in trv.get_children():
        line=trv.item(item)['values']
        if line[-1]=='Y':
            daily['items'].append(line[0])
    fName=today+'.json'
    with open("C:\\Thiago\\organizer\\"+fName,"w") as dFile:
        json.dump(daily,dFile,indent=4)

btnSave=Button(window,text="Save",padx=5,pady=10,command=saveTodayList)
btnSave.grid(row=2,column=0,sticky='N')

load_json()
load_trv_with_json()

window.mainloop()