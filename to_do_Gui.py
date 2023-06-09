import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import dbh

def add():
    if (len(addTask.get()) == 0):
        messagebox.showerror("Error", "No data available\nPlease Enter Some Task")
    else:
        dbh.insertTask(addTask.get())
        addTask.delete(0, END)
        populate()

def populate():
    listbox.delete(0, END)
    for rows in dbh.showdb():
        listbox.insert(END, rows[1])

def deletetask(event):
    dbh.deletyByTask(listbox.get(ANCHOR))
    populate()

main = tkinter.Tk()
main.title("TODO")
main.geometry("500x600")
main.resizable(False, False)
main.configure(
    background = '#1d1d1d',
)

tk.Label(
    main,
    text= "TASK MANAGER",
    bg= '#1d1d1d',
    fg= "#eeeeee",
    font= ("Verdana 20")
).pack()

addframe = tk.Frame(
    main,
    bg= '#eeeeee'
)
# addframe.pack(pady = 15)
addframe.place(x= 10, y=80, width=250, height= 30)

addTask = tk.Entry(
    addframe,
    font= "Verdana",
    bg= '#eeeeee',
)
addTask.pack(ipadx= 12, ipady = 5)

addbtn = tk.Button(
    main,
    text= "ADD TASK",
    command= add,
    bg= '#000000',
    fg='#eeeeee',
    relief= 'raised',
    font= ('Verdana', 12),
    highlightcolor= 'green',
    activebackground= '#1D1D1D',
    activeforeground= 'white',
    bd=0,
)
addbtn.place(x= 270, y=78)
# addbtn.pack(padx= 100,ipadx= 20, ipady= 5)

tk.Label(
    main,
    text="Your tasks",
    font=('Calibri', 15),
    bg='#1d1d1d',
    fg='white'
).place(x=80,y=130)
# tk.Label(main, text="Position 1 : x=0, y=0", bg="black", fg="white").place(x=5, y=10)
taskframe = tk.Frame(
    main,
    bg='#1d1d1d',
)
taskframe.place(x= 10, y = 180, width= 255, height=380)

scrollbar = Scrollbar(taskframe)
scrollbar.pack(side= RIGHT, fill= Y)

listbox = Listbox(
    taskframe,
    font='Verdana 18',
    bg='#1d1d1d',
    fg='white',
    selectbackground= 'red',

)
listbox.pack(fill= BOTH, expand= 300)
listbox.config(yscrollcommand=scrollbar.set)
listbox.bind("<Double-Button-1>", deletetask)
listbox.bind("<Delete>", deletetask)
scrollbar.config(command=listbox.yview)

tk.Label(
    main,
    text= "Tip: Double click to delete a task",
    bg= '#1d1d1d',
    fg= 'yellow',
    font=("Centaur 13")
).pack(side= BOTTOM)

populate()
main.mainloop()