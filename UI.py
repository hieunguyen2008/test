import time

print("Python UI")

import tkinter as tk
from tkinter import *

window = tk.Tk()
window.attributes('-fullscreen', False)
window.title("IOT Project")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print("Size:", screen_width, screen_height)

labelAMONIAText = tk.Label(text="NH3",font="Helvetica 60 bold",fg="#000000",justify=CENTER)
labelAMONIAValue = tk.Label(text="5.12",fg="#0000ff",justify=CENTER,font="Helvetica 60 bold")
labelAMONIAValue.place(x=100, y=200, width=screen_width / 3, height=100)
labelAMONIAText.place(x=100, y=100, width=screen_width / 3, height=100)

labelTDSValue = tk.Label(text="20",fg="#0000ff",justify=CENTER,font="Helvetica 60 bold")
labelTDSText = tk.Label(text="TDS",font="Helvetica 60 bold",fg="#000000",justify=CENTER)
labelTDSValue.place(x=420, y=200, width=screen_width / 3, height=100)
labelTDSText.place(x=420, y=100, width=screen_width / 3, height=100)

labelPHText = tk.Label(text="PH",font="Helvetica 60 bold",fg="#000000",justify=CENTER)
labelPHValue = tk.Label(text="7.11",fg="#0000ff",justify=CENTER,font="Helvetica 60 bold")
labelPHValue.place(x=800, y=200, width=screen_width / 3, height=100)
labelPHText.place(x=800, y=100, width=screen_width / 3, height=100)

buttonOn= tk.Button(text="On", fg="#00FF00", justify=CENTER, bg="#FFF", font="Helvetica 60 bold")
buttonOn.place(x=200, y=400, width=350, height=100)

buttonOff= tk.Button(text="Off", fg="#FF0000", justify=CENTER, bg="#FFF", font="Helvetica 60 bold")
buttonOff.place(x=700, y=400, width=350, height=100)

# def nut_nhan1():
# 	print("On")

# def nut_nhan2():
# 	print("Off")


# buttonOn.config(command = nut_nhan1)
# buttonOff.config(command = nut_nhan2)