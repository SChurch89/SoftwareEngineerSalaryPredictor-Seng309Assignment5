#Stephanie Church
#Assignment 5
#SENG 309

import numpy as np
import pickle
from tkinter import *
from tkinter import Button

root = Tk()
root.title("Software Developer Salary Predictions")
root.geometry("500x500")


#from sklearn.externals
import joblib

# Load our trained model
model = joblib.load('SD_Salary.pkl')

#options = ["United States", "India", "United Kingdom", "Germany", "Canada", "Brazil", "France", "Spain", "Australia", "Netherlands", "Poland", "Italy", "Russian Federation", "Sweden",]
#options2 = ["Less than a Bachelors", "Bachelor’s degree", "Master’s degree", "Post grad"]

# Define the house that we want to value (with the values in the same order as in the training data)
SD_1 = [
    1,  # Country
    4,  # Ed Level
    20,  # Number years coding
]

# scikit-learn assumes you want to predict the values for multiple of houses at once, so it expects an array.
# We only want to estimate the value of a single house, so there will only be one item in our array.
SD = [SD_1]
# Make a prediction for each house in the homes array (we only have one)
#home_values = model.predict(homes)
# Since we are only predicting the price of one house, grab the first prediction
#returned
#predicted_value = home_values[0]
# Make a prediction for each house in the homes array (we only have one)
SD_values = model.predict(SD)

# Since we are only predicting the price of one house, grab the first prediction returned
predicted_value = SD_values[0]

def print_predict():
    print("Software Developer:")
    print(f"Estimated Salary is: ${predicted_value:,.2f}")
# Print the results



myLabel = Label(root, text="What country do you live in?", )
myLabel.pack()

def show():
    label.config(text=clicked.get())
# Dropdown menu options
options = {
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
}
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
clicked.set("Less than a Bachelors")

# Create Dropdown menu
drop = OptionMenu(root, clicked, *options2)
drop.pack()

# Create button, it will change label text
button = Button(root, text="click Me", command=show).pack()

# Create Label
label = Label(root, text=" ")
label.pack()



myLabel = Label(root, text="How many years coding expirence do you have?", )
myLabel.pack()

horizontal = Scale(root, from_=1, to=50, orient=HORIZONTAL)
horizontal.pack()
#Years of coding
My_label = Label(root, text=horizontal.get()).pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(stir(horizontal.get())+ "x500")


myButton = Button(root, text="Predict", command=print_predict)
myButton.pack()

root.mainloop()

#from sklearn.externals
import joblib

# Load our trained model
model = joblib.load('SD_Salary.pkl')

# Define the house that we want to value (with the values in the same order as in the training data)
SD_1 = [
    7,  # Country
    2,  # Ed Level
    5,  # Number years coding
]

# scikit-learn assumes you want to predict the values for multiple of houses at once, so it expects an array.
# We only want to estimate the value of a single house, so there will only be one item in our array.
SD = [SD_1]
# Make a prediction for each house in the homes array (we only have one)
#home_values = model.predict(homes)
# Since we are only predicting the price of one house, grab the first prediction
#returned
#predicted_value = home_values[0]
# Make a prediction for each house in the homes array (we only have one)
SD_values = model.predict(SD)

# Since we are only predicting the price of one house, grab the first prediction returned
predicted_value = SD_values[0]

def print_predict():
    print("Software Developer:")
    print(f"Estimated Salary is: ${predicted_value:,.2f}")

