from tkinter import *
from PIL import ImageTk, Image
import time
import pygame as pg
import threading

pg.mixer.init()

root = Tk()
root.title("Digital Alarm Clock Of 24 Hour")
root.geometry("500x500")

alarmtime = StringVar()
alarm_on = False  # Flag to indicate if the alarm is set

def alarm():
    global alarm_on
    Alarm = alarmtime.get()
    AlarmT = Alarm

    def check_alarm():
        global alarm_on
        while alarm_on:
            CurrentTime = time.strftime("%H:%M")
            if AlarmT == CurrentTime:
                pg.mixer.music.load('GUITAR.WAV')
                pg.mixer.music.play()
                alarm_on = False  # Turn off the alarm once triggered
                break

    alarm_on = True
    alarm_thread = threading.Thread(target=check_alarm)
    alarm_thread.start()

def stop():
    global alarm_on
    pg.mixer.music.stop()
    alarm_on = False

frame = Frame(root, width=60, height=40)
frame.place(x=100,y=80)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("images.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

Label(root,text="Digital Alarm Clock",font="Times 24 bold").place(x=100,y=30)

Label(root,text="Enter Time : ",font="Times 18 ").place(x=80,y=300)
Entry(root,textvariable=alarmtime,width=18).place(x=250,y=310)


Button(root,text="Set Alarm",font="Times 18 bold",command=alarm).place(x=250,y=360)
Button(root,text="Ok",font="Times 18 bold",command=stop).place(x=100,y=360)

Label(root,text="Click Ok To Stop Alarm",font="Times 14 ").place(x=80,y=420)

root.mainloop()
