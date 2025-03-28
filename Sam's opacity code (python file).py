import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math
import mplcursors as cur
import pyautogui
import time
import tkinter as tk 
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QDialog, QDialogButtonBox

      
# reading dataset, you will probably have to change the path
tables = pd.read_csv(r"C:\Users\itzju\OneDrive\Desktop\python things\Maverik Compiled Dataset.csv")

#converting dataset to 2D array
info = []
for row in tables:
     info.append(tables[row])

#sets up periodic table plot values such as range and domain
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, 23)
ax.set_ylim(0, 11)
ax.set_xticks(range(1, 23))
ax.set_yticks(range(1, 11))
ax.set_xticklabels(range(1, 23))
ax.set_yticklabels(range(1, 11))
ax.grid(False)

# dictionary for the period definitions
periods = {"1": {1,2},
           "2": {3,4,5,6,7,8,9,10},
           "3": {11,12,13,14,15,16,17,18},
           "4": {19,20,21,22,23,24,25,26,27,28,29,30,31, 32,33,34,35,36},
           "5": {37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54},
           "6": {85, 86,55,56,57,72,73,74,75,76,77,78,79,80,81,82,83,84},
           "7": {87,88,89,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119},
           "Actinides": {90,91,92,93,94,95,96,97,98,99,100,101,102,103},
           "Lanthinides":{58,59,60,61,62,63,64,65,66,67,68,69,70,71}}

#dictionary for the group definitions
groups = {"1A":{1,3,11,19,37,87}, 
          "2A":{2,4,12,20,38,88},
          "1B":{21,39,57,89},
          "2B":{22,40,72,104,58,90},
          "3B":{23,41,73,105,59,91},
          "4B":{24,42,74,106,60,92},
          "5B":{25,43,75,107,61,93},
          "6B":{26,44,76,108,62,94},
          "7B":{27,45,77,109,63,95},
          "8B":{28,46,78,110,64,96},
          "9B":{29,47,79,111,65,97},
          "10B":{30,48,80,112,66,98},
          "3A":{5,13,31,49,81,113,67,99},
          "4A":{6,14,32,50,82,114,68,100},
          "5A":{7,15,33,51,83,115,69,101},
          "6A":{8,16,34,52,84,116,70,102},
          "7A":{9,17,35,53,85,117,71,103},
          "8A":{2,10,18,36,54,86,118}}

#I dont know what this does, but when i remove it the code breaks
text = [119]

#sort period by atomic number
def period(value):
       if value in periods["1"]:
              return 1
       elif value in periods["2"]:
              return 2
       elif value in periods["3"]:
              return 3
       elif value in periods["4"]:
              return 4
       elif value in periods["5"]:
              return 5
       elif value in periods["6"]:
              return 6
       elif value in periods["7"]:
              return 7
       elif value in periods["Lanthinides"]:
              return 9
       else:
             return 10

#sorts group by atomic number
def group(value):
        if value in groups["1A"]: 
                return 1 
        elif value in groups["2A"]:
              return 2
        elif value in groups["3A"]: 
                return 13
        elif value in groups["4A"]:
              return 14
        elif value in groups["5A"]: 
                return 15
        elif value in groups["6A"]:
              return 16 
        elif value in groups["7A"]:
              return 17
        elif value in groups["8A"]: 
                return 18
        elif value in groups["1B"]:
              return 3
        elif value in groups["2B"]: 
                return 4
        elif value in groups["3B"]:
              return 5
        elif value in groups["4B"]:
              return 6
        elif value in groups["5B"]: 
                return 7
        elif value in groups["6B"]:
              return 8
        elif value in groups["7B"]: 
                return 9
        elif value in groups["8B"]:
              return 10
        elif value in groups["9B"]:
              return 11
        elif value in groups["10B"]:
              return 12
        elif value < 72:
                return value - 54
        else: 
              return value - 86
        

max = 0
print (info[3][1])
# sorting for maximum value in the dataset 
for i in range (0,118):
    x = int(info[4][i])
    if x > max:
     max = x

scatter =[]

#defines list that can be accessed for other uses 
rect = [119]

#unit test
print(max)
for i in range (0,118):
    x = group(int(info[1][i]))
    y = period(int(info[1][i]))

    # exponential graph representation {
    # if int(info[4][i]) > 0:
    #       val = math.exp(int(info[4][i])/max-1)
    #       color = (1,val,0,1)
    # else: 
    #       color = (0.5,0.5,0.5,1)
    # }

    #linear data to color representation 
    color = (1,0,0,int(info[3][i]/max))

    rect.append(patches.Rectangle((x - 0.5, y - 0.5), 1, 1, linewidth=1, edgecolor="black", facecolor=color))
    ax.add_patch(rect[i+1])
    ax.text(x, y, f"{info[1][i]}\n{info[0][i]}", ha="center", va="center", fontsize=8)




#prints the chart
plt.gca().invert_yaxis()
plt.show()



# stuff I was testing for buttons and hover control 


#class MyPopup(QWidget):
        #def __init__(self):
         #   super().__init__()
          #  self.setWindowTitle("My Popup")
           # layout = QVBoxLayout()
          #  label = QLabel("")
          #  button = QPushButton("Close")
          #  button.clicked.connect(self.close)
          #  layout.addWidget(label)
          #  layout.addWidget(button)
          #  self.setLayout(layout)


#popup = MyPopup()    
           
#popup.show()

#self.popup = MyPopup()
#self.popup.show()



#class MyModalPopup(QDialog):
#def __init__(self):
#super().__init__()
#self.setWindowTitle("My Modal Popup")
      #      layout = QVBoxLayout()
      #      label = QLabel("This is a modal popup window.")
      #      button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
      #      button_box.accepted.connect(self.accept)
      ##      button_box.rejected.connect(self.reject)
       #     layout.addWidget(label)
       #     layout.addWidget(button_box)
       #     self.setLayout(layout)

#popup = MyModalPopup()
#result = popup.exec_()
#if result == QDialog.Accepted:
        # User clicked OK
#pass
#else:
        # User clicked Cancel or closed the dialog
#pass
# Get the current position of the mouse cursor


# Print the coordinates
#print(f"The current cursor position is: x={xval}, y={yval}")

