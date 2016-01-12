"""

Interface.py
Copyright Cameron Carmichael Alonso, 2016. All Rights Reserved.

"""

from Tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkintertable import TableCanvas, TableModel
import matplotlib

matplotlib.use("TkAgg")

def PlotGraph(xValues, yValues, labelString):
    ## setup window
    root = Tk()
    root.wm_title("Graphed Projectile")

    ## setup frame
    frame = Frame(root)
    frame.pack()


    label = Label(root, text=labelString, font=("Verdana", 12))
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

    DataGrid()

    root.mainloop()

def DataGrid():
    ## setup window
    dataGrid = Tk()
    dataGrid.wm_title("Data")

    ## setup frame
    frame = Frame(dataGrid)
    frame.pack()

    label = Label(dataGrid, text="DataGrid", font=("Verdana", 12))
    label.pack(pady=10,padx=10)

    table = TableCanvas(frame)
    table.createTableFrame()

    model = TableModel()
    table = TableCanvas(frame, model=model)

    ## sample data
    sDict = {'rec1': {'col1': 99.88, 'col2': 108.79, 'label': 'rec1'},'rec2': {'col1': 99.88, 'col2': 108.79, 'label': 'rec2'},} 
    model.importDict(sDict)
    #table.redrawTable()

    dataGrid.mainloop()
