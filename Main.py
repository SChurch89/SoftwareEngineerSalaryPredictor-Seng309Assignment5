#Stephanie Church
#Assignment 5
#SENG 309

import numpy as np
import pickle
from tkinter import *
from tkinter import Button

root = Tk()
root.title("Software Developer Salary Predictions")
root.geometry("800x800")



#def load_model():
 #   with open('saved_steps.pkl', 'rb') as file:
  #      data = pickle.load(file)
   # return data

#data = load_model()

#regressor = data["model"]
#le_country = data["le_country"]
#le_education = data["le_education"]


#def Predict():
    ########salasry prediction

myButton = Button(root, text="Predict") ##command=Predict#)
myButton.pack()

myLabel = Label(root, text="How many years coding expirence do you have?", )
myLabel.pack()

horizontal = Scale(root, from_=1, to=50, orient=HORIZONTAL)
horizontal.pack()
#Years of coding
My_label = Label(root, text=horizontal.get()).pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(stir(horizontal.get())+ "x500")


myLabel = Label(root, text="What is your educational background?", )
myLabel.pack()




def show():
    label.config(text=clicked.get())


# Dropdown menu options
options2 = [
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("United States")

# Create Dropdown menu
drop = OptionMenu(root, clicked, *options2)
drop.pack()

# Create button, it will change label text
button = Button(root, text="click Me", command=show).pack()

# Create Label
label = Label(root, text=" ")
label.pack()



myLabel = Label(root, text="What country do you live in?", )
myLabel.pack()


def show():
    label.config(text=clicked.get())


# Dropdown menu options
options = [
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("United States")

# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.pack()

# Create button, it will change label text
button = Button(root, text="click Me", command=show).pack()

# Create Label
label = Label(root, text=" ")
label.pack()


root.mainloop()


