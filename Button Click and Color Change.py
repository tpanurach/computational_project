import tkinter as tk
import pandas as pd
import math 
import array as ar 


linearity = True #global linearity variable 


tables = pd.read_csv(r"C:\Users\itzju\OneDrive\Desktop\python things\Maverik Compiled Dataset.csv") #reads csv, may have to change paths on different machines

#period dictionary 
periods = {"1": {1,2},"2": {3,4,5,6,7,8,9,10}, "3": {11,12,13,14,15,16,17,18}, "4": {19,20,21,22,23,24,25,26,27,28,29,30,31, 32,33,34,35,36},
           "5": {37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54},"6": {85, 86,55,56,57,72,73,74,75,76,77,78,79,80,81,82,83,84},
           "7": {87,88,89,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119},
           "Actinides": {90,91,92,93,94,95,96,97,98,99,100,101,102,103},
           "Lanthinides":{58,59,60,61,62,63,64,65,66,67,68,69,70,71}}

#group dictionary 
groups = {"1A":{1,3,11,19,37,87},"2A":{2,4,12,20,38,88}, "1B":{21,39,57,89}, "2B":{22,40,72,104,58,90},
          "3B":{23,41,73,105,59,91}, "4B":{24,42,74,106,60,92}, "5B":{25,43,75,107,61,93}, "6B":{26,44,76,108,62,94},
          "7B":{27,45,77,109,63,95}, "8B":{28,46,78,110,64,96}, "9B":{29,47,79,111,65,97}, "10B":{30,48,80,112,66,98},
          "3A":{5,13,31,49,81,113,67,99}, "4A":{6,14,32,50,82,114,68,100}, "5A":{7,15,33,51,83,115,69,101},
          "6A":{8,16,34,52,84,116,70,102}, "7A":{9,17,35,53,85,117,71,103}, "8A":{2,10,18,36,54,86,118}}

#sorts periods by atomic number 
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

# finds maximum data point 
    
#labels the different cells on teh combined dataset for easy indexing 
info = {"jaea" : 3,
        "icse": 4,
        "all": 5  }

#finds the maximum value in a dataset for projection normalization 
def findmax (data):
    xval = 1 #placeholder value 
    for i in range (1,118): # checks all known elements ( there are some acids under so couldn't use the entire csv)
          check = float(tables.iloc[i, info[data]])#changes temp value
          if check > xval: #compares
            xval = check #converts if bigger
    return xval 


#determines the color of the cell to project on screen in rgb( it was the easiest to do- im sorry)
def colorchoice(val, val2):
         #checks if the amount of data is not 0, if not, it will find the color to represent it as 
         if int(tables.iloc[val, info[val2]]) != 0:
           
           #checks whcih normailzation you want to use for the data, linear or exponential ( can be toggled when run)
           # a failsafe for if the max value is equal to 0 needs to be added so that division by 0 cannot occour
           #  ( maybe edge case is covered by my 0 check already, not too sure on the logic here)
           if linearity == False:
            xval =  float(math.exp(float(tables.iloc[val, info[val2]])/findmax(val2)-1)) #exponential math, float to reduce compression  
           else:
            xval = float(float(tables.iloc[val, info[val2]])/findmax(val2)) #linear math, float to reduce compression

           yval = int(xval*255)# converts back to int for rgb conversion

           # returns rgb value 
           return color(125,yval,0)
         
         # if there is 0 data on th eelement it will be printed as grey
         else: 
            return color(128,128,128)# calls function to convert to hexcode, and returns the hexcode color



#converts the rgb value into a hexcode, because tkinter only accepts hexcode for some reason       
def color(x, y, z):
    return "#{:02x}{:02x}{:02x}".format(x,y,z)


 #function to change the math behing the color selection (one is linear, other is exponential)   
def changelinearity():
      global linearity 
      linearity = not linearity  

#class for printing of buttons to scree, not too sure how it works, majorly based off kavon's code 
class App(tk.Frame):
    #initialization of the chart that the vaules will be printed on
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        tk.Frame.__init__(self, parent, *args)
        self.grid()
        self.infoLine = tk.Label(self, text="", justify='left')
        self.infoLine.grid(row=1, column=3, columnspan=10, rowspan=4)
        self.winfo_toplevel().title("Periodic Table of the Elements")
        self.topLabel = tk.Label(self, text=" ", font=20)
        self.topLabel.grid(row=0, column=0, columnspan=19)

# initial buttons to decide which data set to present on scree, made so that the data set visual can be switched at any time 
    def create_buttons(self):
        thing = 0
        if linearity:
              thing = 1
        tk.Button(self, text="jaea", width=5, height=2, bg = color(125,0,0),
                  command=lambda: self.charting("jaea")).grid(row=0, column=1)
        
        tk.Button(self, text="icse", width=5, height=2, bg = color(0,125,0),
                  command=lambda: self.charting("icse")).grid(row=0, column=2)
        
        tk.Button(self, text="all", width=5, height=2, bg= color(0,0,125),
                  command=lambda: self.charting("all")).grid(row=0, column=3)
        tk.Button(self, text = "linearity", width = 5, height =2, bg = color(125,125,125), 
                  command = lambda: changelinearity()).grid(row = 0, column= 4)
        
# when given a data set to work with, this function is called to chart all the elements data        
    def charting(self, val):
        for i in range (1,118): #loops through the atomic numbers of every element
            tk.Button (self, text = tables.iloc[i, 0], width=5, height=2, bg = colorchoice(i,val), command =lambda v= i: self.name(v) & self.info(v, val)).grid(row= period(i), column= group(i)-1)    

     # Replaces Label at the top with the name of whichever element tk.Button was pressed
    def name(self, val): 
        t = tables.iloc[val, 2]
        self.topLabel.config(text= t)

    # Displays the amount of data on the element of whichever element tk.Button was pressed
    def info(self, val, val2): 
        t = tables.iloc[val, info[val2]]
        self.infoLine.config(text= t + " data points")

# runs the tk class idk how this works 
root = tk.Tk()
a = App(root)
a.grid(row=0, column=0, sticky='nsew') 

#runs the 3 intialization buttons to choos dataset 
a.create_buttons()

#dont know what this does 
a.mainloop()

