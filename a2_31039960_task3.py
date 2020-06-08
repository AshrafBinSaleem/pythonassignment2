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
---------------------
Predictions
---------------------

The program generates results that match the predicted trend for each test case provided to us while they may not be 
the exact same results each time this is due to some variations within the parameters provided such as the meeting 
probability among patients they will however provide a clear trend shown for the direction of where simulation
calculation area headed to.
"""

"""
----------------------
References
______________________
(1) 
URL: https://www.w3schools.com/python/ref_string_rstrip.asp
Date of retrieval: 3/06/2020

(2)
URL: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
Date of retrieval: 4/06/2020

(3)
URL: https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot
Date of retrieval: 4/06/2020

(4)
URL: https://realpython.com/documenting-python-code/#basics-of-commenting-code
Date of retrieval: 8/6/2020
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

# initializing a global variable for the number of days the simulation will take place for
simulation_days = 0
# initializing a global variable for the meeting probability among patients
simulation_meeting_probability = 0
# initializing a global variable for patient zero health
simulation_patient_zero_health = 0


def visual_curve(days, meeting_probability, patient_zero_health):
    """
    A method to visualize the graph and save it as a .png file by the name of task3.
    :param days: number of days the simulation will run for
    :param meeting_probability: the meeting probability among patients
    :param patient_zero_health: the initial starting health of patient zero
    """

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


def user_input():
    """
    A method to ask the user for inputs for the number of days the simulation will run for, the meeting probability
    among patients and the initial starting health for patient zero.
    """

    global simulation_days
    global simulation_meeting_probability
    global simulation_patient_zero_health
    # welcoming the user and asking them to key inputs.
    print("Welcome, please key in the requested inputs.")
    # asking user to key in the number of days the simulation will run for.
    simulation_days = int(input("Please enter the number of days the simulation will run for (eg 60) : "))
    # asking the user to key in the meeting probability among patients
    simulation_meeting_probability = float(input("Please enter the meeting probability from 0.0 to 1.0 (eg: 0.25) : "))
    # asking the user to key in the health of patient zero
    simulation_patient_zero_health = int(input("Please enter the patient zero health from 0 to 100 in integer form (eg: 49) : "))


if __name__ == '__main__':
    """
    Main method to run all functions required for program to work.
    """

    # running the user_input method
    user_input()
    # running the visual_curve method
    visual_curve(simulation_days, simulation_meeting_probability, simulation_patient_zero_health)

