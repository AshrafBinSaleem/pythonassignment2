# Visualisation code template for FIT9136 Assignment 2.
# Instructions to students:
# 1. Implement task 3 within this file as a working program. You may define
#   as many functions or classes as you require to complete this task, if needed.
#   You may also import any libraries allowed by the assignment specification.
# 2. Modify the filename (and import statement(s) where required) to replace
#   the xxxxxxxx with your student ID number.
# 3. Complete tasks 1 and 2 within the other template files. The finished
#   program is split into three files, linked together by import statements.
#   In your IDE, ensure all files are part of the same project so the Python
#   interpreter can locate them.
# 4. Before submission, you should remove these instructions from this
#   template file and add your own program comments instead. This template file
#   has omitted program comments, which are your responsibility to add. Any
#   other 'placeholder' comments should be removed from your final submission.
"""
-------------------
Student Information
-------------------
"""

"""
Name: Ashraf Bin Saleem
Student ID: 31039960

Start Date:  28/5/2020
Last Edit Date: 8/6/2020
"""

"""
---------------------
Overview Of Program
---------------------
"""

"""
This file contains code for the task 3.

The objective of this program is to create a visual graph based on the data output through the simulation. The data
outputted would be number of people infected for each day. Hence a line graph will be used to show the progress of the
infection spread each day.  
"""

"""
-----------------------
Beginning Of Code
-----------------------
"""
# Importing task 2
from a2_31039960_task2 import *

# Importing pandas
# as (keyword) works as a form of alias/namespace.
import pandas as pd

# import statement to make use of functions/classes from earlier task(s).
# (change the xxxxxxxx to match the actual filename.)

# Creating a method to visualize the graph and save it as a .png file by the name of task3.
def visual_curve(days, meeting_probability, patient_zero_health):
    # result will contain the output of the run simulation which is a list of the number of infected people each day.
    result = run_simulation(days, meeting_probability, patient_zero_health)
    # converting result into pandas DataFrame.
    df = pd.DataFrame(result)
    # creating the plot line graph with legends turned off.
    graph = df.plot.line(legend=False)
    # setting the y axis as count to represent the number of infected
    graph.set_ylabel('Count')
    # setting the x axis as count to represent the number of days being ran in the simulation
    graph.set_xlabel('Days')
    # saving the figure as a png file by the name of task 3
    graph.figure.savefig('task3.png')


if __name__ == '__main__':
    # running the visual curve method
    visual_curve(60, 0.25, 49)
# do not add code here (outside the main block).
