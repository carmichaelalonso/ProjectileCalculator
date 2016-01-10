"""

Grapher.py
Copyright Cameron Carmichael Alonso, 2016. All Rights Reserved.

"""

#import matplotlib
#matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure

from Tkinter import *

root = Tk()
root.wm_title("Graphed Projectile")

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

root.mainloop()