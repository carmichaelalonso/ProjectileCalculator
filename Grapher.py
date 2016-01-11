"""

Grapher.py
Copyright Cameron Carmichael Alonso, 2016. All Rights Reserved.

"""

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from Tkinter import *

def PlotGraph(xValues, yValues):
    ## setup window
    root = Tk()
    root.wm_title("Graphed Projectile")

    ## setup frame
    frame = Frame(root)
    frame.pack()


    label = Label(root, text="Graph of Projectile", font=("Verdana", 12))
    label.pack(pady=10,padx=10)

    f = Figure(figsize=(5,5), dpi=100)
    a = f.add_subplot(111)
    a.plot(xValues,yValues)

    canvas = FigureCanvasTkAgg(f, root)
    canvas.show()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

    toolbar = NavigationToolbar2TkAgg(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

    root.mainloop()