"""
igoerjlkdfm,
"""

"""
Ground Station GUI (Tkinter Version)

This code constructs and runs the Ground Station GUI intended for a laptop.

The GUI displays data received over serial onto the display and allows users
to interact with its interface.

27 October 2022
"""

import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from AltDisplay import AltGraph

class GroundStationGUI():

    def __init__(self):
        self.app = Tk()
        self.app.title("CRT Ground Station")
        self.w = self.app.winfo_screenwidth()
        self.h = self.app.winfo_screenheight()

        self.f0 = Frame(master = self.app, width = self.w, height = self.h*0.05, bg = "#142C2E")
        self.f0.pack(fill = tk.BOTH, side = tk.TOP, expand = False)
        self.title = Label(master = self.f0, text = "CRT Ground Station", bg = "#142C2E", fg = "white", font = ('Helvetica', 14))
        self.title.pack(fill = tk.BOTH, side = tk.TOP, expand = True)

        self.f1 = Frame(master = self.app, width = self.w, height = self.h, bg = "black")
        self.f1.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

        self.f2 = Frame(master = self.app, width = self.w, height = self.h, bg = "black")
        self.f2.pack(fill = tk.BOTH, side = tk.RIGHT, expand = True)

        # initialize four panels
        self.map = self.panel(self.f1, self.h*0.67, "GPS")
        self.data = self.panel(self.f1, self.h*0.33, "Data Stream")
        self.alt = self.panel(self.f2, self.h*0.67, "Altimeter")
        #self.createAltGraph()
        self.msg = self.panel(self.f2, self.h*0.33, "Messages")

        self.app.mainloop()

    def panel(self, f, h, header):
        p = Frame(master = f, height = h, bg = "black", highlightbackground="#52C6D0", highlightthickness=2)
        p.pack(fill = tk.BOTH, expand = True)
        p_title = Label(master = p, text = header, bg = "black", fg = "white", font = ('Helvetica', 14))
        p_title.pack(fill = tk.X, expand = True)

    def createAltGraph(self):
        canvas = FigureCanvasTkAgg(fig = AltGraph(), master = self.alt)
        canvas.draw()
        canvas.get_tk_widget().pack(side = tkinter.TOP, fill = tkinter.BOTH, expand = True)

gsg = GroundStationGUI()
