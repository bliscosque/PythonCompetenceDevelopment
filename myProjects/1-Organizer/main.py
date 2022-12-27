from tkinter import *
from tkinter import ttk
import uuid
import json

global my_data_list
global currentWorIndex

my_data_list=[]

window1=Tk()
window1.geometry("760x500")
window1.title("Task Management")
window1.config(padx=10,pady=10)

def newTask():
    blankTuple=('','','','')
    open_popup('add', blankTuple, window1)

btnNewTask=Button(window1, text="Add Task", padx=2, pady=3, command=newTask)
btnNewTask.grid(row=0,column=0,sticky="we")

trv=ttk.Treeview(window1, columns=(1,2,3,4,5,6,7), show="headings",height=16)
trv.grid(row=1,column=0, rowspan=16,columnspan=5)
trv.heading(1,text="Action", anchor="w")
trv.heading(2,text="ID", anchor="center")
trv.heading(3,text="Task Name", anchor="center")
trv.heading(4,text="Hours spend", anchor="center")
trv.heading(5,text="% completed", anchor="center")
trv.heading(6,text="Start Date", anchor="center")
trv.heading(7,text="Finish Date", anchor="center")

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
            values=('edit',uuid,tName,hours,perc_completed,sDate,fDate))
        rowIdx+=1

def trvClicked(event):
    global trv
    currentRowIdx=trv.selection()[0]
    lastTuple=(trv.item(currentRowIdx,'values'))
    open_popup('edit',lastTuple,window1)

