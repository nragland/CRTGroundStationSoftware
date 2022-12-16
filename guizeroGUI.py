"""
Ground Station GUI (guizero Version)

This code constructs and runs the Ground Station GUI intended for a Raspberry
Pi 4 and a touchscreen display.

The GUI displays data received over serial onto the touchscreen display and
allows users to interact with its interface.

22 September 2022
"""

import guizero
from guizero import *

app = App(title = "Ground Station", bg = "black")

w = app.tk.winfo_screenwidth()
h = app.tk.winfo_screenheight()

# Title initialization
title_box = Box(app, width = "fill", align = "top", border = True)
title_box.bg = "#142C2E"
title_box.set_border(3, "#52C6D0")
Text(title_box, text="CRT Ground Station", size = 18)
title_box.text_color = "white"

# map button action function
def map_app_start():
    print("Map start successful")

# alt button action function
def alt_app_start():
    print("Alt Graph start successful")

"""
map_box = Box(app, height = "fill", width = "fill", align = "left", border = True)
Text(map_box, text = "Map", align = "top", size = 14, color = "white")

map_button_box = Box(map_box, width = "fill", align = "left", border = False)

# button action function
def map_app_start():
    print("Map start successful")

map_button = PushButton(map_button_box, text = "Start Map", align = "top", command = map_app_start)
map_button.text_color = "white"

data_box = Box(app, layout = "grid", height = "fill", width = "fill", align = "right", border = True)
Text(data_box, text = "Data", grid = [6,0], size = 14, color = "white")

# find a more efficient way to do the following three boxes :((

alt_box = Box(data_box, grid = [0,12], height = h/4, width = "fill", align = "left", border = False)
Text(alt_box, text = "Altimeter: ", align = "left", color = "white")

acc_box = Box(data_box, grid = [0,24], width = "fill", align = "left", border = False)
Text(acc_box, text = "Accelerometer: ", align = "left", color = "white")

gyr_box = Box(data_box, grid = [0,36], width = "fill", align = "left", border = False)
Text(gyr_box, text = "Gyroscope: ", align = "left", color = "white")

"""

# trying smt sketchy
panel_box = Box(app, layout = "grid", width = "fill", height = "fill", align = "bottom", border = False)
panel_box.set_border(1,"red")

map_box = Box(panel_box, grid = [0,0], height = "fill", width = "fill", align = "left", border = True)
Text(map_box, text = "Map", align = "top", size = 14, color = "white")
map_box.set_border(1,"white")
map_button_box = Box(map_box, width = "fill", align = "left", border = False)
map_button = PushButton(map_button_box, text = "Start Map", align = "top", command = map_app_start)
map_button.text_color = "white"

alt_box =  Box(panel_box, grid = [1,0], height = "fill", width = "fill", align = "right", border = True)
Text(alt_box, text = "Altimeter", align = "top", size = 14, color = "white")
alt_box.set_border(1,"white")
alt_button_box = Box(alt_box, width = "fill", align = "left", border = False)
alt_button = PushButton(alt_button_box, text = "Start Alt Graph", align = "top", command = alt_app_start)
alt_button.text_color = "white"

message_box =  Box(panel_box, grid = [0,1], height = "fill", width = "fill", align = "right", border = True)
Text(message_box, text = "Messages", size = 14, color = "white")
message_box.set_border(1,"white")

data_box = Box(panel_box, grid = [1,1], height = "fill", width = "fill", align = "left", border = True)
Text(data_box, text = "Data", size = 14, color = "white")
data_box.set_border(1,"white")

app.display()
