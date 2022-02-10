# BIG-M PYTHON INTERFACE

## Introduction

This project was initially made in my Optimisation lessons.
It is aiming to implement the big-M method in Python, with an easy to use interface.
There are also three presets available, extracted from an evaluation.
This project should be able to solve any problem with N variables and M constrincts.


## 1. The structure

This project is relying on two Python files : _bigM.py_ and _simplex_widgets.py_.

##  2. The files     

1. bigM.py

This first file implements the big-M method in Python.
The table in each iteration of the process, and the final result are diplayed on the console.
This uses the pandas library, to help displaying each table.

2. _simplex_widgets.py_

This second files generates an interface for the user, and uses the first file to solve the system.
The interface was made using the PyQt5 library.
It also contains the presets used to answer the 3 questions of the evaluation, you can run them as some examples.

## 3. The windows

1. Home

In this window, you have two choices :
* "Manual input" : to solve your own systems
* "Use presets"	: to select the 3 examples  

Press "Begin" to select your choice.

2. Parameters

Opened when "Manual input" is previously selected.
In this window, you have three parameters to choose :
* Whether you want to maximize or minimize a function
* The numer of variables (must be an integer)
* The number of constrincts (must be an integer)
Press "Continue" to validate your parameters.

3. Presets

Opened when "Use presets" is selected in the "Home" window.
In this window you can choose between the 3 examples.  
Press "Continue" to validate your choice

4. The initial table

Opened whenever "Continue" is pressed.  
In the first row, you can select the coefficients of each variables in the function.  
The M following rows represent the contrincts you want to add.  
You can choose between three comparisons : <= | = | >=.  
Press "Compute" to solve your system, and see each results on the console.


## 4. Run the project

To run the project you only need :
* Python 3
* A Python IDE
* _pandas_ and _PyQt5_ libraries  

Then you just have to run "simplex_widgets.py".