def open_popup(_mode,_tuple,primary):
    global myname
    child_window=Toplevel(primary)
    child_window.geometry("750x500")
    child_window.title("Add/Edit Task")
    child_window.grab_set() # allow to receive events/prevent interacting with main window
    #load_form=True
    ipt_frame=LabelFrame(child_window,text="Enter new task")
    ipt_frame.grid(row=0,rowspan=10,column=0,columnspan=10)

    lbl_ID=Label(ipt_frame,text="ID: ",width=25,anchor="w")
    lbl_name=Label(ipt_frame,text="Task Name: ",width=25,anchor="w")
    lbl_hours=Label(ipt_frame,text="Hours spend: ",width=25,anchor="w")
    lbl_per_completed=Label(ipt_frame,text="% Completed: ",width=25,anchor="w")
    lbl_start_date=Label(ipt_frame,text="Start Date: ",width=25,anchor="w")
    lbl_finish_date=Label(ipt_frame,text="Finish Date: ",width=25,anchor="w")
    lbl_ID.grid(column=0,row=0,padx=1,pady=0)
    lbl_name.grid(column=0,row=1,padx=1,pady=0)
    lbl_hours.grid(column=0,row=2,padx=1,pady=0)
    lbl_per_completed.grid(column=0,row=3,padx=1,pady=0)
    lbl_start_date.grid(column=0,row=4,padx=1,pady=0)
    lbl_finish_date.grid(column=0,row=5,padx=1,pady=0)

    id_value=StringVar()
    id_value.set(uuid.uuid4())

    ipt_id=Label(ipt_frame,anchor="w",textvariable=id_value)
    ipt_id.grid(row=0,column=1)
    ipt_name=Entry(ipt_frame,width=30)
    ipt_name.grid(row=1,column=1)
    ipt_hours=Entry(ipt_frame,width=30)
    ipt_hours.grid(row=2,column=1)
    ipt_per_completed=Entry(ipt_frame,width=30)
    ipt_per_completed.grid(row=3,column=1)
    ipt_start_date=Entry(ipt_frame,width=30)
    ipt_start_date.grid(row=4,column=1)
    ipt_finish_date=Entry(ipt_frame,width=30)
    ipt_finish_date.grid(row=5,column=1)

    def delete_task():
        uuid=ipt_id.cget("text") #get info from a label
        name=ipt_name.get()
        hours=ipt_hours.get()
        perComp=ipt_per_completed.get()
        sDate=ipt_start_date.get()
        fDate=ipt_finish_date.get()
        process_request('_DELETE_',uuid,name,hours,perComp,sDate,fDate)
        reload_main_form()
        child_window.grab_release()
        child_window.destroy()
        child_window.update()
        
    def determineAction():
        #if load_form==False:
        if _mode=="edit":
            update_entry()
        else:
            add_entry()
        reload_main_form()
        child_window.grab_release()
        child_window.destroy()
        child_window.update()

    def child_cancel():
        child_window.grab_release()
        child_window.destroy()
        child_window.update()

    btnAdd=Button(ipt_frame,text="Save",padx=5,pady=10,command=determineAction)
    btnAdd.grid(row=6,column=0)

    btnDelete=Button(ipt_frame,text="Delete",padx=5,pady=10,command=delete_task)
    btnDelete.grid(row=6,column=1)

    btnCancel=Button(ipt_frame,text="Cancel",padx=5,pady=10,command=child_cancel)
    btnCancel.grid(row=6,column=2)

    #load_form=False



    def reload_main_form():
        load_trv_with_json()

    def process_request(command_type, uuid,name,hours,perComp,sDate,fDate):
        global my_data_list
        global dirty
        dirty=True
        if command_type=='_UPDATE_':
            row=find_row_in_my_data_list(uuid)
            print(f"row: {row}")
            if row>=0:
                dict={"uuid":uuid, "name": name, "hours": hours, "percentage": perComp, "sDate":sDate,"fDate": fDate}
                my_data_list[row]=dict
        elif command_type=='_INSERT_':
            dict={"uuid":uuid, "name": name, "hours": hours, "percentage": perComp, "sDate":sDate,"fDate": fDate}
            my_data_list.append(dict)
        elif command_type=='_DELETE_':
            row=find_row_in_my_data_list(uuid)
            if row>=0:
                del my_data_list[row]
        save_json_to_file()
        clear_all_fields()

    def add_entry():
        uuid=ipt_id.cget("text")
        name=ipt_name.get()
        hours=ipt_hours.get()
        perComp=ipt_per_completed.get()
        sDate=ipt_start_date.get()
        fDate=ipt_finish_date.get()
        process_request('_INSERT_',uuid,name,hours,perComp,sDate,fDate)
    
    def update_entry():
        print("update entry")
        uuid=ipt_id.cget("text")
        name=ipt_name.get()
        hours=ipt_hours.get()
        perComp=ipt_per_completed.get()
        sDate=ipt_start_date.get()
        fDate=ipt_finish_date.get()
        process_request('_UPDATE_',uuid,name,hours,perComp,sDate,fDate)

    def load_edit_field_with_row_data(_tuple):
        if len(_tuple)==0: return
        id_value.set(_tuple[1])
        ipt_name.delete(0,END)
        ipt_name.insert(0,_tuple[2])
        ipt_hours.delete(0,END)
        ipt_hours.insert(0,_tuple[3])
        ipt_per_completed.delete(0,END)
        ipt_per_completed.insert(0,_tuple[4])
        ipt_start_date.delete(0,END)
        ipt_start_date.insert(0,_tuple[5])
        ipt_finish_date.delete(0,END)
        ipt_finish_date.insert(0,_tuple[6])

    if _mode=='edit':
        load_edit_field_with_row_data(_tuple)

    def find_row_in_my_data_list(uuid):
        global my_data_list
        row=0
        found=False
        for rec in my_data_list:
            if rec["uuid"]==uuid:
                found=True
                break
            row+=1
        if found==True: return row
        return -1

    def save_json_to_file():
        global my_data_list
        with open("C:\\Thiago\\organizer\\tasks.json","w") as dFile:
            json.dump(my_data_list,dFile,indent=4)
        print('file has been written')

    def clear_all_fields():
        ipt_name.delete(0,END)
        ipt_hours.delete(0,END)
        ipt_per_completed.delete(0,END)
        ipt_start_date.delete(0,END)
        ipt_finish_date.delete(0,END)
        id_value.set(uuid.uuid4())
        ipt_id.configure(text="")
        ipt_name.focus()

trv.bind("<ButtonRelease>",trvClicked)
load_json()
load_trv_with_json()

window1.mainloop()