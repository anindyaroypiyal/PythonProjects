from tkinter import *
import tkinter as ui
import time

def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_pm = time.strftime("%p")
    current_time = hours + ' : ' + minutes + ' : ' + seconds + ' ' + am_pm
    digi_clck_lbl.config(text=current_time)
    digi_clck_lbl.after(1000, update_clock)

window = ui.Tk()
window.geometry('330x135+1590+0')
window.title("My Digital Clock")

#remove title bar
window.overrideredirect(True)

def move_app(e):
    window.geometry(f'+{e.x_root}+{e.y_root}')
def quitter(e):
    window.quit()

#create fake title bar
title_bar = Frame(window, bg='#101010', relief='raised', bd=0)
title_bar.pack(expand=1, fill=X)

#Bind the titlebar
title_bar.bind("<B1-Motion>", move_app)
title_label = Label(title_bar, text="  It's Never too Late", bg='#101010', fg= 'white')
title_label.pack(side=LEFT, pady=3.3, padx=30)
title_close = Label(title_bar, text="❖ ", bg= '#31060f', fg= 'red', bd=0, relief= "sunken")
title_close.pack(side=RIGHT)
title_close.bind("<Button-1>", quitter)

# my_button = Button(window, command= window.quit, text= "CLOSE !", font=("helvetica", 10))
# my_button.pack(pady=5)

digi_clck_lbl = ui.Label(window, text="00:00:00", font="{tandelle} 60 normal", bg='#101010',  fg= 'white', bd=40)

digi_clck_lbl.pack(anchor='center')

update_clock()

window.mainloop()