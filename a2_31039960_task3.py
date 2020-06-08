"""
-------------------
Student Information
-------------------

Name: Ashraf Bin Saleem
Student ID: 31039960

Start Date:  28/5/2020
Last Edit Date: 8/6/2020
"""

"""
---------------------
Overview Of Program
---------------------
This file contains code for the task 3.

The objective of this program is to create a visual graph based on the data output through the simulation. The data
outputted would be number of people infected for each day. Hence a line graph will be used to show the progress of the
infection spread each day.  
"""

"""
-----------------------
Code
-----------------------
"""
# Importing task 2
from a2_31039960_task2 import *

# Importing pandas
# as (keyword) works as a form of alias/namespace.
import pandas as pd

simulation_days = 0  # initializing a global variable for the number of days the simulation will take place for
simulation_meeting_probability = 0  # initializing a global variable for the meeting probability among patients
simulation_patient_zero_health = 0  # initializing a global variable for patient zero health

"""
A method to visualize the graph and save it as a .png file by the name of task3.
:param days: number of days the simulation will run for
:param meeting_probability: the meeting probability among patients
:param patient_zero_health: the initial starting health of patient zero
"""
def visual_curve(days, meeting_probability, patient_zero_health):
    result = run_simulation(days, meeting_probability, patient_zero_health)  # result will contain the output of the run simulation which is a list of the number of infected people each day.
    df = pd.DataFrame(result) # converting result into pandas DataFrame.
    graph = df.plot.line(legend=False)  # creating the plot line graph with legends turned off.
    graph.set_ylabel('Count')  # setting the y axis as count to represent the number of infected
    graph.set_xlabel('Days')  # setting the x axis as count to represent the number of days being ran in the simulation
    graph.figure.savefig('task3.png')  # saving the figure as a png file by the name of task 3


"""
A method to ask the user for inputs for the number of days the simulation will run for, the meeting probability
among patients and the initial starting health for patient zero.
"""
def user_input():
    global simulation_days
    global simulation_meeting_probability
    global simulation_patient_zero_health
    print("Welcome, please key in the requested inputs.") # welcoming the user and asking them to key inputs.
    simulation_days = int(input("Please enter the number of days the simulation will run for (eg 60) : "))  # asking user to key in the number of days the simulation will run for.
    simulation_meeting_probability = float(input("Please enter the meeting probability from 0.0 to 1.0 (eg: 0.25) : "))  # asking the user to key in the meeting probability among patients
    simulation_patient_zero_health = int(input("Please enter the patient zero health from 0 to 100 in integer form (eg: 49) : "))  # asking the user to key in the health of patient zero


if __name__ == '__main__':
    user_input()  # running the user_input method
    visual_curve(simulation_days, simulation_meeting_probability, simulation_patient_zero_health)  # running the visual_curve method

