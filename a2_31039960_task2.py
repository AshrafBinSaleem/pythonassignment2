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

"""
Patient is a class inherited from Person.
"""
class Patient(Person):

    """
    Constructor
    first_name: str -> the first name of patient
    last_name: str -> the last name of patient
    health: int -> health of patient
    """
    def __init__(self, first_name, last_name, health):

        Person.__init__(self, first_name, last_name)
        self.health = health

    """
    Method will return patient health
    :return: self.health
    """
    def get_health(self):
        return self.health

    """
    Method will allow patient health to be modified
    :param new_health: new health input
    """
    def set_health(self, new_health):
        self.health = round(new_health)

    """
    Method will check whether or not a patient is contagious
    :return: it will return true or false based on whether or not it meets the requirements specified
    """
    def is_contagious(self):
        # return true if patient health is between or equal to 0 and 49 else return false
        if 0 <= self.health <= 49:
            return True
        else:
            return False

    """
    The method will infect the user it is called upon.
    viral_load: is the viral load produced by each person.
    """
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

    """
    The method wil return the patient viral load
    :return: viral load based on the calculation in the method.
    """
    def get_viral_load(self):
        return 5.0 + (pow((self.health - 25.0), 2)/62.0)

    """
    This method will increase the patient health when called
    """
    def sleep(self):
        self.health += 5
        if self.health >= 100:  # if the health goes over 100 reset it to 100
            self.health = 100

    """
    Return the information about the object.
    """
    def __str__(self):
        return self.first_name + " " + self.last_name + " : " + str(self.get_health())


"""
Method to run the simulation
:param days:
:param meeting_probability:
:param patient_zero_health:
:return: contagious_count_list
 """
def run_simulation(days, meeting_probability, patient_zero_health):
    patients = load_patients(75)  # returning patient_dict with all patients health starting at 75.
    patients[0].set_health(patient_zero_health)  # setting patient zero health based on user input at the parameters.
    contagious_count_list = []  # creating a list to hold the amount of contagious people for each day the simulation is ran.
    for day in range(days):  # looping through each day of the simulation.
        count = 0  # count is a variable that stores the number of contagious people for that particular day.s
        for patient in patients:  # looping through each patient in the patients list
            for friend in patient.get_friends():  # looping through each friend of the patient
                if random.random() <= meeting_probability:  # checking to see whether or not the patient will meet their friend or not
                    if patient.is_contagious():  # if the patient is contagious, please spread it to the friend they are currently meeting.
                        friend.infect(patient.get_viral_load())
                    if friend.is_contagious():  # if the friend is contagious, please spread it to the patient that is currently visiting them.
                        patient.infect(friend.get_viral_load())

        for patient in patients:  # looping through each patient to check whether or not they are contagious today.
            if patient.is_contagious():  # if patient is contagious please increase count.
                count += 1
            patient.sleep()  # patient goes to sleep at the end of the day.
        contagious_count_list.append(count)  # appending the count to the list to show the number of contagious people each day.
    return contagious_count_list


"""
Creating a dictionary to store name and patient object as value.
name: str -> string read from text file.
health: int -> provided by user.
:return: patient_dict[name]
"""
def dict_loader(name, health):

    if name not in patient_dict:  # validating if dictionary key exist or not, if not create new Person

        person_first_name = name.split(" ")[0]  # assigning first part of string eg : "Gill"
        person_last_name = name.split(" ")[1]  # assigning second part of string eg : "Bates"
        patient_dict[name] = Patient(person_first_name, person_last_name, health)  # creating dictionary input with string name as key and Person as value
    return patient_dict[name]  # returning the dictionary key/value


"""
#Method to load (initialize) people
#Initial_health: int -> to initialize the person health.
:return: patient_list
"""
def load_patients(initial_health):
    try:  # Validating if file can be opened
        read_file = open("a2_sample_set.txt", "r")  # reading text file
        patient_list = []  # creating a list to store person objects
        for line in read_file:  # looping through each line in the text file
            line_splitted = line.split(": ")  # splitting each line into half's
            """
            #Assigning the dictionary value based on the input of the first half of the line (aka the person name)
            and providing the intial starting health value.
            """
            patient = dict_loader(line_splitted[0], initial_health)
            for friend_name in line_splitted[1].split(", "):  # adding friends
                friend_person = dict_loader(friend_name.rstrip(), initial_health)   # adding a person friend to the list by checking the second half of the line
                patient.add_friend(friend_person)  # adding the value friend
            patient_list.append(patient)  # adding a person to the person_list[]
        return patient_list  # returning person_list[]
    except IOError:  # returns and error if file cannot be found or opened
        print("File could not be open !, please check if file named a2_sample_set.txt exist or close file !")


if __name__ == '__main__':
    test_result = run_simulation(15, 0.8, 49)  # Running example test case 1
    print(test_result)  # results of test case 1

    test_result = run_simulation(40, 1, 1)  # Running example test case 2
    print(test_result)  # results of test case 2

