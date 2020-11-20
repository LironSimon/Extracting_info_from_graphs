{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# importing all neccery libreries\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from PIL import Image\n",
    "import tkinter\n",
    "from tkinter import simpledialog\n",
    "root = tkinter.Tk()\n",
    "root.withdraw() # preving root window from opening"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def tellme(s):\n",
    "    print(s)\n",
    "    plt.title(s, fontsize=16)\n",
    "    plt.draw()\n",
    "\n",
    "def pic2data(source):\n",
    "    \"\"\" GUI to get data from an XY graph image. The graph\n",
    "        is provided in 'source' as a path. Graph is\n",
    "        considered rectangular and parrallel to the edges\n",
    "        of the picture.\n",
    "    \"\"\"\n",
    "    image = Image.open(source)\n",
    "    origin = 'lower'\n",
    "\n",
    "    ###### DISPLAY THE IMAGE ######\n",
    "    plt.ion()  # interactive mode\n",
    "    fig, ax = plt.subplots(1)\n",
    "    imgplot = ax.imshow(image, origin=origin)\n",
    "    fig.canvas.draw()\n",
    "    plt.draw()\n",
    "\n",
    "    ##### PROMPT THE AXES ########\n",
    "    def promptPoint(text=None):\n",
    "        if text is not None: tellme(text)\n",
    "        return np.array(plt.ginput(1, timeout=-1)[0])\n",
    "\n",
    "    def askValue(text='', initialvalue=0.0):\n",
    "        return tkinter.simpledialog.askfloat(text,'Value:',initialvalue=initialvalue)\n",
    "\n",
    "    origin = promptPoint('Place the origin of the graph')\n",
    "    origin_value = askValue('X coordinate of origin:', 0), askValue('Y coordinate of origin:', 0)\n",
    "    Xref = promptPoint('Place a point you know on X [i.e (x_i, 0)]')\n",
    "    Xref_value = askValue('X reference', 1.0)\n",
    "    Yref = promptPoint('Place a point you know on Y [i.e (0, y_i)]')\n",
    "    Yref_value = askValue('Y reference', 1.0)\n",
    "    Xref[1] = origin[1]  # to make sure Xref is a pt of (x_i, 0)\n",
    "    Yref[0] = origin[0]  # to make sure Yref is a pt of (0, y_i)\n",
    "\n",
    "    ##### PROMPT THE POINTS #######\n",
    "    selected_points = []\n",
    "    tellme(\"\\nSelect your points!\")\n",
    "    print(\"   Right-click or press 's' to select\")\n",
    "    print(\"   Left-click or press 'del' to deselect\")\n",
    "    print(\"   Middle-click or press 'Enter' to confirm\")\n",
    "    print(\"   Note that the keyboard may not work.\")\n",
    "    selected_points = plt.ginput(-1, timeout=-1)\n",
    "\n",
    "    ##### RETURN THE POINTS COORDINATES ######\n",
    "    # compute the coordinates of the points in the user-defined system\n",
    "    OXref = Xref - origin\n",
    "    OYref = Yref - origin\n",
    "    xScale = (Xref_value - origin_value[0]) / np.linalg.norm(OXref)\n",
    "    yScale = (Yref_value - origin_value[1]) / np.linalg.norm(OYref)\n",
    "    ux = OXref / np.linalg.norm(OXref)\n",
    "    uy = OYref / np.linalg.norm(OYref)\n",
    "\n",
    "    result = [(ux.dot(pt - origin) * xScale + origin_value[0],\n",
    "               uy.dot(pt - origin) * yScale + origin_value[1])\n",
    "              for pt in selected_points]\n",
    "    \n",
    "    return result"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}