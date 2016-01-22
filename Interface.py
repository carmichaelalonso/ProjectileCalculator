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

    DataGrid(xValues, yValues)

    root.mainloop()

def DataGrid(xValues, yValues):
    ## setup window
    dataGrid = Tk()
    dataGrid.wm_title("Data")

    ## setup frame
    frame = Frame(dataGrid)
    frame.pack()

    label = Label(dataGrid, text=("Showing %.0f data points" % len(xValues)), font=("Verdana", 12))
    label.pack(pady=5,padx=10)

    dataDict = {}

    ## iterate through time
    for i in range(0, len(xValues)):
        xVal = ("%.2f" % float(xValues[i]))
        yVal = ("%.2f" % float(yValues[i]))
        dataDict[xVal] = {"Time (s)":xVal, "Height (m)":yVal}


    model = TableModel()
    model.importDict(dataDict)
    model.moveColumn(model.getColumnIndex('Time (s)'), 0)

    table = TableCanvas(frame, model=model,editable=False)
    table.createTableFrame()

    ## order by time
    table.sortTable(columnName='Time (s)')

    dataGrid.mainloop()
