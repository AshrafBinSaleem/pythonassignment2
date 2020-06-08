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

# Importing task 1
from a2_31039960_task1 import *
# Importing random
import random

# patient_dict -> map the name with Patient object
# { str : Patient }
# key = patient_name (str) & value =  Patient_object
patient_dict = {}


class Patient(Person):
    """
    Patient is a class inherited from Person.
    """

    def __init__(self, first_name, last_name, health):
        """
        Constructor
        first_name: str -> the first name of patient
        last_name: str -> the last name of patient
        health: int -> health of patient
        """

        Person.__init__(self, first_name, last_name)
        self.health = health

    def get_health(self):
        """
        Method will return patient health
        :return: self.health
        """

        return self.health

    def set_health(self, new_health):
        """
        Method will allow patient health to be modified
        :param new_health: new health input
        """

        self.health = round(new_health)

    def is_contagious(self):
        """
        Method will check whether or not a patient is contagious
        :return: it will return true or false based on whether or not it meets the requirements specified
        """

        # return true if patient health is between or equal to 0 and 49 else return false
        if 0 <= self.health <= 49:
            return True
        else:
            return False

    def infect(self, viral_load):
        """
        The method will infect the user it is called upon.
        viral_load: is the viral load produced by each person.
        """

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

    def get_viral_load(self):
        """
        The method wil return the patient viral load
        :return: viral load based on the calculation in the method.
        """

        return 5.0 + (pow((self.health - 25.0), 2)/62.0)

    def sleep(self):
        """
        This method will increase the patient health when called
        """

        self.health += 5
        if self.health >= 100:  # if the health goes over 100 reset it to 100
            self.health = 100

    def __str__(self):
        """
        Return the information about the object.
        :return: first_name, last_name and get_health
        """

        return self.first_name + " " + self.last_name + " : " + str(self.get_health())


def run_simulation(days, meeting_probability, patient_zero_health):
    """
    Method to run the simulation
    :param days:
    :param meeting_probability:
    :param patient_zero_health:
    :return: contagious_count_list
     """

    # returning patient_dict with all patients health starting at 75.
    patients = load_patients(75)
    # setting patient zero health based on user input at the parameters.
    patients[0].set_health(patient_zero_health)
    # creating a list to hold the amount of contagious people for each day the simulation is ran.
    contagious_count_list = []
    # looping through each day of the simulation.
    for day in range(days):
        # count is a variable that stores the number of contagious people for that particular day
        count = 0
        # looping through each patient in the patients list
        for patient in patients:
            # looping through each friend of the patients
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


def dict_loader(name, health):
    """
    Creating a dictionary to store name and patient object as value.
    name: str -> string read from text file.
    health: int -> provided by user.
    :return: patient_dict[name]
    """

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


def load_patients(initial_health):
    """
    #Method to load (initialize) people
    #Initial_health: int -> to initialize the person health.
    :return: patient_list
    """

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

            # Assigning the dictionary value based on the input of the first half of the line (aka the person name)
            # and providing the initial starting health value.
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
    """
    Main method to run all functions required for program to work.
    """

    # Running example test case 1
    test_result = run_simulation(15, 0.8, 49)
    # results of test case 1
    print(test_result)

    # Running example test case 2
    test_result = run_simulation(40, 1, 1)
    # results of test case 2
    print(test_result)

