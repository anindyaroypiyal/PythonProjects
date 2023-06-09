import tkinter as tk
from tkinter import *
from tkinter import messagebox
import dbh

main = tk.Tk()
main.title("TODO")
main.geometry("330x635+1590+140")
main.resizable(False, False)
main.configure(
    background = '#101010',
)


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

def Bin():
    listbox2.delete(0, END)
    for rows in dbh.showdlt():
        listbox2.insert(END, rows[1])

def deletetask(event):
    dbh.deletyByTask(listbox.get(ANCHOR))
    populate()
    Bin()

def remove(event):
    dbh.deletyByTask2(listbox2.get(ANCHOR))
    populate()
    Bin()

#remove title bar
main.overrideredirect(True)

def move_app(e):
    main.geometry(f'+{e.x_root}+{e.y_root}')
def quitter(e):
    main.quit()

title_close = Label(main, text="❖ ", bg= '#101010', fg= 'red', bd=0, relief= "sunken")
title_close.place(x= 310, y= 615)
title_close.bind("<Button-1>", quitter)

title = Label(main,
    text= "TASK MANAGER",
    bg= '#101010',
    fg= "white",
    font= ("Tandelle 35"))
title.place(x= 80, y= 0)
title.bind("<B1-Motion>", move_app)

addframe = tk.Frame(
    main,
    bg= '#eeeeee'
)
addframe.place(x= 10, y=80, width=218, height= 28)

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
    bg= '#101010',
    fg='white',
    relief= 'sunken',
    font= ('Tandelle', 25),
    activebackground= '#091835',
    activeforeground= 'red',
    bd=0,
)
addbtn.place(x= 242, y=80, width=80, height= 27 )
# addbtn.pack(padx= 100,ipadx= 20, ipady= 5)

tk.Label(
    main,
    text="You Have to do",
    font=('DejaVu Serif', 13),
    bg='#101010',
    fg='white'
).place(x=80,y=125)

tk.Label(
    main,
    text="You Did",
    font=('DejaVu Serif', 13),
    bg='#101010',
    fg='white'
).place(x=120, y=368)

# tk.Label(main, text="Position 1 : x=0, y=0", bg="black", fg="white").place(x=5, y=10)

taskframe = tk.Frame(
    main,
    bg='#101010',
)
taskframe.place(x= 10, y = 170, width= 300, height=182)

scrollbar = Scrollbar(taskframe)
scrollbar.pack(side= RIGHT, fill= Y)

listbox = Listbox(
    taskframe,
    font='Verdana 18',
    bg='#101010',
    fg='white',
    selectbackground= 'red',

)
listbox.pack(fill= BOTH, expand= 300)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

listbox.bind("<Double-Button-1>", deletetask)
listbox.bind("<Delete>", deletetask)
listbox.config(font="{Outfit} 15 normal ")

taskframe2 = tk.Frame(
    main,
    bg='#101010',
)
taskframe2.place(x= 10, y = 410, width= 300, height=182)

scrollbar2 = Scrollbar(taskframe2)
scrollbar2.pack(side= RIGHT, fill= Y)

listbox2 = Listbox(
    taskframe2,
    font='Verdana 18',
    bg='#101010',
    fg='white',
    selectbackground= '#3EC129',

)
listbox2.pack(fill= BOTH, expand= 300)

listbox2.config(yscrollcommand=scrollbar2.set)
scrollbar2.config(command=listbox2.yview)
listbox2.config(font="{Outfit} 15 normal ")

listbox2.bind("<Double-Button-3>", remove)
listbox2.bind("<Delete>", remove)


tk.Label(
    main,
    text= "Double click to delete a task",
    bg= '#101010',
    fg= 'white',
    font=("Arial 10")
).pack(side= BOTTOM)

populate()
Bin()
main.mainloop()