import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tkinter
from tkinter import simpledialog
root = tkinter.Tk()
root.withdraw()

###################################################################################
####### Functions for extracting data from scatter graphs in jpg ##################
###################################################################################

def tellme(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw()

def pic2data(source):
    """ GUI to get data from a XY graph image. The graph
        is provided in 'source' as a path. Graph is
        considered rectangular and parrallel to the edges
        of the picture.
    """
    image = mpimg.imread(source)
    origin = 'lower'

    ###### DISPLAY THE IMAGE
    plt.ion()  # interactive mode !
    fig, ax = plt.subplots(1)
    imgplot = ax.imshow(image, origin=origin)
    fig.canvas.draw()
    plt.draw()

    ##### PROMPT THE AXES
    def promptPoint(text=None):
        if text is not None: tellme(text)
        return np.array(plt.ginput(1, timeout=-1)[0])

    def askValue(text='', initialvalue=0.0):
        return tkinter.simpledialog.askfloat(text,'Value:',initialvalue=initialvalue)

    origin = promptPoint('Place the origin of the graph')
    origin_value = askValue('X coordinate of origin:', 0), askValue('Y coordinate of origin:', 0)
    Xref = promptPoint('Place a point you know on X [i.e (x_i, 0)]')
    Xref_value = askValue('X reference', 1.0)
    Yref = promptPoint('Place a point you know on Y [i.e (0, y_i)]')
    Yref_value = askValue('Y reference', 1.0)
    Xref[1] = origin[1]
    Yref[0] = origin[0]

    ##### PROMPT THE POINTS
    selected_points = []
    tellme("\nSelect your points!")
    print("Right-click or press 's' to select")
    print("Left-click or press 'del' to deselect")
    print("Middle-click or press 'Enter' to confirm")
    print("Note that the keyboard may not work.")
    selected_points = plt.ginput(-1, timeout=-1)

    ##### RETURN THE POINTS COORDINATES
    # ~ selected_points.sort() # sorts the points in increasing x order
    # compute the coordinates of the points in the user-defined system
    OXref = Xref - origin
    OYref = Yref - origin
    xScale = (Xref_value - origin_value[0]) / np.linalg.norm(OXref)
    yScale = (Yref_value - origin_value[1]) / np.linalg.norm(OYref)
    ux = OXref / np.linalg.norm(OXref)
    uy = OYref / np.linalg.norm(OYref)

    result = [(ux.dot(pt - origin) * xScale + origin_value[0],
               uy.dot(pt - origin) * yScale + origin_value[1])
              for pt in selected_points]
    
    return result   #returns a list of tuples, representing each point selected on the graph
