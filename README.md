# Seng309Assignment5 - Salary Prediction Machine Learning App

## Introduction

Welcome to the Seng309Assignment5 repository! This project is a machine learning application designed to predict the salary of software developers based on various factors including country, education level, and years of coding experience.

## Project Overview

### A. Idea and Objective

The primary goal of this project is to build a predictive model for software developer salaries. The model takes into account key variables such as country, education level, and years of coding experience to estimate a developer's potential salary.

### B. Data Source and Preprocessing

The data used for this project was sourced from Stack Overflow's yearly Developer Survey. The original dataset contained 48 different columns, but for this project, we narrowed it down to 5 columns: Country, Education Level, Years of Professional Coding, Employment Status, and Salary.

The preprocessing steps included:
- Removing entries with null values, resulting in 47,183 valid entries.
- Keeping only data for full-time employed subjects, reducing entries to 40,399.
- Grouping countries with a small number of entries into an "Other" category, resulting in 25 named countries and an "Other" category.
- Cleaning Years of Coding and Education Level by addressing outliers and unique values.

To find the best parameters for machine learning algorithms, we used GridSearchCV with cross-validation.

### C. Technology and Implementation

This project was implemented using Python. The project initially attempted to use streamline.io for the user interface, but due to issues, we are now exploring using Tkinter for the interface implementation.

### D. Demo and Presentation

A demo of this project will be presented in class on 7/6. Alternatively, the demo might be uploaded to the class Teams platform for viewing.

### E. Machine Learning Algorithms and Results

Three machine learning algorithms were experimented with:
1. Linear Regression
2. Decision Tree Regression
3. Random Forest Regressor

The project's focus was to minimize prediction errors. The lowest error was achieved using the Decision Tree Regressor, with Linear Regression and Random Forest Regressor producing errors of $34,369.73 and $34,731.21, respectively.

## Current Challenges

The project is currently addressing challenges in the following areas:
- Saving inputs for the test model.
- Displaying the results on the application interface rather than the terminal.

Feel free to explore the code and documentation to gain a deeper understanding of this exciting journey into salary prediction using machine learning!

For any inquiries or feedback, please feel free to contact [Your Name] at [Your Email Address].

Thank you for your interest in this project! 🚀👩‍💻
