import math
import tkinter as ui
import time

def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    seconds_x = seconds_hand_length * math.sin ( math.radians ( seconds * 6 ) ) + center_x
    seconds_y = -1 * seconds_hand_length * math.cos ( math.radians ( seconds * 6 ) )+ center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    minutes_x = minute_hand_length * math.sin ( math.radians ( minutes * 6 ) ) + center_x
    minutes_y = -1 * minute_hand_length * math.cos ( math.radians ( minutes * 6 ) )+ center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    hours_x = hour_hand_length * math.sin ( math.radians ( hours * 30 ) ) + center_x
    hours_y = -1 *  hour_hand_length * math.cos ( math.radians ( hours * 30 ) )+ center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    window.after(1000, update_clock)

window = ui.Tk()

window.geometry("694x702")
window.title("Analog Clock")

canvas = ui.Canvas(window, width= 694, height= 702, bg= "black")
canvas.pack(expand=True, fill='both')

bg = ui.PhotoImage(file='watch dial.png')
canvas.create_image(347, 351, image=bg)

center_x = 347
center_y = 351
seconds_hand_length = 200
minute_hand_length = 175
hour_hand_length = 120

seconds_hand = canvas.create_line(center_x, center_y,
                                  center_x+seconds_hand_length, center_y+seconds_hand_length,
                                  width=1.6, fill='red')

minutes_hand = canvas.create_line(center_x, center_y,
                                  center_x+minute_hand_length, center_y+minute_hand_length,
                                  width=3.2, fill='teal')

hours_hand = canvas.create_line(center_x, center_y,
                                  center_x+hour_hand_length, center_y+hour_hand_length,
                                  width=8, fill='white')


update_clock()

window.mainloop()