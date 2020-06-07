# Task 2 code template for FIT9136 Assignment 2.
# Instructions to students:
# 1. Where required, replace the *pass* statements with your own method and
#   function definitions. Your submission must comply with the specification:
#   do not rename specified functions or change the number or type of arguments
#   or return values; otherwise you will be deemed not to have demonstrated
#   clear comprehension of the specified instructions. (You may define
#   your own additional functions and instance variables if you wish, as long
#   as these don't contradict the specified requirements. You may also
#   import any libraries allowed by the assignment specification.)
# 2. Complete task 2 within the framework of this template file.
# 3. Modify the filename (and import statement(s) where required) to replace
#   the xxxxxxxx with your student ID number.
# 4. Complete tasks 1 and 3 within the other template files. The finished
#   program is split into three files, linked together by import statements.
# 5. In this file, you may define your own testing code within the main block
#   to check if your simulation is working when running this script file
#   directly. Code in the main block will not be run by the automarker algorithm,
#   which will instead test the specified functions/methods by attempting to
#   call them directly according to how they are defined in the assignment 
#   requirments specification.
# 6. Before submission, you should remove these instructions from this
#   template file and add your own program comments instead. This template file
#   has omitted program comments, which are your responsibility to add. Any
#   other 'placeholder' comments should be removed from your final submission.
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

This file contains code for the task 2.

The objective of this program is to create a simulation about infection among patients (patients objects created by the 
Patient Class which inherit Person Class). The infection simulation will display the spread of virus by each day the
simulation progresses based on the meeting probability between patients and their friends and the starting health of
patient zero (who will determine the lethality of the infection).
"""

"""
-----------------------
Beginning Of Code
-----------------------
"""

# Importing task 1
from a2_31039960_task1 import *
# Importing random
import random

# patient_dict -> map the name with Patient object
# { str : Patient }
# key = patient_name (str) & value =  Patient_object
patient_dict = {}


class Patient(Person):
    """Patient is a class inherited from Person."""

    # Constructor
    # first_name: str -> the first name of patient
    # last_name: str -> the last name of patient
    # health: int -> health of patient
    def __init__(self, first_name, last_name, health):
        Person.__init__(self, first_name, last_name)
        self.health = health

    # method will return patient health
    # return will return self.health
    def get_health(self):
        return self.health

    def set_health(self, new_health):
        """
        Method will allow patient health to be modified
        :param new_health: new health input.
        """
        self.health = round(new_health)

    # method will check whether or not a patient is contagious
    # it will return true or false based on whether or not it meets the requirements specified
    def is_contagious(self):
        # return true if patient health is between or equal to 0 and 49 else return false
        if 0 <= self.health <= 49:
            return True
        else:
            return False

    # the method will infect the user it is called upon
    def infect(self, viral_load):
        # if user health is equal or below 29 use this calculation
        if self.health <= 29:
            self.health = round(self.health - (0.1 * viral_load))
        # if user health is between 29 and 50 use this calculation
        elif 29 < self.health < 50:
            self.health = round(self.health - (1.0 * viral_load))
        # if user health is above 50 use this calculation
        elif self.health >= 50:
            self.health = round(self.health - (2.0 * viral_load))
        # if user health dips below 0, reset health to 0
        if self.health < 0:
            self.health = 0

    # the method wil return the patient viral load
    # return will return the provided formula calculation
    def get_viral_load(self):
        return 5.0 + (pow((self.health - 25.0), 2)/62.0)

    # This method will increase the patient health when called
    def sleep(self):
        self.health += 5
        if self.health >= 100:
            self.health = 100

    # Return the information about the object.
    def __str__(self):
        return self.first_name + " " + self.last_name + " : " + str(self.get_health())


def run_simulation(days, meeting_probability, patient_zero_health):
    """

    :param days:
    :param meeting_probability:
    :param patient_zero_health:
    :return:
    """
    # returning patient_dict with all patients health starting at 75.
    patients = load_patients(75)
    # setting patient zero health based on user input at the parameters.
    patients[0].set_health(patient_zero_health)
    # creating a list to hold the amount of contagious people for each day the simulation is ran.
    contagious_count_list = []
    # looping through each day of the simulation.
    for day in range(days):
        # count is a variable that stores the number of contagious people for that particular day.
        count = 0
        # looping through each patient in the patients list
        for patient in patients:
            # looping through each friend of the patient
            for friend in patient.get_friends():
                # checking to see whether or not the patient will meet their friend or not
                if random.random() <= meeting_probability:
                    # if the patient is contagious, please spread it to the friend they are currently meeting.
                    if patient.is_contagious():
                        friend.infect(patient.get_viral_load())
                    # if the friend is contagious, please spread it to the patient that is currently visiting them.
                    if friend.is_contagious():
                        patient.infect(friend.get_viral_load())
        # looping through each patient to check whether or not they are contagious today.
        for patient in patients:
            # if patient is contagious please increase count.
            if patient.is_contagious():
                count += 1
            # patient goes to sleep at the end of the day.
            patient.sleep()
        # appending the count to the list to show the number of contagious people each day.
        contagious_count_list.append(count)
    return contagious_count_list

# creating a dictionary to store name and patient object as value.
# name: str -> string read from text file.
# health: int -> provided by user.
def dict_loader(name, health):
    # validating if dictionary key exist or not, if not create new Person
    if name not in patient_dict:
        # assigning first part of string eg : "Gill"
        person_first_name = name.split(" ")[0]
        # assigning second part of string eg : "Bates"
        person_last_name = name.split(" ")[1]
        # creating dictionary input with string name as key and Person as value
        patient_dict[name] = Patient(person_first_name, person_last_name, health)
    # returning the dictionary key/value
    return patient_dict[name]

# Method to load (initialize) people
# initial_health: int -> provided by user.

def load_patients(initial_health):
    # Validating if file can be opened
    try:
        # reading text file
        read_file = open("a2_sample_set.txt", "r")
        # creating a list to store person objects
        patient_list = []
        # looping through each line in the text file
        for line in read_file:
            # splitting each line into half's
            line_splitted = line.split(": ")

            """
            Assigning the dictionary value based on the input of the first half of the line (aka the person name)
            and providing the intial starting health value.
            """
            patient = dict_loader(line_splitted[0], initial_health)

            # adding friends
            for friend_name in line_splitted[1].split(", "):
                # adding a person friend to the list by checking the second half of the line
                friend_person = dict_loader(friend_name.rstrip(), initial_health)
                # adding the value friend
                patient.add_friend(friend_person)
            # adding a person to the person_list[]
            patient_list.append(patient)
        # returning person_list[]
        return patient_list
    # returns and error if file cannot be found or opened
    except IOError:
        print("File could not be open !, please check if file named a2_sample_set.txt exist or close file !")


if __name__ == '__main__':
    # You may add your own testing code within this main block
    # to check if the code is working the way you expect.

    #This is a sample test case. Write your own testing code here.
    #test_result = run_simulation(15, 0.8, 49)
    #print(test_result)
    # Sample output for the above test case (15 days of case numbers):
    # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]
    #
    # Note: since this simulation is based on random probability, the
    # actual numbers may be different each time you run the simulation.


    # Another sample test case (high meeting probability means this will
    # spread to everyone very quickly; 40 days means will get 40 entries.)
    test_result = run_simulation(40, 1, 1)
    print(test_result)
    #sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200, 
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

    

# do not add code here (outside the main block).
